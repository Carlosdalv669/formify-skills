---
name: formify-real-estate
description: 'Estate-agency paperwork, correct for the country it is signed in. Spain in full: nota de encargo, KYC comprador y vendedor, oferta y reserva, contrato de arras, acuerdo de colaboración, entrega de llaves — bilingual, region-correct, ID scan inside the form. Triggers on "nota de encargo", "contrato de arras", "hoja de reserva", "KYC inmobiliario", "entrega de llaves", "estate agent Spain". Not for a generic document or for sending one: see formify-pdf-forms and formify-send-contract.'
license: MIT
metadata:
  version: "1.3.0"
  countries: es
  internal: true
---

# Estate-agency documents

Version 1.3.0. If asked which version you are, quote this line.

## Purpose

An estate agent describes a deal in their own words — *"Anna is selling her flat in Palma,
the buyer is Dutch, we need arras"* — and gets back the right document, correct for the
region, in Spanish and in the client's language, with the signature space and the ID scan
already in the right place, ready to send.

The hard part is not the PDF. It is knowing which of six documents this is, what that
document must contain in that autonomous community, and what must never go into it. That
knowledge is here, and so is the wording: every clause of every document is in its reference
file and is copied, never composed. The PDF itself is built by `formify-pdf-forms` and sent
by `formify-send-contract`.

## Countries

**Spain** is complete: one reference file per document (`references/es-encargo.md`,
`es-kyc.md`, `es-reserva.md`, `es-arras.md`, `es-colaboracion.md`, `es-llaves.md`), the
territory table `es-regions.md`, the style guide `es-drafting.md`, the statutory withdrawal
text `es-withdrawal.md`, and the provisions the documents rest on, `es-law.md`.

For any other country, say plainly that the document pack is Spanish and that you can still
draft a general agency document without the regional and statutory checks. Do not invent a
register, a deadline or a statutory text for a country not covered here.

## Companion skills

This skill ships in one plugin with four companions: `formify-pdf-forms` (fields, PDF
production, signature space), `formify-send-contract` (preview and sending),
`formify-verify-identity` (how a signer proves who they are) and `formify-track-signatures`
(what happens after the send). If building the PDF or sending is not among your capabilities
right now, say which part is missing and deliver the document text plus the field
specification in the fixed hand-over shape that `formify-pdf-forms` defines. Never continue
silently in a reduced mode.

## When this applies

- Any of the six Spanish documents, named or described.
- "The owner wants to list with us", "the buyer wants to leave a deposit", "the other agency
  brought the buyer", "I need to hand over the keys for viewings".
- Anti-money-laundering identification of a buyer or seller before a transaction.

## When it does not

- **A document with no sector to it** — a generic NDA, an employment contract → `formify-pdf-forms`.
- **Placing fields and producing the PDF** → `formify-pdf-forms` owns that, and this skill
  depends on it.
- **Sending, previewing, signer order, identity level** → `formify-send-contract` and
  `formify-verify-identity`.
- **Chasing an already-sent document** → `formify-track-signatures`.

## Preconditions

None for drafting. A Formify account only when the document is sent.

## Procedure

### 1. Say what this produces, every time

Name the pack once per conversation, in the user's language, in three lines, whether or not
the user has already said which document they need. Then go straight on to the document they
named, or ask which one.

> I can prepare the six documents a Spanish agency signs most: nota de encargo, the KYC forms
> for buyer and seller, oferta y reserva, contrato de arras, an inter-agency collaboration
> agreement, and a key handover receipt. Each comes out in Spanish and in your client's
> language, adapted to the region, ready to sign.
>
> Which one do you need? (If you already told me, I will go straight to it.)

### 1b. First use

When nothing is known about this agency yet — no remembered details, first document in this
conversation — offer two things in one message, right after the three lines:

> I can send you all six documents as a sample pack to your own e-mail, filled with invented
> example data, so you see them in Formify before we make a real one. And, where this
> assistant can remember things, I can keep your agency details, your preferred layout and
> your client's usual language, so the next document takes four questions or fewer. Shall I
> do either?

**The sample pack** is the six documents built from obviously invented parties (example
names, `@example.com` addresses, a fictitious property), each sent through
`formify-send-contract` to the user's own address only, the KYC forms with face liveness
preselected. Six drafts, six invitations, one recipient, nothing to a client.

