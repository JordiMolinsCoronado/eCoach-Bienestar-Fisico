# Jordi Agent â€” Hoja de ruta actualizada

## Principio central

Jordi Agent no es un chatbot general.

Es un asistente local-first, orientado a tareas concretas, que funciona por Telegram y ayuda a construir un proceso patrimonial claro, auditable y prudente.

Postura por defecto:

```text
Local primero.
Prompts en Markdown.
Datos vivos en Markdown.
Logs auditables.
Sin magia oculta.
Sin recomendaciones no controladas.
El cliente decide.
La IA prepara.
La IA registra.
```

Para el primer caso profesional, Jordi Agent serÃ¡ un **copiloto patrimonial independiente para clientes espaÃ±oles**.

Regla esencial:

```text
El asistente no recomienda inversiones.
No vende productos.
No decide por el cliente.
Ayuda a entender opciones, riesgos, costes, criterios y preguntas.
El cliente o un asesor humano decide.
```

La direcciÃ³n actual del producto ha cambiado respecto al primer prototipo:

```text
Antes:
un menÃº de pequeÃ±as herramientas financieras.

Ahora:
un sistema socrÃ¡tico de clarificaciÃ³n patrimonial.

El cliente escribe libremente.
El sistema interpreta.
Un orquestador fuerte hace la primera versiÃ³n completa del trabajo.
Las skills existen primero como mÃ³dulos de criterio, plantillas y checklists internos, no necesariamente como llamadas separadas.
Los archivos Markdown se actualizan.
El orquestador responde.
Los botones muestran resÃºmenes, no capturan inputs.
```

---

# Estado actual del proyecto

Hasta ahora se han construido varias piezas Ãºtiles, aunque algunas quedan como prototipo o andamio tÃ©cnico.

## v0 â€” Bot de eco en Telegram

**Objetivo:** demostrar que el bot de Telegram estÃ¡ vivo.

Funcionalidades:

```text
/start
Respuesta bÃ¡sica
```

**Estado:** hecho.

---

## v1 â€” Captura de mensajes en Markdown

**Objetivo:** convertir Telegram en una herramienta rÃ¡pida de captura.

Funcionalidad:

```text
Cualquier mensaje normal â†’ SecondBrain_inbox.md
```

**Estado:** hecho como prototipo personal.

**Nota de producto:** esta funciÃ³n ya no pertenece al producto patrimonial principal. Puede conservarse en otro bot personal, pero no debe estar visible en el bot Wealth.

---

## v2 â€” Comando `/inbox`

**Objetivo:** ver capturas recientes.

**Estado:** hecho como prototipo personal.

**Nota de producto:** no se mantiene en la interfaz Wealth.

---

## v3 â€” Comando `/today`

**Objetivo:** ver capturas de hoy.

**Estado:** hecho como prototipo personal.

**Nota de producto:** no se mantiene en la interfaz Wealth.

---

## v4 â€” LLM local con Ollama

**Objetivo:** conectar Jordi Agent a un modelo local.

Modelo local probado:

```text
gemma4:e4b-it-q4_K_M
```

**Estado:** hecho.

**Aprendizaje:** Ãºtil para comprobar la arquitectura local-first, pero demasiado dÃ©bil para respuestas patrimoniales fiables con prompts largos y conocimiento inyectado.

---

## v5 â€” Primer menÃº de botones

**Objetivo:** reducir fricciÃ³n usando botones de Telegram.

Primeros botones:

```text
ðŸ§  Ask
ðŸ“¥ Inbox
ðŸ“… Today
âœï¸ Capture
```

**Estado:** hecho como prototipo.

**Nota de producto:** sustituido por una interfaz patrimonial mucho mÃ¡s simple.

---

## v6 â€” Botones con estado conversacional

**Objetivo:** hacer que botones como Ask y Capture esperen el siguiente mensaje.

**Estado:** hecho como prototipo.

---

# Fase 1 â€” Asistente controlado por prompts

## v7 â€” Archivos Markdown de prompts

**Objetivo:** dejar de hardcodear instrucciones dentro del Python.

Carpeta creada:

```text
/prompts/
```

Archivos iniciales:

