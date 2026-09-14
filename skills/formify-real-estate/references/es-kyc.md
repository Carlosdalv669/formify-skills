# Formulario de identificación (KYC) de comprador y vendedor

## Purpose and default profile
Once per person per transaction, before the reserva or the arras. The agency is a regulated
entity and must identify both sides. Two forms with the same identity box, one per person:
each co-owner, each buyer. Default profile: official.

## Boxes
A. Identidad. B. Actividad y operación (seller: Propiedad y operación). C. Persona con
responsabilidad pública. Then optional Representante and Persona jurídica blocks, the
declarations, and the client's signature. On a separate page, D. Comprobación y valoración por
la agencia, which the agency completes by hand after signing: plain boxes and rules, not PDF
fields. The risk assessment and sanctions check live in the agency's file, never in the form
the client signs.

### Box A is scanned, not typed
Build this part exactly.

| Element | Field name | Size | Notes |
|---|---|---|---|
| Scan control, right-hand side | `documento_scan\|tink-scan-id[1]` | 180 × 120 pt | The only required field in the form. Becomes the scan button, then the image of the document front. |
| Ten MRZ values, left-hand side | `tink-scanned-id-mrz-*[1]` | 135 pt each | Given name, surname, date and place of birth, nationality, document number, issuing country, issue date, expiry date, personal number. Formify fills them when the scan completes. |
| Three short values under the image | NIF/NIE, phone, email | 180 pt each | Label above, value or field below. |
| Reverse-side upload | `documento_reverso_subir\|tink-upload-attachment[1]` | 75 × 22 pt | With the instruction to photograph the back. Accepts photographs. |
| Name of the uploaded file | `documento_reverso_nombre\|tink-uploaded-attachmentname[1]` | - | Read-only. Formify writes the file name here. |

Only the scan control is marked required: Formify reads that from the PDF and shows it in
red, so the form cannot be signed without scanning. The ten MRZ fields are not required,
because the scan fills them and the client does not. Never ask for these details in the chat
and never print them. The client scans; the data arrive verified.

## What to ask
Buyer: name and e-mail for the invitation, and if they have them, NIF/NIE or foreign tax
number, address, tax residence, phone; nothing more about identity. Then occupation, purpose of
the purchase, source of funds, expected bank financing. Whether they act for themselves; if for
someone else, the representative block; if a company, the legal-entity block with directors and
beneficial owners at 25 %. PEP: yes or no, and if yes the office, country and dates.

Seller: the same, plus marital status and property regime, spouse where relevant, registry data
of the property, how and when they acquired it and at what price, share of ownership, date of
the nota simple, and the account the price is to be paid into.

Whatever the user lacks becomes a field the client fills at signing.

## Fields
The five scan elements are fixed in the template; see the Box A table above.

| name | printed or field | size | required | who | tink |
|---|---|---|---|---|---|
| nif, telefono, email | printed or field, under the image | 180 pt | yes | client | - |
| domicilio, residencia_fiscal | printed or field | 300 pt | yes | client | - |
| profesion, finalidad, origen_fondos, financiacion, nombre_propio | printed or field, box B | 300 pt | yes (buyer) | client | - |
| estado_civil, conyuge, inmueble_registral, titulo_adquisicion, porcentaje_titularidad, fecha_nota_simple, iban_destino | printed or field, box B | 300 pt | yes (seller) | client | - |
| pep_no_marca, pep_si_marca, pep_detalle | printed, box C | - | yes | user | - |
| rep_* | printed, only with a representative | - | no | user | - |
| pj_* | printed, only for a legal entity; one beneficial owner per line | - | no | user | - |
| referencia, lugar, fecha_larga, inmueble_corto, agencia_*, agente_nombre, agencia_email_datos | printed | - | yes | agency | - |
Keep these widths: a wider field covers the neighbouring cell.

## Signers and order
Comprador/a (Buyer) or Vendedor/a (Seller): the client only, plus Representante
(Representative) if any. No ID scan on the signature: the document is already scanned inside
the form, so a second scan at signing is pure friction. The agent does not sign. No signing
order.

## Clauses
### KYC-B-01 · Persona con responsabilidad pública (pregunta)
- applies: verbatim
- variables: none
- es: ¿Desempeña o ha desempeñado en los últimos doce meses usted, un familiar suyo o una persona allegada un cargo público importante (jefe de Estado o de Gobierno, ministro, parlamentario, magistrado de tribunal supremo o constitucional, embajador, alto mando militar, directivo de empresa pública, dirigente de partido u organización internacional)?
- en: Do you, a family member or a close associate hold, or have you held in the last twelve months, a prominent public function (head of State or government, minister, member of parliament, supreme or constitutional court judge, ambassador, high-ranking officer, director of a State-owned enterprise, party leader or official of an international organisation)?

### KYC-B-02 · Declaración del comprador
- applies: verbatim
- variables: none
- es: El firmante declara que los datos de los cuadros anteriores son ciertos y completos, que el documento de identidad aportado está en vigor, que los fondos destinados a la compra tienen origen lícito y que comunicará a la agencia cualquier cambio en estos datos mientras dure la operación.
- en: The signatory declares that the details in the boxes above are true and complete, that the identity document provided is valid, that the funds intended for the purchase are of lawful origin and that he or she will inform the agency of any change in these details for the duration of the transaction.

