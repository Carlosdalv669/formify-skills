# Documento de entrega de llaves

## Purpose and default profile
A receipt for the keys the owner hands to the agency for viewings. Small, fast, the one most often done from a phone. Default profile light. With the agency's details already known it must be finished in five questions or fewer. It presupposes a mediation contract: encargo comes before llaves.

## Boxes
A. Lugar y fecha (place and date; the closing refers to it). B. Parte propietaria (one owner, or two with the propietario_2 block). C. Agencia (the agency that keeps the keys, with its own NIF, never a parent franchise). D. Inmueble. E. Llaves (the inventory). Labels bilingual; then the conditions in two columns, which speak only of la parte propietaria, la agencia and the boxes. A value appears once, in its box.

## What to ask
Only what memory and the conversation do not hold, one per message, in this order:
1. Owner(s): you have their details (name, document, address), or they fill them in at signing. Several owners: all sign.
2. Property: full address. Registry data or cadastral reference only if to hand.
3. Sale or letting, and the date of the mediation contract. No mandate yet: offer to produce the nota de encargo first. If the user insists, the date is "este mismo día" and the chat says so.
4. Inventory: how many keys of each kind, remotes, anything else.
5. Viewing log: default yes for a letting, no for a sale.
6. The client's language, when not already known.
Never asked: alarm codes, entryphone codes, passwords. Never asked: the agent's own document.

## Fields
| name | printed or field | size | required | who | tink |
|---|---|---|---|---|---|
| agencia_nombre, agencia_nif, agencia_direccion, agencia_email_datos | printed from memory | - | yes | agency | - |
| agencia_registro_linea / agencia_registro_frase | printed only if the agency is registered, else empty | - | no | agency | - |
| logo_html | printed or empty | - | no | agency | - |
| referencia | agency format or LLA-{{año}}-{{n}} | - | yes | agency | - |
| lugar, fecha_larga | printed, date in words ("5 de septiembre de 2026") | - | yes | agency | - |
| propietario_1_nombre, propietario_1_doc, propietario_1_domicilio | printed or field; doc is type and number ("NIE X1234567L") | - | yes | owner | - |
| propietario_2_* | with the propietario_2 block | - | no | second owner | - |
| agente_nombre | printed from memory; never the agent's document | - | yes | agency | - |
| inmueble_direccion, inmueble_corto | printed; corto like "el piso de Calle Mayor 12, 3.º B" | - | yes | user | - |
| inmueble_datos_registrales_frase | printed or empty | - | no | user | - |
| operacion / operacion_tr | venta / sale, arrendamiento / letting | - | yes | user | - |
| fecha_encargo | date of the mediation contract | - | yes | user | - |
| n_llaves_vivienda, n_llaves_portal, n_llaves_garaje, n_llaves_buzon, n_mandos, otros_llaves (+ _tr) | printed; "0" or "ninguna" when none | - | yes | user | - |
| visitas_aviso_frase / _tr | printed only if the owner wants prior notice, else empty | - | no | user | - |
| n_datos, n_idioma | 9 and 10 with LLA-09, 8 and 9 without | - | yes | - | - |
| idioma_cliente_es / _tr | "inglés" / "English" and so on | - | yes | user | - |
No source gives widths or tink attributes. Owner fields left for signing are passed as {"field", "width"}.

## Signers and order
Propietario/a / Owner: each owner. Agente inmobiliario / Real estate agent: the agent. Drawn signature (digital_ink), no ID scan, no signing order.

## Clauses
### LLA-01 · Apertura
- applies: verbatim
- variables: none
- es: La parte propietaria identificada en el cuadro B, titular del inmueble del cuadro D, entrega en este acto a la agencia del cuadro C las llaves relacionadas en el cuadro E, con sujeción a las siguientes condiciones. Ambas partes se reconocen capacidad legal suficiente para otorgar el presente documento.
- en: The owner identified in box B, holder of title to the property in box D, hereby hands over to the agency in box C the keys listed in box E, subject to the following terms. Both parties acknowledge that they have sufficient legal capacity to execute this document.

### LLA-02 · Objeto
- applies: verbatim
- variables: none
- es: 1. Objeto. La agencia recibe las llaves con el único fin de mostrar el inmueble a personas interesadas en la operación encargada. Cualquier otro uso requiere el consentimiento previo y por escrito de la parte propietaria.
- en: 1. Purpose. The agency receives the keys for the sole purpose of showing the property to persons interested in the transaction entrusted. Any other use requires the owner's prior written consent.

### LLA-03 · Inventario
- applies: verbatim
- variables: none
- es: 2. Inventario. Las llaves y dispositivos entregados son los que constan en el cuadro E. La parte propietaria declara que no entrega ningún otro.
- en: 2. Inventory. The keys and devices handed over are those recorded in box E. The owner declares that no others are handed over.

### LLA-04 · Custodia
- applies: verbatim
- variables: none
- es: 3. Custodia. La agencia custodiará las llaves con la diligencia de un profesional, en lugar cerrado y sin identificación de la dirección del inmueble. Queda prohibido hacer copias de las llaves por cualquier motivo y cederlas a terceros, salvo a personal de la agencia para las visitas.
- en: 3. Safekeeping. The agency shall keep the keys with professional diligence, in a locked place and without any label identifying the property's address. Copying the keys for any reason, or passing them to third parties, is prohibited, except to agency staff for viewings.