```text
base_rules.md
wealth_policy.md
client_profile_questions.md
```

**Para quÃ© sirve:** permite cambiar el comportamiento del asistente editando Markdown, sin tocar Python.

**Estado:** hecho.

---

## v8 â€” Cargador de prompts en Python

**Objetivo:** aÃ±adir funciones reutilizables para cargar prompts y llamar al LLM.

Funciones:

```text
load_prompt()
local_llm()
```

**Estado:** hecho.

---

## v9 â€” Primer botÃ³n Wealth

**Objetivo:** aÃ±adir un modo financiero explÃ­cito.

BotÃ³n:

```text
ðŸ’¼ Wealth
```

**Estado:** hecho como prototipo.

**Nota de producto:** sustituido por la lÃ³gica futura de entrada libre + orquestador.

---

## v10 â€” Estado conversacional Wealth

**Objetivo:** permitir que el bot espere un caso financiero y responda con anÃ¡lisis estructurado.

**Estado:** hecho como prototipo.

---

## v11 â€” Logs de Wealth

**Objetivo:** guardar cada anÃ¡lisis en Markdown para trazabilidad.

Archivo:

```text
Wealth_Logs.md
```

**Estado:** hecho.

**Para quÃ© sirve:** permite auditar quÃ© se preguntÃ³, quÃ© modelo respondiÃ³ y quÃ© anÃ¡lisis produjo la IA.

---

# Fase 2 â€” Primer asistente patrimonial Ãºtil

Estas versiones crearon herramientas separadas. Fueron Ãºtiles para aprender, pero no son la forma final de producto.

## v12 â€” Client profiling assistant

**Objetivo original:** generar preguntas de perfil del cliente.

**Estado:** hecho.

**Aprendizaje:** Ãºtil como skill interna, pero no debe ser un botÃ³n separado. El cliente no debe tener que decidir si algo pertenece a â€œperfilâ€; el sistema debe extraerlo automÃ¡ticamente.

---

## v13 â€” Platform/options assistant

**Objetivo original:** comparar categorÃ­as de bancos, custodios, plataformas, roboadvisors, etc.

**Estado:** hecho.

**Aprendizaje:** debe convertirse en una skill tÃ©cnica interna, no en botÃ³n visible.

---

## v14 â€” Basic portfolio parser

**Objetivo original:** analizar una cartera pegada en texto.

**Estado:** hecho.

**Aprendizaje:** Ãºtil internamente para leer posiciones o documentos, pero el objetivo final no es â€œhacer portfolio analysisâ€; el objetivo es extraer hechos para ayudar al cliente a decidir mejor.

---

## v15 â€” Suitability checklist generator

**Objetivo original:** generar checklist pre-asesoramiento.

**Estado:** hecho.

**Aprendizaje:** Ãºtil como skill interna de preguntas y datos faltantes.

---

## v16 â€” Investment memo generator

**Objetivo original:** redactar memorandos no finales de inversiÃ³n.

**Estado:** hecho.

**Aprendizaje:** demasiado tÃ©cnico como botÃ³n. Puede reaparecer mÃ¡s adelante como salida interna o profesional, no como funciÃ³n principal para el cliente.

---

# Fase 3 â€” Conocimiento local y grounding documental

## v17 â€” Carpeta Wealth_Knowledge

**Objetivo:** permitir que Jordi Agent use documentos propios de marco patrimonial.

Carpeta:

```text
/Wealth_Knowledge/
```

Archivos creados:

```text
investment_policy.md
mifid_checklist.md
client_meeting_template.md
platform_due_diligence_template.md
product_due_diligence_template.md
portfolio_review_template.md
```

**Estado:** hecho.

**Para quÃ© sirve:** proporciona el marco conceptual: riesgos, criterios, due diligence, costes, liquidez, fiscalidad, custodia y preguntas de cliente.

---

## v18 â€” RAG local simple sobre Markdown

**Objetivo:** leer archivos Markdown locales y aÃ±adirlos al contexto del modelo.

Primera versiÃ³n:

```text
Leer todos los .md de Wealth_Knowledge/
Inyectarlos en el prompt
Responder
```

