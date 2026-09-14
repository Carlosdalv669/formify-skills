# Nota de encargo y contrato de mediación

## Purpose and default profile
The mandate. It entitles the agency to advertise, show and receive money, and it fixes the
fee. Default profile: official in ES-IB, ES-CT, ES-VC; professional elsewhere. Boxes first,
clauses second; a value appears once, in its box, and the clauses refer to the boxes. Chain:
encargo, then llaves.

## Boxes
A. Partes: client and agency side by side; box A carries the register line built as
`es-regions.md` describes. B. Inmueble. C. Encargo y honorarios. D. Seguro y garantía
(optional). E. Estipulaciones. The statutory minimum content sits in A to D and the freely
agreed terms in E, visibly separate: Baleares requires that separation and it is good practice
everywhere.

## What to ask
1. Region of the property.
2. Owners: name, ID document, address, e-mail, phone; any representative and on what authority;
   private individual selling their own home (consumer) or a business.
3. Family home of a married owner whose spouse is not on the title: offer the spouse as a
   signer (optional here, mandatory in the arras).
4. Property: address, cadastral reference, Registro and finca, declared charges, protected
   regime, relevant legal situation (proceedings, occupation, existing tenancy).
5. Sale or letting; price or rent; exclusive (default) or not; start and end dates: three to
   six months is normal, never propose more than twelve.
6. Fee: percentage or amount; the tax and the total including it; when paid (default at the
   deed, sometimes half at the arras).
7. Cap on deposits the agency may receive, as a percentage (default 10 %).
8. Consequence of a direct sale under exclusivity (default half the fee). If the user wants the
   whole fee, say in the chat that courts moderate clauses out of proportion to the work done
   and that half has held up best. They decide.
9. Reporting frequency; tacit renewal (default no, with consumers).
10. "Do you want the indemnity insurance and the guarantee in the document?": one question,
    every region, no explanation of who requires it. In Andalucía it admits a policy or a bank
    guarantee.
11. Signed remotely or at the client's home? An unsolicited home visit makes the withdrawal
    period 30 days instead of 14.
Never asked: the ten identity values (they come from the ID scan at signing).

## Fields
| name | printed or field | size | required | who | tink |
|---|---|---|---|---|---|
| cliente_nombres, cliente_docs, cliente_domicilio, cliente_email, cliente_telefono | printed, or field when the user lacks the value | 180 / 120 / 180 / 180 / 100 pt | yes | owner | - |
| representante_bloque | printed, only with a representative | - | no | user | - |
| registro_linea, establecimiento_linea, agencia_*, agente_* | printed, from memory and `es-regions.md` | - | yes | agency | - |
| box B and C values (inmueble_*, refcat, registro, finca, cargas_declaradas, regimen_proteccion, situacion_juridica, operacion, precio_*, fecha_inicio, fecha_fin, exclusiva_si_no, honorarios_*, impuesto_*) | printed | - | yes | user | - |
| rc_aseguradora, rc_nif, rc_poliza, garantia_entidad, garantia_nif, garantia_numero | printed, only when box D was chosen | - | no | agency | - |
| max_arras_pct, consecuencia_venta_directa, informe_periodicidad, preaviso_dias, prorroga_frase, garantia_frase, idioma_cliente_es | printed, clause variables | - | yes (prorroga_frase no) | user | - |
| dias_desistimiento, agencia_nombre, agencia_direccion, agencia_telefono, agencia_email, fecha_larga | printed, withdrawal block variables | - | consumer only | agency | - |
No tink attributes in this document; the ID scan is a signer setting, not a field.

## Signers and order
Propietario/a (Owner): each owner. Representante (Representative): if any. Cónyuge (Spouse):
the non-owning spouse if wanted. Agente inmobiliario (Estate agent). ID scan for owners and
representative; the agent signs with a drawn signature. No signing order, unless the user wants
owners first.

## Clauses

The clause library of this document is in `es-encargo-clauses.md`: every clause with its ID, its flag
(verbatim, optional with its condition, variant for a region), its variables, the Spanish master
text and the English text. Open it when drafting; copy by ID, never compose.

## Own rules
Do not change a word of ENC-12 or ENC-15 except their fields: statutory text, the exception to
the no-law rule. The direct-sale consequence is proportionate compensation, never a penalty,
never the word "penalización". No waiver of withdrawal. No jurisdiction clause taking a consumer
away from the courts of the property. Question 10 is asked without saying who requires the
insurance.

## Draft title and invitation
Draft title: "Nota de encargo {{inmueble_corto}}". Invitation (at most 500 characters, in the
client's language): "Nota de encargo para la {{operacion}} de {{inmueble_corto}}. Revise los
cuadros A a C, las estipulaciones y la información sobre su derecho de desistimiento. Firme
cuando esté conforme."

## Conflicts noted (not resolved)
- Withdrawal block: OURS treats it as a core part of the document; the guide offers it through
  one yes/no question and lets the user drop it, and the clause file tags it optional. OURS
  followed: included for a consumer signing remotely or at home.
- The guide asks 13 questions (adds the client's language); OURS lists 11. OURS followed.
- Field widths come from the guide only; OURS gives none.