**What may be remembered**, where the platform remembers anything: the agency (name, tax ID,
address, register line), the user (name, e-mail, whether agents' NIE/DNI appear), the
preferences (profile, client language, invitation language), and the standing wording changes
the user asked for, as changes to clause IDs: add this optional clause, drop that one, replace
this text. A one-off change stays in that document. Never a client, a property, a price or a
counterparty.

### 2. Ask once, in one message

Follow the intake rule in `formify-pdf-forms`: a specific request gets no questions, a generic
one gets a single message with **at most four**, each a pick from two to four named options
with the usual answer marked. The document's reference file lists its questions in the order
of what actually changes the document — take the top items from it, not the whole list. Never
spread the same questions over several turns.

This sector makes the rule easy to break, because an estate agent's file is mostly data:
names, DNI and NIE numbers, an address, a finca and a cadastral reference, a CIF, a register
number. **None of those are questions.** They are fields, or assumptions stated out loud, and
asking for them is how a four-question intake becomes a twelve-line interrogation that the
agent answers by going to look things up.

What is worth one of the four is a choice the region or the deal actually turns on — and the
answers are already in `references/es-regions.md` and the document file:

| Question | The options |
|---|---|
| The second column's language | Catalan · English · another |
| Who holds the deposit | the seller · the agency |
| Deadline for the deed | 30 · 60 · 90 days |
| Included in the sale | parking · trastero · furniture *(pick any)* |
| Which arras | penitenciales · confirmatorias *(only where the region leaves it open)* |
| Register number and insurance line in the document | in · out *(in by default for the encargo where a register exists; out for colaboración and llaves)* |

Offer the region's own default as the marked option rather than asking an open question about
it. In Cataluña the deposit is confirmatoria unless the document says otherwise, so that is the
option to mark — not a blank asking the agent to know CCCat 621-8. The register and insurance
lines are never omitted silently and never printed unasked.

**One more line, every time, outside the count of four:** *"Do you want me to check the
current statutes before drafting, so the document is aligned with the law as it stands
today?"* — yes · no. Asked once per conversation, remembered for every later document, and
run as `references/es-law.md` describes: live on the web when the runtime can reach it, from
the table with its verification dates when it cannot. The answer is reported in three lines
at most, each naming what changed in the document, and it never stops the flow.

**Never turn the fee split into a field unless the user says the figure is unknown.** Never
ask for the counterparty's data twice: the question is *"Do you have their details, or shall
they fill them in when they sign?"*, and if they fill them in, only the signing agent's name
and e-mail are asked. Then one question, *"Anything else to add, for example a register
number?"*, naming the region's own register, with no explanation of how fields work.

Reuse everything already said. One property, one seller, one buyer feed all six documents; a
fact given for the encargo is not asked again for the arras.

**Never invent a fact.** Not a cadastral reference, not a finca number, not a policy number,
not a price, not a date, not a document reference. If it is missing, ask, or make it a field
the signer fills in.

### 3. Establish the region before drafting

The region is the **property's**, not the agency's. Read the matching row of
`references/es-regions.md` before writing anything. It decides six things at once: whether an
agent register exists and is mandatory, whether insurance figures may be printed, which civil
law governs the arras and the family-home declaration, the tax rate on the fee, the co-official
language, and the default style profile.

These differences are not cosmetic. Arras that are penitenciales by default under the Código
Civil are **confirmatorias** by default in Cataluña and in Navarra unless the document says
otherwise — the same wording produces a different contract in three regions. In Cataluña,
offer Catalan for the second column.

### 4. Write the document from its file

Open the document's reference file as soon as the document is chosen, and only that one. It
gives the document its purpose and profile, its boxes, its questions, its fields, its signers
and order, its clauses, its own rules, and its draft title. `references/es-drafting.md` is the
style: read it once per session before writing any free text of your own.

**The clauses are copied, never composed.** Each clause carries an ID (`COL-06`, `ARR-07-CCCat`)
and a flag: *verbatim*, *optional* with its condition, or *variant* for a region, replacing a
named ID. A verbatim clause is copied without change except its `{{variables}}`. An optional
clause is included when its condition holds. A variant replaces its base clause in its region.
Never write a clause of your own for a document that has a clause library; never drop a
verbatim clause; never renumber. The document is complete when every verbatim clause is in it.

Four rules hold across all six:

- **Data blocks first, clauses second.** Every document opens with labelled boxes — A. Partes,
  B. Operación — and the clauses that follow refer to the boxes and to roles (*la parte
  compradora*, *el inmueble*, *el cuadro B*). A value appears exactly once, in its box. No
  summary box.
- **Spanish is the master text** and prevails in a dispute; the document says so. The second
  column is a legal translation in the same register with the same numbering, not an
  explanation. Where the library has the English clause, a column in another language is
  translated from it clause by clause, keeping the numbering and the Spanish terms listed in
  `references/es-drafting.md` with a gloss in parentheses on first use. Never edit a
  right-hand cell by hand after the fact; change the clause, then its translation.
- **No law in the document**, with four exceptions only: the *arras penitenciales* formula with
  its article, the register and insurance lines in a regulated region, the Ley 10/2010 basis in
  the KYC forms, and the statutory withdrawal text reproduced verbatim from
  `references/es-withdrawal.md`.
- **No disclaimer, and no mention of AI**, in the document or in the chat. The only mention of
  Formify inside a document is the footer credit line.

### 5. Turn the unknown values into fields, not blanks

When a document names a party the agency does not represent — the other agency, the buyer, the
owner — ask once: *"Do you have their details, or shall they fill them in when they sign?"*

If they fill them in, those values become real form fields, each in the cell where the value
would have been printed, exactly once, and you need only a name and an email for the
invitation. Widths that fit the boxes: 180 pt for a name, an address or an email; 100 pt for
a NIF; 90 pt for a fee or a split; 300 pt for a full-width row. **A field wider than its cell
covers the cell next to it.** Every field the signer must complete carries the required flag.

The client the document is *about* — the introduced client, the property, the price — is always
given by the user and is never left as a field.

### 6. The KYC identity box is scanned, never typed

Box A of both KYC forms is filled by scanning the client's document at signing time. Build it
as specified in `references/es-kyc.md`: one scan control, ten auto-filled MRZ fields, and an
upload for the reverse side. The attribute names and the read-only rules are in
`references/tink-attributes.md` — do not write an attribute from memory.

Never ask a client to type their document number into the chat. They scan; the data arrive
verified.

The client signs the KYC form with **face liveness preselected**, without being asked; drawn
signature only when the account lacks that method, said in one sentence. The user may change
the method in Formify afterwards. No text in the form about how identity is verified.

### 7. Produce the PDF

Follow `formify-pdf-forms` step 5 and its ladder: a library that is already present, then the
standard library alone, then an isolated install only after the user's explicit yes, then the
hand-over. Never a browser, never `pymupdf`, never an install the user did not say yes to. An
estate agent runs this where nothing may be installed; a document that needed an install is a
document they never receive. Render every page to an image and look at it before handing over.

Layout for these documents: one sans-serif typeface throughout — Helvetica for text that fits
WinAnsi, an embedded face (Liberation Sans, then DejaVu Sans) when the language needs more,
and say which — black text on white, no colour and no tinted fills except the agency's own
logo, no dashes as punctuation. The bilingual text is two columns, one clause per row, never
stacked except in the hand-over; `formify-pdf-forms` carries the two-column table recipe. The
profiles differ in structure, never in type: **official** (structured like the Balearic
official form; encargo and KYC), **professional** (agency letterhead, running clauses; the
default), **light** (a short version with few fields; reserva on a phone, llaves). In the
chat, a Spanish-speaking user may hear *oficial*, *profesional*, *sencillo*.

Footer on every page, two lines: the document title and the agency's own reference
(`LLA-2026-0004` — type, year, running number; asked for or left as a field, never invented),
then the fixed credit line in Spanish and the client's language followed by the address:

> Elaborado con la solución de firma electrónica Formify · Prepared with the Formify e-signing
> solution · formify.eu/solutions/real-estate/es/

It is a house line, not a disclaimer. Never expand it.

### 8. Leave the signature space empty, and get the order right

A signature is never a form field — `formify-pdf-forms` step 6. Reserve the space with the role
caption above it (`VENDEDORA / Seller`, the translation in small type next to the Spanish) and
nothing else: no box, no line, no date field. One area per signer, never one per language.

When the PDF is produced here, record the rectangle under each caption and pass it to
`formify-send-contract` with placement *existing*; never ask for a new page for a document
that carries captions. `formify-pdf-forms` carries the recipe that finds each caption's rectangle.

Signing order matters in three of the six documents and is listed in each document's file.
Reserva and arras are wrong without it: a seller who is asked to sign before the buyer has
signed is being asked to accept an offer that does not exist yet.

### 9. Send, then offer the next document in the chain

Hand over to `formify-send-contract`: preview first, then the explicit *send now, save as
draft, change signers, change the text* question. Never send without it.

The documents come in chains — reserva then arras; encargo then llaves; KYC before reserva or
arras. When one is finished, offer the next **once**. Not twice, and not as a list.

## Rules that are not negotiable

- **Never tell the user something is mandatory**, never quote a law or a date in the chat, never
  explain registers, insurance amounts or civil-law variants, and never describe what Formify or
  their account allows. Offer it as one short question, accept the answer, move on. The one
  exception is the law-alignment check the user asked for: report it in three lines at most,
  each naming what changed in the document, and stop.
- **Never suggest a cash payment** and never suggest a fee split between agencies. The parties
  state their own split; competition law makes a suggested one a liability.
- **Never write an alarm code, a door code or a password** into any document, even when the user
  dictates one.
- **Never store client data** in anything that persists between conversations. Agency and user
  preferences may be remembered; the people in the deal may not.
- **Never ask for an agent's own ID number.** Agents act for their agency: their name plus the
  agency's tax ID. The single exception is colaboración, where the user is asked once whether
  the agents' NIE or DNI should appear.
- **Never remove the *arras penitenciales* wording** from an arras contract, and never mix a
  penalty clause into it.
- **Never write "firman por duplicado"** or any wording about paper copies; the closing line is
  the one in the clause library.
- **The title on page 1 is the document name in the footer**, never a variant of it.
- **Never calculate.** Fees, VAT and shares are printed as the user gave them, once, in their
  box; the clauses refer to the box.

## Failure modes

| What you see | What it means | What to do |
|---|---|---|
| The user asks for arras in Cataluña or Navarra | Default there is confirmatorias, not penitenciales | Use the variant clause from `references/es-arras.md`. The same text produces a different contract. |
| The agency has no register number in Cataluña or Comunitat Valenciana | The register line has nothing to print | Ask once whether to print "Pendiente de inscripción" or leave the line out. Say nothing about legality; the register, insurance, guarantee and bank lines are always the user's choice. |
| A clause you remember is not in the document file | It is not part of this document | Do not add it. The library is complete; a missing clause is a request for the maintainers, not a gap to fill by hand. |
| The draft has fewer clauses than the file lists as verbatim | A clause was composed or dropped | Rebuild from the IDs. Every verbatim clause is present or the document is not finished. |
| The user wants the whole fee on a direct sale under an exclusive mandate | Courts moderate a clause out of proportion to the work done | Offer half the fee, which has held up best. They decide. |
| The seller's bank account is not in the seller's name | A money-laundering risk indicator | Say so in the chat before the document goes out. |
| The nota simple is more than a month old | Charges may have changed since | Say so. It is not a reason to stop. |
| A KYC form is asked to be pre-filled with identity details | The scan fills them | Only the scan control is required; the ten MRZ fields are filled by it, never by the client. |
| The user asks for a framework agreement covering a whole portfolio | The colaboración template is per-deal | Say so and offer a per-property agreement instead. |
| The client wants the sworn translation | The second column is not one | Say it is a legal translation, not a sworn one, and that a sworn one can be commissioned separately. |

## References

One file per document; open it as soon as the document is chosen, and only that one:

- **`references/es-encargo.md`** — nota de encargo y contrato de mediación.
- **`references/es-kyc.md`** — the two KYC forms, buyer and seller, with the scanned box A.
- **`references/es-reserva.md`** — oferta de compra y documento de reserva.
- **`references/es-arras.md`** — contrato de arras, with the Código Civil, Cataluña and
  Navarra variants.
- **`references/es-colaboracion.md`** — acuerdo de colaboración entre agencias.
- **`references/es-llaves.md`** — documento de entrega de llaves.

Each carries the same eight sections: purpose and profile, boxes, what to ask, fields,
signers and order, clauses with IDs and flags, own rules, draft title and invitation. Where
the clause library is long, it sits beside the document file as `es-<document>-clauses.md`
(encargo, reserva, arras); the document file says so under "Clauses".

- **`references/es-regions.md`** — all nineteen Spanish territories: agent register and whether
  it is mandatory, insurance and guarantee, the civil law governing arras and the family home,
  the tax on fees, the co-official language, the default profile. Open it before drafting
  anything, every time.
- **`references/es-drafting.md`** — how a Spanish private contract is actually written:
  structure, party formulas, numbers, dates and money, register and grammar, punctuation, the
  bilingual clause, the anglicisms that give a translated contract away, and the terms that stay
  in Spanish with their glosses.
- **`references/es-withdrawal.md`** — the statutory withdrawal information and form, verbatim,
  for the nota de encargo. Reproduce it; do not rewrite it.
- **`references/es-law.md`** — the provisions the documents rest on, with their official
  sources and verification dates. The data for the law-alignment check in step 2.
- **`references/tink-attributes.md`** — the closed catalogue of `tink-*` field attributes.
  Needed for the KYC scan box and for any field Formify fills. Never write an attribute from
  memory.