**Estado:** hecho mecÃ¡nicamente.

**Aprendizaje:** funciona tÃ©cnicamente, pero puede generar â€œsopa de plantillasâ€ con modelos pequeÃ±os. MÃ¡s adelante conviene usar selecciÃ³n de archivos o RAG mÃ¡s inteligente.

---

## v19 â€” RAG local mejorado

**Objetivo original:** mejorar recuperaciÃ³n de conocimiento.

Opciones futuras:

```text
selecciÃ³n de archivos por skill
bÃºsqueda por palabras clave
SQLite FTS
FAISS
Chroma
LanceDB
```

**Estado:** aparcado.

**Criterio:** no hacerlo todavÃ­a hasta que el producto estÃ© claro. Primero necesitamos arquitectura de flujo y skills.

---

# Fase 4 â€” Archivos y documentos

## v20 â€” CSV portfolio import

**Estado:** aparcado.

**Motivo:** demasiado especÃ­fico para la fase actual. No es el nÃºcleo del producto.

---

## v21 â€” Excel portfolio import

**Estado:** aparcado.

**Motivo:** demasiado especÃ­fico para la fase actual.

---

## v22 â€” Lectura de PDFs / posiciones actuales

**Objetivo actualizado:** leer documentos del cliente, especialmente posiciones actuales, propuestas bancarias, fichas de producto o informes, pero no para producir â€œportfolio analysisâ€ como fin principal.

Nuevo propÃ³sito:

```text
Documento del cliente
â†’ extraer hechos relevantes
â†’ actualizar archivos vivos
â†’ identificar preguntas
â†’ ayudar al cliente a comparar opciones
```

**Estado:** futuro.

**Para quÃ© sirve:** convierte documentos en informaciÃ³n estructurada para el proceso de decisiÃ³n.

---

## v23 â€” Due diligence de producto como skill

**Objetivo actualizado:** no crear un botÃ³n de â€œProduct Reviewâ€, sino una skill interna capaz de leer un producto/propuesta y extraer:

```text
quÃ© es
quÃ© exposiciÃ³n da
quÃ© cuesta
quÃ© riesgos contiene
quÃ© liquidez tiene
quÃ© preguntas hay que hacer
quÃ© informaciÃ³n falta
```

**Estado:** futuro.

**Regla:** no recomienda el producto; solo ayuda a evaluarlo.

---

# Fase 5 â€” LLM externo y calidad de respuesta

## v24 â€” Conector Gemini API

**Objetivo:** usar un modelo externo mÃ¡s fuerte cuando haga falta mayor calidad.

Modelo inicial probado:

```text
gemini-2.5-flash-lite
```

Comando de prueba:

```text
/geminiask
```

**Estado:** hecho.

**Aprendizaje:** Gemini funciona, muestra tokens y coste estimado. Las respuestas son mejores que Gemma local.

---

## v24b â€” Gemini como cerebro principal temporal

**Objetivo:** sustituir el uso normal de Gemma local por Gemini, mientras se conserva el enfoque local-first como ideal de arquitectura.

**Estado:** hecho parcialmente en el prototipo Wealth.

**Nota:** para la versiÃ³n cliente se usarÃ¡ Gemini como orquestador principal, con aviso de confidencialidad antes de enviar texto sensible.

---

# Nueva Fase 6 â€” RediseÃ±o del producto: entrada libre + archivos vivos

Esta es la nueva direcciÃ³n central.

## v25 â€” Interfaz limpia de tres botones de salida

**Objetivo:** eliminar botones tÃ©cnicos y dejar solo tres resÃºmenes visibles.

Botones:

```text
ðŸ‘¤ Resumen de quiÃ©n soy yo
ðŸŽ¯ Resumen de quÃ© quiero
ðŸ§­ Resumen de quÃ© tengo que hacer
```

**Principio:** los botones no son para clasificar el input. Son para ver outputs.

El cliente no debe elegir si su texto es â€œperfilâ€, â€œobjetivoâ€ o â€œacciÃ³nâ€. El cliente escribe libremente. El sistema separa.

**Estado:** prÃ³ximo paso.

---

## v26 â€” Archivos vivos del cliente

