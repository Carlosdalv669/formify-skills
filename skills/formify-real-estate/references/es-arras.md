# Contrato de arras penitenciales

## Purpose and default profile
The seller has accepted; the parties now fix the price, the deposit and the date of the deed.
The document with the most money at stake in the pack. Default profile professional. Four
conditions must all be met for the arras to be penitenciales, and stipulation 3 (ARR-04) meets
them: it names them so, cites the article, gives both parties the right to withdraw, and writes
the consequence for each. A bare mention of the article is not enough: the Supreme Court has
read one as a simple advance. Chain: KYC before it; usually a reserva before it.

## Boxes
Labelled data boxes first, stipulations second. A value appears once, in its box; the
stipulations cite the box and the role. No summary box. A. Partes: every seller with document,
address, marital status and property regime if married; a Cónyuge row when the spouse signs;
every buyer with document and address; anyone acting under a power of attorney ("en nombre y
representación de ... según poder ..."); the agency in the parties block when it holds the
deposit. B. Operación: the property in full (address, floor area, Registro, finca, tomo, libro,
folio, cadastral reference, annexes, how it was acquired, date of the nota simple, charges per
the nota simple, the family-home declaration), price, deposit and percentage, balance, who
receives the deposit and the escrow IBAN when the agency does, the transfer-proof upload, deed
deadline, notary's town, days of notice, days to return the doubled deposit, the financing row
(deadline, bank, minimum amount) when ARR-06 is printed, energy certificate number and letter.
Then the stipulations. Annexes cited (II inventory, III nota simple, IV energy certificate, V
habitability certificate, VI powers) are PDFs the user supplies, merged before the draft. No
empty annex pages.

## What to ask
Reuse everything already in the reserva, in memory or in the conversation. At most four, in
one message, as choices:
1. Region of the property: Código Civil (default, ARR-04) / Cataluña (ARR-04-CCCat) / Navarra
   (ARR-04-FN). It also sets ley_aplicable and the family-home article.
2. Financing: the buyer needs a mortgage (ARR-06, with deadline, bank and minimum amount) or
   does not (ARR-07). Exactly one, never neither and never both. No default.
3. Who receives the deposit: the seller directly (default) or the agency as escrow holder
   (ARR-05, with IBAN).
4. Seller's tax residence: resident in Spain (ARR-13) or not (ARR-12, 3 % withholding).
   Exactly one.
Also needed: all sellers with marital status and regime, and whether the property is a married
seller's family home (spouse as signer, or the declaration that it is not); all buyers with NIE
(if a foreign buyer has none yet, say in the chat that they will need it for the deed); powers
of attorney; the property in full; price, deposit (5 to 10 %) and balance; any seller mortgage
cancelled at the deed out of the buyer's funds; deed deadline (30 to 90 days; foreign buyers
without a NIE need longer; in Cataluña with a notarial deposit, six months maximum), notary's
town, days of notice (7), days to return the doubled deposit (10 to 15); energy certificate
number and letter, habitability certificate where the region uses one, building inspection if
there is one, furniture inventory if included; costs (default: buyer pays transfer tax and stamp
duty, the deed and the registration; seller pays the municipal land value tax, the cancellation
of charges and the current year's IBI unless apportioned); the client's language.

## Fields
| name | printed or field | size | required | who | tink |
|---|---|---|---|---|---|
| agencia_*, agente_* | printed, from memory (heading, and the parties block when escrow holder) | - | yes | user | - |
| referencia, lugar, fecha_larga | printed | - | yes | user | - |
| vendedor_nombres, vendedor_docs, vendedor_domicilio, vendedor_email | printed, or field when the user lacks them | - | yes | seller | - |
| conyuge_nombre, conyuge_doc, conyuge_de | printed, row in box A | - | with spouse | seller | - |
| buyers' names, documents, address, e-mail (box A) | printed or field | - | yes | buyer | - |
| inmueble_direccion, inmueble_corto, superficie_frase(_tr), registro(_tr), finca, registro_detalle(_tr), refcat, titulo_adquisicion(_tr) | printed; "construida de 95 m²" / "of 95 m² built"; "compraventa en escritura de 12 de mayo de 2015" / "purchase by deed of 12 May 2015" | - | yes | user | - |
| anejos_frase(_tr) | printed | - | no | user | - |
| fecha_nota_simple, cargas_frase(_tr) | printed: "se encuentra libre de cargas y gravámenes" / "is free of charges and encumbrances", or "está gravado con hipoteca a favor de X, que la parte vendedora cancelará en el otorgamiento de la escritura" / "is encumbered by a mortgage in favour of X, which the seller shall cancel on execution of the deed" | - | yes | user | - |
| vivienda_familiar_declaracion(_tr) | printed; see fill text below | - | yes | user | - |
| estado_cargas_objeto(_tr) | printed: "libre de cargas, gravámenes, arrendatarios y ocupantes" / "free of charges, encumbrances, tenants and occupants" | - | yes | user | - |
| precio_letras(_tr), precio_cifra(_tr), arras_letras(_tr), arras_cifra(_tr), arras_pct, resto_letras(_tr), resto_cifra(_tr) | printed; balance = price minus deposit | - | yes | user | - |
| hipoteca_vendedor_frase(_tr) | printed, empty by default; see fill text | - | no | user | - |
| arras_depositario_resumen(_tr) | printed: " a la agencia, que las custodia" / " to the agency, which holds them", or " al vendedor" / " to the seller" | - | yes | user | - |
| iban_deposito | printed | - | with ARR-05 | user | - |
| justificante_subir | field, upload button in box B | 75 × 22 | yes | buyer | tink-upload-attachment[1], tink-style-transparent |
| justificante_nombre | field, read-only, filled by the upload | 250 | yes | buyer | tink-uploaded-attachmentname[1] |
| fecha_escritura(_tr), dias_devolucion, lugar_notaria, dias_preaviso_notaria | printed | - | yes | user | - |
| deposito_notarial_frase(_tr) | printed, ES-CT only, otherwise empty; see fill text | - | no | user | - |
| fecha_limite_financiacion(_tr), entidad_financiera, importe_financiacion_cifra(_tr) | printed | - | with ARR-06 | user | - |
| financiacion_cccat_frase(_tr) | printed, ES-CT with ARR-06 only, otherwise empty; see fill text | - | no | user | - |
| muebles_frase(_tr) | printed: " y con los muebles y enseres relacionados en el Anexo II" / " and with the furniture and fittings listed in Annex II" | - | no | user | - |
| cee_numero, cee_letra | printed | - | yes | user | - |
| cedula_frase(_tr) | printed: "; la cédula de habitabilidad n.º {{n}} de fecha {{fecha}} (Anexo V)" / "; habitability certificate no. {{n}} dated {{fecha}} (Annex V)" | - | no | user | - |
| ite_frase(_tr) | printed: "; el informe de la inspección técnica del edificio de fecha {{fecha}}" / "; the building technical inspection report dated {{fecha}}" | - | no | user | - |
| declaraciones_extra(_tr) | printed: ", salvo {{lo que declare}}" / ", except {{...}}" | - | no | user | - |
| notaria_matriz_frase(_tr) | printed; empty = buyer pays the whole notary bill; the legal rule: ", salvo la matriz, que corresponde a la parte vendedora" / ", except the original deed (matriz), which is borne by the seller" | - | no | user | - |
| ibi_frase(_tr) | printed: "el impuesto sobre bienes inmuebles del año en curso" / "the property tax (IBI) for the current year" (default), or "la parte proporcional del impuesto sobre bienes inmuebles del año en curso hasta la fecha de la escritura" / "the proportional part of the property tax for the current year up to the date of the deed" | - | yes | user | - |
| ley_aplicable(_tr) | printed: "la ley española" / "Spanish law"; ES-CT: "la ley española y, en particular, el Código Civil de Cataluña" / "Spanish law and, in particular, the Civil Code of Catalonia"; ES-NC: "la ley española y, en particular, el Fuero Nuevo de Navarra" | - | yes | user | - |
| recibi_frase(_tr) | printed: ". La parte vendedora declara recibir en este acto la cantidad indicada en la estipulación 2.a)" / ". The seller acknowledges receipt of the sum stated in clause 2.a)"; with escrow: ". La agencia declara recibir en depósito la cantidad indicada en la estipulación 2.a), en la que se incluye la reserva de {{n}} € entregada el {{fecha}}" | - | no | user | - |
| agencia_email_datos, idioma_cliente_es(_tr) | printed | - | yes | user | - |

Fill text for the longer variables:
- vivienda_familiar_declaracion, spouse signs: "el inmueble constituye la vivienda habitual de la familia de la parte vendedora, por lo que comparece su cónyuge para prestar el consentimiento previsto en {{artículo}}." Not the family home: "el inmueble no constituye la vivienda habitual de la familia de la parte vendedora, a los efectos de {{artículo}}." Unmarried seller or company: "la parte vendedora no está casada y el inmueble no constituye vivienda familiar alguna." {{artículo}} by region: "el artículo 1320 del Código Civil" (default, also País Vasco, Galicia and Comunitat Valenciana); "el artículo 231-9 del Código Civil de Cataluña" (ES-CT); "el artículo 190 del Código del Derecho Foral de Aragón" (ES-AR); "la ley 81 del Fuero Nuevo de Navarra" (ES-NC); "el artículo 4.3 de la Compilación de derecho civil de las Illes Balears" (ES-IB; "el artículo 67.1" in Eivissa and Formentera).
- hipoteca_vendedor_frase: ", destinándose de esa cantidad la parte necesaria a la cancelación de la hipoteca que grava el inmueble, cuyo certificado de deuda aportará la parte vendedora" / ", the necessary portion of which shall be applied to cancelling the mortgage on the property, the seller providing the lender's debt certificate".
- deposito_notarial_frase (ES-CT, six months maximum): " Las arras se depositan ante el notario {{notario}} por un plazo de {{n}} meses y las partes solicitan la constancia del depósito en el Registro de la Propiedad conforme al artículo 621-8.3 del Código Civil de Cataluña." / " The deposit is lodged with notary {{notario}} for {{n}} months and the parties request that the deposit be recorded at the Land Registry under article 621-8.3 of the Civil Code of Catalonia." Explain in the chat: the notary releases the arras to the entitled party; it protects the buyer against a sale to a third party.
- financiacion_cccat_frase (ES-CT with ARR-06): ", conforme al artículo 621-49 del Código Civil de Cataluña, y la parte compradora dejará a la vendedora en la situación en que se hallaría de no haberse celebrado el contrato" / ", under article 621-49 of the Civil Code of Catalonia, and the buyer shall leave the seller in the position it would have been in had the contract not been concluded". Empty everywhere else, including ES-NC.

## Signers and order
Vendedor/a (Seller): every seller. Cónyuge (Spouse): the non-owner spouse when the property is
the family home. Comprador/a (Buyer): every buyer. Agencia depositaria (Escrow agency): only
when the agency holds the deposit. Signing order on: sellers and spouse at position 1, buyers at
2, the escrow agency at 3 if it is involved. ID scan for sellers, spouse and buyers (face
liveness if the account has it and the user prefers it); the agency signs with a drawn
signature.

## Clauses

The clause library of this document is in `es-arras-clauses.md`: every clause with its ID, its flag
(verbatim, optional with its condition, variant for a region), its variables, the Spanish master
text and the English text. Open it when drafting; copy by ID, never compose.

## Own rules
- Do not touch the deposit clause (ARR-04 and its variants) outside its fields.
- Do not add "a cuenta del precio" to stipulation 2.a): the crediting against the price is
  already at the end of stipulation 3.
