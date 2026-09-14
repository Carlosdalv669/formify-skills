# Oferta de compra y documento de reserva

## Purpose and default profile
A buyer makes an offer and leaves money to hold the property. One document, two phases: offer
and reservation (buyer and agency sign), then acceptance (seller signs). Default profile
professional; light when it is signed on a phone during the viewing. It says who holds the money
(the agency, in a client account, on behalf of both parties) and when it comes back (five working
days); it separates the offer phase, where the money is returned in full if there is no
acceptance, from the arras phase, where it is forfeited or doubled; and it sets the arras out as
penitenciales with the express formula, without which the money is presumed a simple advance.
Chain: KYC before it, arras after it.

## Boxes
Labelled data boxes first, conditions second. A value appears once, in its box; the conditions
cite the box and the role (la parte compradora, el inmueble, el cuadro B). No summary box.
A. Partes: the buyers, the sellers, and the agency with its agent and the mandate it acts under
(date of the nota de encargo). B. Operación: property (address, finca and Registro, cadastral
reference, annexes), asking price, date of the viewing and of the nota simple, offered price, a
furniture row when furniture is included (Annex III), reservation amount, destination account,
the transfer-proof upload, the seller's answer deadline with date and time, the arras deadline,
percentage and total, the deed deadline, and the financing row when RES-09 is printed. Then the
conditions (RES-01 to RES-16) and D. Aceptación, which the seller signs (RES-17, RES-18).
Annex II is the nota simple, a PDF the user supplies, merged before the draft. No empty annex
pages.

## What to ask
Only what is not in memory, in the encargo or in the conversation. At most four, in one
message, as choices:
1. Where the reservation goes: the agency's client account (default; the agency is the
   depositary) or another account, for example the seller's (then the seller is the depositary).
   IBAN from memory. If the transfer has not been made yet, say in the chat that the reservation
   does not exist until the money arrives.
2. Reservation amount: €1,000 to €6,000 or around 1 % of the price. Never suggest more than
   5 %.
3. Financing: the purchase depends on a mortgage (RES-09, with deadline, minimum amount and
   bank) or it does not (no block). No default.
4. Deadlines: the seller's answer, date and time (3 to 10 calendar days); the arras (7 to 15
   days) and its percentage; the deed (30 to 90 days).
Also needed, printed or left as fields for the signer: buyers (all of them sign) and seller,
property, viewing and nota simple dates, offered price, furniture if any, whether the buyer pays
the agency a fee (default no), a proposed notary (optional), the property's region for the
RES-08 variant, and the client's language.

## Fields
| name | printed or field | size | required | who | tink |
|---|---|---|---|---|---|
| referencia, lugar, fecha_larga, hora | printed; the time fixes the moment of the offer | - | yes | user | - |
| comprador_nombres, comprador_docs, comprador_domicilio, comprador_email | printed, or field when the user lacks them; several buyers joined with " y " (names) and "; " (documents) | - | yes | buyer | - |
| vendedor_nombres, vendedor_docs, vendedor_domicilio, vendedor_email | printed or field | - | yes | seller | - |
| agencia_*, agente_*, agencia_email, fecha_encargo | printed, from memory | - | yes | user | - |
| inmueble_direccion, inmueble_corto, finca, registro(_tr), refcat | printed; registro as "n.º 3 de Palma" / "no. 3 of Palma" | - | yes | user | - |
| anejos_frase(_tr) | printed: ", con plaza de garaje n.º {{n}} y trastero n.º {{n}}" / ", together with parking space no. {{n}} and storage room no. {{n}}" | - | no | user | - |
| precio_publico_cifra(_tr), precio_cifra(_tr), precio_letras(_tr) | printed; "250.000" and "doscientos cincuenta mil", "250,000" and "two hundred and fifty thousand" | - | yes | user | - |
| muebles (row in box B, Annex III) | printed | - | no | user | - |
| reserva_cifra(_tr), reserva_letras(_tr) | printed | - | yes | user | - |
| cuenta_destino(_tr) | printed: "la cuenta de depósito de la agencia con IBAN ES..." / "the agency's deposit account with IBAN ES...", or "la cuenta de la parte vendedora con IBAN ES..." / "the seller's account with IBAN ES..." | - | yes | user | - |
| depositario, depositario_mayus (+ _tr) | printed: "la agencia" / "La agencia" / "the agency" / "The agency", or "la parte vendedora" / "La parte vendedora" / "the seller" / "The seller" | - | yes | user | - |
| justificante_subir | field, upload button in box B | 75 × 22 | yes | buyer | tink-upload-attachment[1], tink-style-transparent |
| justificante_nombre | field, read-only, filled by the upload | 250 | yes | buyer | tink-uploaded-attachmentname[1] |
| fecha_visita, fecha_nota_simple | printed | - | yes | user | - |
| hora_limite_respuesta, fecha_limite_respuesta(_tr) | printed: "18:00", "12 de septiembre de 2026" / "12 September 2026" | - | yes | user | - |
| dias_arras, porcentaje_arras, arras_total_cifra(_tr), dias_escritura | printed; arras_total = price × percentage | - | yes | user | - |
| fecha_limite_financiacion(_tr), importe_financiacion_cifra(_tr) | printed | - | with RES-09 | user | - |
| honorarios_comprador_frase(_tr) | printed, empty by default: ", salvo los pactados en el encargo de búsqueda de fecha {{fecha}}" / ", except those agreed in the buyer's mandate dated {{fecha}}" | - | no | user | - |
| notario_propuesto_frase(_tr) | printed, empty by default: "; las partes proponen la notaría de {{notaría}}" / "; the parties propose the notary office of {{notaría}}" | - | no | user | - |
| agencia_email_datos, idioma_cliente_es(_tr) | printed | - | yes | user | - |
The upload pair is fixed in the template. No date fields for signers.