**Objetivo:** crear una estructura Markdown que actÃºe como memoria editable del proceso.

Carpeta:

```text
ClientData/
```

Archivos:

```text
quien_soy.md
que_quiero.md
que_tengo_que_hacer.md
estilo_respuesta.md
configuracion_privacidad.md
historial_interacciones.md
privacidad_log.md
```

### `quien_soy.md`

**Para quÃ© sirve:** resume quiÃ©n es el cliente: situaciÃ³n personal, fiscal, profesional, patrimonial, experiencia inversora, relaciÃ³n con el riesgo, restricciones y miedos.

No decide por el cliente. Es un espejo editable.

### `que_quiero.md`

**Para quÃ© sirve:** resume lo que el cliente quiere conseguir: ingresos, jubilaciÃ³n, seguridad, crecimiento, liquidez, independencia del banco, simplicidad, fiscalidad, legado, etc.

Ayuda a separar deseos reales de productos concretos.

### `que_tengo_que_hacer.md`

**Para quÃ© sirve:** convierte el proceso en pasos claros: informaciÃ³n pendiente, documentos a pedir, preguntas al banco, comparaciones que hacer, riesgos a entender, prÃ³xima acciÃ³n.

Es el mapa de avance.

### `estilo_respuesta.md`

**Para quÃ© sirve:** define cÃ³mo debe escribir el orquestador para ese cliente: tono, nivel tÃ©cnico, idioma, grado de detalle, necesidad de calma, estructura preferida.

Esto es importante porque la respuesta patrimonial no solo debe ser correcta; debe ser legible y Ãºtil para esa persona.

### `configuracion_privacidad.md`

**Para quÃ© sirve:** guarda la polÃ­tica privada de confidencialidad del cliente.

Incluye, como mÃ­nimo:

```text
umbral_revision_manual = 6
```

Si el riesgo de confidencialidad estimado es igual o inferior a este umbral, el sistema puede continuar automÃ¡ticamente.

Si el riesgo estimado es superior a este umbral, el sistema debe detenerse y preguntar al cliente si quiere enviar el texto tal como estÃ¡ o reducir el riesgo antes de continuar.

Esto evita convertir la privacidad en fricciÃ³n constante. El cliente conserva control, pero no tiene que confirmar cada mensaje de bajo o medio riesgo.

### `historial_interacciones.md`

**Para quÃ© sirve:** guarda un registro resumido de lo que el cliente ha ido diciendo y cÃ³mo ha evolucionado el proceso.

### `privacidad_log.md`

**Para quÃ© sirve:** registra decisiones de confidencialidad: quÃ© se enviÃ³, si se redujo el riesgo, quÃ© nivel de riesgo se estimÃ³ y cuÃ¡ndo.

**Estado:** futuro inmediato.

---

## v27 â€” Entrada libre del cliente

**Objetivo:** cualquier mensaje normal de Telegram se considera potencialmente relevante.

Flujo:

```text
Cliente escribe libremente
â†’ sistema guarda mensaje temporal
â†’ evalÃºa riesgo de confidencialidad
â†’ lee el umbral privado del cliente
â†’ si el riesgo estÃ¡ por debajo o igual al umbral, procesa automÃ¡ticamente
â†’ si el riesgo supera el umbral, muestra riesgo 0â€“10 y ofrece enviar o reducir riesgo
```

**Principio:** el cliente habla como una persona. El sistema estructura.

**Estado:** futuro inmediato.

---

## v28 â€” Evaluador de confidencialidad 0â€“10

**Objetivo:** antes de enviar un texto a una LLM externa, mostrar al usuario un indicador claro del riesgo de confidencialidad.

Escala:

```text
0 = sin riesgo apreciable
10 = riesgo alto: datos personales, financieros o identificativos sensibles
```

Formato sugerido:

```text
Riesgo de confidencialidad: 7/10
â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘

Este texto contiene datos financieros personales concretos.
Puedes enviarlo tal como estÃ¡ o reducir el riesgo antes de enviarlo a una LLM externa.
```

Comportamiento tras evaluar:

```text
Si riesgo <= umbral privado del cliente:
    procesar automÃ¡ticamente

Si riesgo > umbral privado del cliente:
    mostrar botones contextuales:
    - Enviar la pregunta
    - Reducir riesgo de confidencialidad
```

**Para quÃ© sirve:** hace visible la privacidad, evita envÃ­os inconscientes y crea confianza sin interrumpir innecesariamente el flujo del cliente.

**Estado:** futuro inmediato.

---

## v28b â€” Umbral privado de confidencialidad por cliente

**Objetivo:** permitir que cada cliente defina cuÃ¡nta fricciÃ³n quiere antes de enviar texto a una LLM externa.

Archivo:

```text
ClientData/Cliente1/configuracion_privacidad.md
```

Contenido inicial sugerido:

```markdown
# ConfiguraciÃ³n de privacidad

## Umbral de revisiÃ³n manual

6

## Significado

Si el riesgo de confidencialidad estimado es igual o inferior a este nÃºmero, el sistema puede procesar automÃ¡ticamente el texto.

Si el riesgo es superior a este nÃºmero, el sistema debe detenerse y preguntar al cliente si quiere enviar el texto tal como estÃ¡ o reducir el riesgo antes de continuar.

Escala:
- 0 = sin riesgo apreciable.
- 10 = riesgo alto: datos personales, financieros o identificativos sensibles.
```

Regla operativa:

```text
riesgo = estimar_confidencialidad(mensaje)
umbral = leer_umbral_privacidad(cliente)

if riesgo <= umbral:
    continuar automÃ¡ticamente
else:
    mostrar decisiÃ³n al cliente
```

Valor inicial recomendado:

```text
6
```

**Para quÃ© sirve:** convierte la privacidad en una preferencia configurable. El sistema es prudente cuando el texto es sensible, pero no molesta al cliente cuando el riesgo estÃ¡ dentro del nivel que Ã©l ha aceptado.

**Estado:** futuro inmediato.

---

## v29 â€” ReducciÃ³n de riesgo de confidencialidad

**Objetivo:** transformar el texto del cliente en una versiÃ³n menos identificable.

Ejemplo:

Texto original:

```text
Tengo 800.000 â‚¬, vendÃ­ parte de mi empresa en Barcelona y quiero jubilarme en 7 aÃ±os.
```

VersiÃ³n reducida:

```text
El cliente tiene un relaciones lÃ­quido significativo tras una operaciÃ³n empresarial. Quiere preparar ingresos de jubilaciÃ³n a medio plazo y tiene poca experiencia inversora.
```

El sistema vuelve a mostrar riesgo:

```text
Riesgo de confidencialidad: 3/10
â–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘
```

**Estado:** futuro inmediato.

---

# Nueva Fase 7 â€” Orquestador monolÃ­tico primero

La arquitectura inicial no debe multiplicar llamadas innecesariamente.

En la primera versiÃ³n Ãºtil, el sistema usarÃ¡ una sola llamada fuerte a Gemini para procesar el mensaje del cliente, actualizar los archivos vivos y generar la respuesta final.

Las â€œskillsâ€ existen desde el principio, pero no como agentes separados ni como llamadas independientes por defecto. Existen como mÃ³dulos de criterio, plantillas, instrucciones y checklists que el orquestador puede usar dentro de una sola llamada.

Principio:

```text
Primero, orquestador monolÃ­tico.
DespuÃ©s, skills separadas solo cuando exista un dolor real.
```

Esto evita duplicar tareas, reduce latencia, reduce coste y simplifica la depuraciÃ³n.

Las skills siguen siendo importantes, pero al principio son â€œcapacidades internasâ€ del orquestador, no necesariamente procesos separados.

## v30 â€” MÃ³dulo interno: actualizar â€œquiÃ©n soy yoâ€

**Objetivo:** dar al orquestador criterios claros para extraer del mensaje libre todo lo que pertenece al perfil del cliente y actualizar `quien_soy.md`.

Uso inicial:

```text
Se incorpora al prompt del orquestador como instrucciones de extracciÃ³n y actualizaciÃ³n.
No requiere una llamada separada al modelo en la primera versiÃ³n.
```

Salida esperada dentro de la respuesta estructurada del orquestador:

```markdown
ActualizaciÃ³n propuesta o contenido completo actualizado para quien_soy.md
```

Ejemplos de informaciÃ³n:

```text
edad
residencia fiscal
situaciÃ³n familiar
origen del relaciones
experiencia inversora
miedos
restricciones
relaciÃ³n con el riesgo
```

**Estado:** futuro.

---

## v31 â€” MÃ³dulo interno: actualizar â€œquÃ© quieroâ€

**Objetivo:** dar al orquestador criterios para extraer deseos, objetivos y prioridades, y actualizar `que_quiero.md`.

Ejemplos:

```text
preparar jubilaciÃ³n
generar ingresos
proteger capital
evitar productos complejos
mantener liquidez
comparar opciones independientes
no depender ciegamente del banco
```

Archivo:

```text
que_quiero.md
```

**Estado:** futuro.

---

## v32 â€” MÃ³dulo interno: actualizar â€œquÃ© tengo que hacerâ€

**Objetivo:** dar al orquestador criterios para convertir lo aprendido en acciones, documentos pendientes, preguntas y decisiones por preparar.

Ejemplos:

```text
definir ingreso anual necesario
pedir desglose completo de comisiones
comparar custodios
revisar fiscalidad
pedir KID/ficha del producto
separar liquidez inmediata de capital invertible
```

Archivo:

```text
que_tengo_que_hacer.md
```

**Estado:** futuro.

---

## v33 â€” MÃ³dulo interno: actualizar estilo de respuesta

**Objetivo:** permitir que el orquestador detecte preferencias de tono, detalle y formato, y actualice `estilo_respuesta.md` cuando el cliente lo revele.

Ejemplos:

```text
quiere lenguaje sencillo
prefiere tablas
se agobia con jerga
quiere respuestas cortas
quiere razonamiento detallado
necesita tono calmado
prefiere castellano
```

Archivo:

```text
estilo_respuesta.md
```

**Estado:** futuro.

---

# Nueva Fase 8 â€” MÃ³dulos tÃ©cnicos patrimoniales

Estos mÃ³dulos son esenciales para responder bien, pero no tienen que ser llamadas separadas desde el principio.

En la primera versiÃ³n, serÃ¡n archivos Markdown, bloques de prompt o secciones de conocimiento que el orquestador usa cuando el mensaje del cliente lo requiera.

MÃ¡s adelante, si alguna tarea necesita mÃ¡s precisiÃ³n, actualizaciÃ³n externa, bÃºsqueda web o lectura documental, podrÃ¡ convertirse en una skill separada con su propia llamada y su propio log.

## v34 â€” MÃ³dulo tÃ©cnico: custodios y plataformas

**Objetivo:** aportar al orquestador criterios para ayudar a comparar dÃ³nde puede mantenerse o invertirse el dinero.

Opciones a comparar:

```text
banco tradicional
banca privada
broker online
plataforma de fondos
roboadvisor
asesor financiero independiente + RTO/custodia separada
fondos monetarios
letras del Tesoro
depÃ³sitos
```

Criterios:

```text
coste total
custodia
conflictos de interÃ©s
reporting fiscal espaÃ±ol
acceso a clases limpias
facilidad operativa
calidad de atenciÃ³n
seguridad jurÃ­dica
capacidad de transferir activos
```

**Regla:** no dice quÃ© plataforma usar. Ayuda a comparar.

**Estado:** futuro.

---

## v35 â€” MÃ³dulo tÃ©cnico: estrategias patrimoniales generales

**Objetivo:** aportar al orquestador rutas generales a comparar, dado quiÃ©n es el cliente y quÃ© quiere.

Ejemplos de rutas:

```text
mantener liquidez en depÃ³sitos/letras/fondos monetarios
roboadvisor indexado
plataforma de fondos indexados
asesor financiero independiente
banca privada
modelo hÃ­brido
gestiÃ³n delegada
gestiÃ³n propia con apoyo puntual
```

**Regla:** no elige una ruta. Explica ventajas, riesgos, costes, preguntas y condiciones bajo las cuales cada ruta puede tener sentido.

**Estado:** futuro.

---