### KYC-B-03 · Protección de datos
- applies: verbatim
- variables: {{agencia_nombre}}, {{agencia_email_datos}}
- es: La agencia, {{agencia_nombre}}, es responsable del tratamiento de estos datos. Los trata para cumplir las obligaciones de identificación y diligencia debida que le impone la Ley 10/2010, de 28 de abril, de prevención del blanqueo de capitales y de la financiación del terrorismo, y los conserva durante diez años desde el fin de la relación, sin usarlos para otros fines. Puede comunicarlos a las autoridades competentes cuando la ley lo exija. La copia del documento de identidad se almacena en soporte electrónico que garantiza su integridad. El firmante puede ejercer sus derechos de acceso, rectificación y los demás previstos en la normativa de protección de datos en {{agencia_email_datos}}, sin que ello afecte a las obligaciones legales de conservación.
- en: The agency, {{agencia_nombre}}, is the controller of these data. It processes them to comply with the identification and due diligence obligations imposed by Spanish Law 10/2010 of 28 April on the prevention of money laundering and terrorist financing, and keeps them for ten years after the end of the relationship, without using them for any other purpose. It may disclose them to the competent authorities where the law so requires. The copy of the identity document is stored electronically in a manner that ensures its integrity. The signatory may exercise the rights of access, rectification and the other rights provided for by data protection law at {{agencia_email_datos}}, without prejudice to the statutory retention obligations.

### KYC-V-01 · Persona con responsabilidad pública (pregunta)
- applies: verbatim
- variables: none
- es: ¿Desempeña o ha desempeñado en los últimos doce meses usted, un familiar suyo o una persona allegada un cargo público importante (jefe de Estado o de Gobierno, ministro, parlamentario, magistrado de tribunal supremo o constitucional, embajador, alto mando militar, directivo de empresa pública, dirigente de partido u organización internacional)?
- en: Do you, a family member or a close associate hold, or have you held in the last twelve months, a prominent public function (head of State or government, minister, member of parliament, supreme or constitutional court judge, ambassador, high-ranking officer, director of a State-owned enterprise, party leader or official of an international organisation)?

### KYC-V-02 · Declaración del vendedor
- applies: verbatim
- variables: none
- es: El firmante declara que los datos de los cuadros anteriores son ciertos y completos, que el documento de identidad aportado está en vigor, que es titular del inmueble en los términos indicados y que comunicará a la agencia cualquier cambio en estos datos mientras dure la operación.
- en: The signatory declares that the details in the boxes above are true and complete, that the identity document provided is valid, that he or she owns the property as stated and will inform the agency of any change in these details for the duration of the transaction.

### KYC-V-03 · Protección de datos
- applies: verbatim
- variables: {{agencia_nombre}}, {{agencia_email_datos}}
- es: La agencia, {{agencia_nombre}}, es responsable del tratamiento de estos datos. Los trata para cumplir las obligaciones de identificación y diligencia debida que le impone la Ley 10/2010, de 28 de abril, de prevención del blanqueo de capitales y de la financiación del terrorismo, y los conserva durante diez años desde el fin de la relación, sin usarlos para otros fines. Puede comunicarlos a las autoridades competentes cuando la ley lo exija. La copia del documento de identidad se almacena en soporte electrónico que garantiza su integridad. El firmante puede ejercer sus derechos de acceso, rectificación y los demás previstos en la normativa de protección de datos en {{agencia_email_datos}}, sin que ello afecte a las obligaciones legales de conservación.
- en: The agency, {{agencia_nombre}}, is the controller of these data. It processes them to comply with the identification and due diligence obligations imposed by Spanish Law 10/2010 of 28 April on the prevention of money laundering and terrorist financing, and keeps them for ten years after the end of the relationship, without using them for any other purpose. It may disclose them to the competent authorities where the law so requires. The copy of the identity document is stored electronically in a manner that ensures its integrity. The signatory may exercise the rights of access, rectification and the other rights provided for by data protection law at {{agencia_email_datos}}, without prejudice to the statutory retention obligations.

## Own rules
Never keep anything from this form in anything that persists between conversations. If the
seller's destination account is not in the seller's name, say so in the chat: it is a risk
indicator. If the source of funds is cash, crypto or an unidentified third party, say so too,
and that the agency should obtain evidence before continuing. Retention is ten years; remind
the user not to delete the signed form earlier. The Ley 10/2010 citation in KYC-B-03 and
KYC-V-03 is a permitted exception to the no-law rule: keep it. A PEP answer of yes changes
nothing in the form; the agency records its measures in its own file.

## Draft title and invitation
Draft title: "Identificación comprador {{nombre_completo}}" or "Identificación vendedor
{{nombre_completo}}". Invitation (at most 500 characters, in the client's language), which must
warn them to have their document to hand: "Formulario de identificación que la ley obliga a la
agencia a recoger antes de la operación de {{inmueble_corto}}. Tenga a mano su documento de
identidad: se fotografía al firmar."

## Conflicts noted (not resolved)
- The guide's field table lists nombre_completo, fecha_nacimiento, nacionalidades and
  documento_* as required variables; OURS says box A is scanned and these values are never
  asked or printed. OURS followed.
- The guide adds a 2027 EU note (five-year retention); OURS says ten years. OURS followed.