## Signers and order
Comprador/a (Buyer): every buyer. Agente inmobiliario (Estate agent): the user's agent.
Vendedor/a (Seller): every seller; when the property is a married seller's family home and the
spouse is not an owner, the spouse also signs the acceptance as Cónyuge (Spouse). Signing order
on: buyers and agent at position 1, sellers at position 2; Formify notifies the seller once buyer
and agency have signed. Drawn signature, no ID scan by default (identification happens in the
KYC); if the user wants identification in this act, ID scan for buyers and sellers. The seller's
acceptance is the signature itself: no boxes to tick.

## Clauses

The clause library of this document is in `es-reserva-clauses.md`: every clause with its ID, its flag
(verbatim, optional with its condition, variant for a region), its variables, the Spanish master
text and the English text. Open it when drafting; copy by ID, never compose.

## Own rules
- Never suggest a cash reservation. If asked, explain the legal ceiling in the chat and propose
  a transfer.
- Never remove RES-08 or change the arras penitenciales formula with its article (1454 CC,
  621-8 CCCat, ley 467 Fuero Nuevo). It is one of the few places where the document cites the
  law.
- A reservation "non-refundable in any case" is not included: with a consumer buyer the clause
  is unfair. Say so.
- The seller's acceptance is their signature. A counter-offer is a new document (RES-18), never
  an edit of this one.
- No 14-day withdrawal block: contracts on immovable property are excluded from that right,
  unlike the nota de encargo.
- No value from a box is repeated in the conditions; the conditions cite the boxes and the
  roles.
- Title "Oferta de compra y documento de reserva", the same name in the footer.

## Draft title and invitation
Draft title: "Oferta y reserva {{inmueble_corto}}". Invitation to the seller (at most 500
characters, in the recipient's language; invitation e-mails exist only in Spanish, English and
Swedish): "Ha recibido una oferta por {{inmueble_corto}}. Revise el documento y, si está
conforme, firme para aceptarla antes del {{fecha_limite_respuesta}}."

## Conflicts noted (not resolved)
- Intake: the guide asks twelve questions, one per message; OURS caps intake at four choices in
  one message. Written to OURS.
- The guide lists an optional `deposito_agencia` that removes the escrow sentence from condition
  2 when the money goes to another account; the clause file has RES-03 as always, with the
  escrow sentence fixed and no variable. Written to the clause file.
- Arras percentage: the guide calls 10 % usual; OURS §4 says 5 to 10 %. Written to OURS.
- The guide's variants section names only Cataluña for condition 7; the clause file also carries
  the Navarra row. Both kept.