## v36 â€” MÃ³dulo tÃ©cnico: preguntas para banco o asesor

**Objetivo:** aportar al orquestador preguntas concretas que el cliente debe hacer antes de aceptar una propuesta.

Ejemplos:

```text
Â¿CuÃ¡l es el coste total anual?
Â¿Hay retrocesiones?
Â¿Existe clase limpia?
Â¿QuiÃ©n custodia los activos?
Â¿Puedo transferir la posiciÃ³n sin vender?
Â¿QuÃ© pasa si quiero salir?
Â¿QuÃ© reporting fiscal recibirÃ© en EspaÃ±a?
Â¿QuÃ© parte del coste paga al asesor o banco?
```

**Estado:** futuro.

---

## v37 â€” Skill futura separada: lectura de documentos / posiciÃ³n actual

**Objetivo:** leer PDFs, extractos, propuestas bancarias, fichas de producto o posiciones actuales.

Flujo:

```text
documento
â†’ extraer hechos
â†’ actualizar archivos vivos
â†’ generar preguntas
â†’ alimentar al orquestador
```

**Regla:** la lectura documental no es para â€œdar una recomendaciÃ³n de carteraâ€, sino para entender la realidad del cliente y las opciones sobre la mesa.

**Estado:** futuro.

---

# Nueva Fase 9 â€” Orquestador

## v38 â€” Orquestador principal con Gemini fuerte

**Objetivo:** coordinar todo el sistema.

El orquestador recibe:

```text
mensaje actual del cliente
quien_soy.md
que_quiero.md
que_tengo_que_hacer.md
estilo_respuesta.md
configuracion_privacidad.md
Wealth_Knowledge/*.md
mÃ³dulos internos relevantes
nivel de confidencialidad
```

En la primera versiÃ³n, el orquestador hace todo en una sola llamada:

```text
1. interpreta el mensaje libre;
2. separa informaciÃ³n de perfil, objetivos y acciones;
3. actualiza los tres archivos vivos;
4. usa los mÃ³dulos tÃ©cnicos relevantes;
5. genera la respuesta final;
6. propone la siguiente acciÃ³n;
7. deja informaciÃ³n para el log.
```

Y produce:

```text
quien_soy.md actualizado
que_quiero.md actualizado
que_tengo_que_hacer.md actualizado
respuesta final al cliente
prÃ³xima acciÃ³n
registro de auditorÃ­a
```

**Modelo sugerido:** usar el mejor Gemini disponible y razonable en coste para esta parte, porque requiere integraciÃ³n fina, estilo, prudencia y seguimiento de instrucciones.

**Reglas:**

```text
no recomendar productos
no vender
no decidir
no crear urgencia
no hacer market timing
comparar opciones
formular criterios
hacer preguntas
explicar riesgos y costes
ayudar al cliente a decidir por sÃ­ mismo
```

**Estado:** futuro.

---

## v38b â€” SeparaciÃ³n progresiva de skills solo cuando haga falta

**Objetivo:** evitar sobreingenierÃ­a prematura.

Regla:

```text
No crear una llamada separada para una skill hasta que exista un problema claro que lo justifique.
```

Ejemplos de cuÃ¡ndo separar una skill:

```text
- el orquestador mezcla mal quiÃ©n soy / quÃ© quiero / quÃ© hacer;
- el cÃ¡lculo de privacidad necesita ser mÃ¡s fiable;
- la lectura de PDFs requiere extracciÃ³n especÃ­fica;
- la comparaciÃ³n de custodios necesita datos actualizados;
- una tarea necesita bÃºsqueda web o una fuente externa;
- una parte debe auditarse de forma independiente.
```

Mientras no exista ese dolor, la skill seguirÃ¡ como mÃ³dulo interno dentro del prompt o del conocimiento local.

**Para quÃ© sirve:** mantiene el sistema simple, barato y rÃ¡pido, sin perder la posibilidad de crecer hacia una arquitectura modular.

**Estado:** futuro.

---

## v39 â€” Respuesta final en tono adaptado

**Objetivo:** que cada respuesta use el estilo adecuado para el cliente.

Fuente:

```text
estilo_respuesta.md
```