- Do not mix penalties or liquidated damages into the arras. If the user wants confirmatorias or
  penales, say that this is a penitenciales document and that the other kinds need their own
  drafting. Do not improvise.
- Exactly one of ARR-06 / ARR-07, and exactly one of ARR-12 / ARR-13.
- Check the arithmetic yourself: balance = price minus deposit, and the percentage agrees.
  Write it in the chat. If there was a reservation, today's arras include it: say so in
  recibi_frase.
- A nota simple older than a month deserves a warning.
- When the seller is not resident in Spain, ARR-12 (the buyer's 3 % withholding) is never
  removed.
- No cash. The translated column is not a sworn translation; if the buyer wants one, it can be
  ordered separately and is not required.
- Title "Contrato de arras penitenciales", the same name in the footer.

## Draft title and invitation
Draft title: "Arras {{inmueble_corto}}". Invitation to the buyer (at most 500 characters, in
their language or in Spanish; invitation e-mails exist only in Spanish, English and Swedish):
"Contrato de arras de {{inmueble_corto}}. Revise el precio, las arras, la fecha de escritura y
la estipulación 3 antes de firmar."

## Conflicts noted (not resolved)
- The model's §4.2 names a NOEXCLUSIVA variant for 04_arras; the clause file has only CC, CCCat
  and FN. Written to the clause file.
- The guide's field table has no buyer rows for box A, although buyers are asked for and sign;
  their field names are therefore not listed here.
- The guide mentions `poderes_frase` and an optional `poderes`; neither appears in the clause
  file's variables or in the guide's field table. Not listed.
- Intake: the guide asks eleven questions, one per message; OURS caps intake at four choices in
  one message. Written to OURS.
- The guide points to `references/regions.md` and `references/controls.json`; here the regional
  table is `es-regions.md` and there is no controls file.
- Days of notice (7) is a guide default; OURS gives none.