### LLA-05 · Visitas
- applies: verbatim
- variables: {{visitas_aviso_frase}}, {{visitas_aviso_frase_tr}}
- es: 4. Visitas. Las visitas se realizarán siempre acompañadas por personal de la agencia{{visitas_aviso_frase}}. Al terminar cada visita, la agencia dejará cerradas todas las puertas y ventanas, desconectados los aparatos que hubiera encendido y el inmueble en el mismo estado en que lo encontró.
- en: 4. Viewings. Viewings shall always be accompanied by agency staff{{visitas_aviso_frase_tr}}. At the end of each viewing the agency shall leave all doors and windows closed, switch off any appliances it turned on and leave the property in the same condition in which it found it.

### LLA-06 · Alarma y accesos
- applies: verbatim
- variables: none
- es: 5. Alarma y accesos. Los códigos de alarma, claves de acceso y contraseñas no constan en este documento y se comunican por separado. La agencia los tratará como información confidencial y no los anotará junto a las llaves.
- en: 5. Alarm and access codes. Alarm codes, access codes and passwords are not recorded in this document and are communicated separately. The agency shall treat them as confidential and shall not keep them together with the keys.

### LLA-07 · Devolución
- applies: verbatim
- variables: none
- es: 6. Devolución. La agencia devolverá las llaves a la parte propietaria, contra recibo, en el plazo máximo de dos días hábiles desde que se produzca cualquiera de estos hechos: la formalización de la operación encargada, la extinción del contrato de mediación, o el requerimiento de la parte propietaria por cualquier medio que deje constancia.
- en: 6. Return. The agency shall return the keys to the owner, against receipt, within two working days of any of the following: completion of the transaction entrusted, termination of the brokerage agreement, or a request by the owner made by any means that leaves a record.

### LLA-08 · Pérdida o extravío
- applies: verbatim
- variables: none
- es: 7. Pérdida o extravío. Si las llaves se perdieran o fueran sustraídas mientras están en poder de la agencia, esta lo comunicará a la parte propietaria sin demora y asumirá el coste de sustitución de los bombines afectados y de las nuevas llaves.
- en: 7. Loss or theft. If the keys are lost or stolen while in the agency's possession, the agency shall inform the owner without delay and shall bear the cost of replacing the affected lock cylinders and the new keys.

### LLA-09 · Registro de visitas
- applies: optional: a viewing log is wanted (default yes for a letting, no for a sale); when dropped, renumber {{n_datos}} and {{n_idioma}} to 8 and 9
- variables: none
- es: 8. Registro de visitas. La agencia llevará un registro con fecha y hora de cada visita y lo facilitará a la parte propietaria cuando lo solicite.
- en: 8. Viewing log. The agency shall keep a log with the date and time of each viewing and shall provide it to the owner on request.

### LLA-10 · Datos personales
- applies: verbatim
- variables: {{n_datos}}, {{agencia_email_datos}}
- es: {{n_datos}}. Datos personales. Los datos de las partes se tratan por la agencia para cumplir este documento y el contrato de mediación, y se conservan mientras duren esas relaciones y los plazos legales posteriores. Las partes pueden ejercer sus derechos de acceso, rectificación, supresión y demás previstos en la normativa de protección de datos dirigiéndose a {{agencia_email_datos}}.
- en: {{n_datos}}. Personal data. The parties' data are processed by the agency to perform this document and the brokerage agreement, and are kept for as long as those relationships last and for the statutory periods thereafter. The parties may exercise their rights of access, rectification, erasure and the other rights provided for in data protection law by writing to {{agencia_email_datos}}.

### LLA-11 · Idioma
- applies: verbatim
- variables: {{n_idioma}}, {{idioma_cliente_es}}, {{idioma_cliente_tr}}
- es: {{n_idioma}}. Idioma. El presente documento se firma en español y en {{idioma_cliente_es}}. En caso de discrepancia entre ambas versiones prevalecerá la versión española.
- en: {{n_idioma}}. Language. This document is signed in Spanish and in {{idioma_cliente_tr}}. In the event of any discrepancy between the two versions, the Spanish version shall prevail.

### LLA-12 · Cierre
- applies: verbatim
- variables: none
- es: Y en prueba de conformidad, las partes firman electrónicamente el presente documento en el lugar y la fecha del cuadro A.
- en: In witness whereof, the parties sign this document electronically at the place and on the date stated in box A.

## Own rules
- Never write an alarm code, an entryphone code or a password, even when dictated; remind the user they are communicated separately (LLA-06).
- Three or more owners: all sign. No signing for another owner without a power of attorney; ask for it and add "en nombre y representación de" in the parties block.
- Letting with a tenant already in the property: add ", y previo consentimiento de la persona ocupante" to LLA-05 in both columns. Ask first.
- No mediation contract: propose the nota de encargo first.
- Prior-notice wording, when wanted, is the {{visitas_aviso_frase}} text from the guide: ", previo aviso a la parte propietaria con al menos {{horas}} horas de antelación" / ", with at least {{horas}} hours' prior notice to the owner".
- Registered agency line: "<br>Registro {{nombre_registro}} n.º {{numero}}" and ", inscrita en el {{nombre_registro}} con el n.º {{numero}}" / ", registered in the {{nombre_registro}} under no. {{numero}}"; empty otherwise.
- A photo of the key set as an annex is out of this version; the inventory in LLA-03 is the proof of what was handed over.

## Draft title and invitation
Title: "Entrega de llaves {{inmueble_corto}}". Invitation (500 characters max, in the client's language or Spanish): "Recibo de las llaves de {{inmueble_corto}} entregadas a {{agencia_nombre}} para las visitas. Firma en un minuto desde el móvil."

## Conflicts noted (not resolved)
- OURS caps this document at five questions; OURS and the guide both list six asks (language included). Kept as six, language only when unknown.
- The guide's "user may insist, date is este mismo día" fallback and the field table come from the guide only; OURS is silent on both.
