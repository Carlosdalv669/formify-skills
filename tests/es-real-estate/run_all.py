#!/usr/bin/env python3
"""Builds every document in tests/es-real-estate/documents.json (fill, style check, render).

Run from the repository root:

  python3 tests/es-real-estate/run_all.py
  python3 tests/es-real-estate/run_all.py encargo
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skills" / "formify-es-real-estate"
HERE = Path(__file__).resolve().parent


def run(cases=None, only=None):
    cases = cases if cases is not None else json.loads((HERE / "documents.json").read_text(encoding="utf-8"))
    if only:
        cases = [c for c in cases if c["name"] in only]
    failures = []
    for c in cases:
        dest = HERE / "out"
        dest.mkdir(parents=True, exist_ok=True)
        body, pdf = dest / (c["name"] + ".html"), dest / (c["name"] + ".pdf")
        try:
            commands = [
                ["fill.py", "--template", str(SKILL / c["template"]), "--data", str(SKILL / c["data"]), "--out", str(body), "--own", ""],
                ["check_style.py", str(body), "--doc", c["doc"]],
                ["render_pdf.py", "--html", str(body), "--signers", str(SKILL / c["signers"]), "--out", str(pdf),
                 "--profile", c.get("profile", "professional"), "--title", c["title"], "--ref", c["reference"], "--lang", c.get("language", "en")],
            ]
            if c.get("variant"):
                commands[0] += ["--variant", c["variant"]]
            if c.get("no_signatures"):
                commands[-1].append("--no-signatures")
            for cmd in commands:
                r = subprocess.run([sys.executable, str(SKILL / "scripts" / cmd[0])] + cmd[1:], capture_output=True, text=True)
                if r.returncode:
                    raise ValueError(cmd[0] + ": " + (r.stdout + r.stderr).strip()[-600:])
            meta = json.loads((dest / (c["name"] + ".signatures.json")).read_text(encoding="utf-8"))
            signers = json.loads((SKILL / c["signers"]).read_text(encoding="utf-8"))
            expected = 0 if c.get("no_signatures") else len(signers)
            if len(meta["signers"]) != expected or meta["pages"] < 1:
                raise ValueError("signer or page count mismatch")
            if "expect_fields" in c and len(meta.get("form_fields", [])) != c["expect_fields"]:
                raise ValueError("expected %d form fields, got %d" % (c["expect_fields"], len(meta.get("form_fields", []))))
            from pypdf import PdfReader  # type: ignore
            for page in PdfReader(str(pdf)).pages:
                if c["reference"] not in (page.extract_text() or ""):
                    raise ValueError("footer reference missing on a page")
            print("PASS", c["name"], meta["engine"], meta["pages"], "pages", len(meta.get("form_fields", [])), "fields")
        except Exception as e:
            failures.append(c["name"])
            print("FAIL", c["name"], e, file=sys.stderr)
    return 1 if failures or not cases else 0


if __name__ == "__main__":
    code = run(only=sys.argv[1:] or None)
    r = subprocess.run([sys.executable, str(SKILL / "scripts/check_law.py"), "--all"], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "law check: no output")
    raise SystemExit(code)