La respuesta debe poder ser:

```text
mÃ¡s simple o mÃ¡s tÃ©cnica
mÃ¡s breve o mÃ¡s extensa
mÃ¡s calmada o mÃ¡s directa
mÃ¡s narrativa o mÃ¡s tabular
```

**Estado:** futuro.

---

## v40 â€” Logs auditables del proceso completo

**Objetivo:** guardar quÃ© pasÃ³ en cada interacciÃ³n.

Archivo:

```text
logs/interacciones.md
```

Cada entrada deberÃ­a incluir:

```markdown
## Fecha/hora

### Mensaje original

### Riesgo de confidencialidad

### Texto enviado al modelo
Original / reducido

### Modelo usado

### Skills ejecutadas

### Archivos actualizados

### Respuesta final

---
```

**Estado:** futuro.

---

# Nueva Fase 10 â€” Producto completo

## v41 â€” Flujo completo de clarificaciÃ³n patrimonial

**Objetivo:** unir todas las piezas en un producto coherente.

Flujo completo:

```text
1. El cliente escribe libremente.
2. El sistema estima riesgo de confidencialidad.
3. El sistema lee el umbral privado de confidencialidad del cliente.
4. Si el riesgo estÃ¡ dentro del umbral, procesa automÃ¡ticamente.
5. Si el riesgo supera el umbral, el cliente elige enviar o reducir riesgo.
6. El orquestador monolÃ­tico procesa el mensaje completo.
7. El orquestador separa informaciÃ³n de perfil, objetivos y acciones.
8. El orquestador usa mÃ³dulos tÃ©cnicos cuando el tema lo requiera.
9. Los archivos vivos se actualizan.
10. El orquestador responde en el tono adecuado.
11. Los tres botones permiten ver:
   - quiÃ©n soy
   - quÃ© quiero
   - quÃ© tengo que hacer
12. Todo queda registrado.
```

**Resultado esperado:**

```text
El cliente no recibe una recomendaciÃ³n.
Recibe claridad.
Recibe preguntas mejores.
Recibe criterios de comparaciÃ³n.
Recibe un mapa editable de sÃ­ mismo, de sus objetivos y de sus prÃ³ximos pasos.
```

**Estado:** objetivo principal actual.

---

# Interfaz final deseada

## Botones visibles

```text
ðŸ‘¤ Resumen de quiÃ©n soy yo
ðŸŽ¯ Resumen de quÃ© quiero
ðŸ§­ Resumen de quÃ© tengo que hacer
```

## Botones contextuales tras un mensaje libre

Solo aparecen cuando el riesgo de confidencialidad supera el umbral privado del cliente.

```text
Enviar la pregunta
Reducir riesgo de confidencialidad
```

## No mostrar como botones

Estas funciones deben existir como mÃ³dulos internos o skills futuras, no como interfaz:

```text
Client Profile
Platform Options
Portfolio Parser
Suitability Checklist
Investment Memo
Inbox
Today
Capture
```

---

# Principio final del producto

```text
No es un asesor que decide.
No es un banco que vende.
No es una plantilla de informes.

Es un espejo patrimonial socrÃ¡tico:
ordena quiÃ©n eres,
clarifica quÃ© quieres,
muestra quÃ© tienes que hacer,
y te ayuda a comparar opciones sin quitarte la decisiÃ³n.
```

---

# DecisiÃ³n arquitectÃ³nica actual

La arquitectura inmediata serÃ¡:

```text
Entrada libre
â†’ evaluaciÃ³n de confidencialidad
â†’ umbral privado del cliente
â†’ una llamada fuerte al orquestador Gemini
â†’ actualizaciÃ³n de archivos vivos
â†’ respuesta final
â†’ log
```

Las skills no desaparecen. Cambian de forma:

```text
Ahora:
skills como instrucciones, mÃ³dulos Markdown y criterios internos del orquestador.

MÃ¡s adelante:
skills como llamadas separadas solo cuando aporten precisiÃ³n, auditorÃ­a o datos externos.
```

Esta decisiÃ³n evita duplicar tareas y permite construir rÃ¡pido sin perder la estructura conceptual del producto.


