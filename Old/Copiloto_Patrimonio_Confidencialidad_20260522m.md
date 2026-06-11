# Copiloto Relaciones â€” Independencia y confidencialidad

Fecha: 2026-05-22

## 1. Idea central

Copiloto Relaciones no debe ser â€œotro bot financieroâ€.

Debe ser una herramienta para pensar sobre decisiones importantes con mÃ¡s privacidad, mÃ¡s independencia y mÃ¡s control.

La idea simple es:

> Google es para comodidad.  
> Copiloto Relaciones es para consecuencias.

Google y otras grandes plataformas pueden ser muy Ãºtiles para tareas normales: resumir correos, buscar informaciÃ³n, organizar documentos, planificar viajes o automatizar trabajo.

Pero cuando la pregunta toca relaciones, jubilaciÃ³n, venta de una empresa, herencia, familia, dependencia econÃ³mica, decisiones mÃ©dicas o temas muy personales, la necesidad cambia.

La persona ya no solo pregunta:

> Â¿Puedes ayudarme rÃ¡pido?

TambiÃ©n pregunta:

> Â¿QuiÃ©n ve esto?  
> Â¿QuiÃ©n gana si tomo una decisiÃ³n u otra?  
> Â¿Me estÃ¡n empujando hacia un producto?  
> Â¿Esto queda guardado en algÃºn sitio?  
> Â¿Puedo confiar en los incentivos del sistema?

AhÃ­ aparece el espacio natural de Copiloto Relaciones.


## 2. DecisiÃ³n prÃ¡ctica: Telegram valida utilidad; PWA valida confianza

Esta decisiÃ³n debe estar muy al principio del documento porque afecta a la estrategia inmediata.

Hay dos caminos de producto, con promesas distintas.

### Piloto rÃ¡pido con Telegram

Telegram permite avanzar rÃ¡pido porque ya ofrece:

```text
- interfaz de chat;
- envÃ­o y recepciÃ³n de mensajes;
- experiencia conocida por el usuario;
- menos trabajo de frontend;
- integraciÃ³n sencilla con un backend y una IA externa.
```

Pero tiene una limitaciÃ³n importante:

> En Telegram, el texto original del usuario llega a Telegram y al servidor de Prevengen.

Por tanto, en el piloto de Telegram, la promesa honesta debe ser:

> Prevengen recibe tu texto original para procesarlo. No vendemos tus datos, no entrenamos modelos con tus conversaciones privadas, restringimos el acceso humano y reducimos la informaciÃ³n sensible antes de enviarla a una IA externa.

Telegram sirve para validar utilidad:

```text
- Â¿El producto responde bien?
- Â¿El usuario encuentra valor?
- Â¿QuÃ© preguntas hace realmente?
- Â¿QuÃ© skills hacen falta?
- Â¿QuÃ© verticales aparecen primero?
- Â¿QuÃ© partes del flujo generan confianza o fricciÃ³n?
```

Pero algunos beta testers pueden escribir menos o evitar detalles sensibles si saben que Prevengen puede ver el texto original.

Eso no es un fallo moral del piloto. Es una limitaciÃ³n estructural del canal.

### PWA privada como producto verdadero

La PWA privada es mÃ¡s trabajo que Telegram, pero no necesariamente muchÃ­simo mÃ¡s si la primera versiÃ³n es mÃ­nima.

La diferencia es:

```text
Telegram MVP:
rÃ¡pido porque Telegram ya da la interfaz.

PWA privada:
mÃ¡s trabajo porque Prevengen debe construir la interfaz, el login, el estado local, la vista previa, el vault y el envÃ­o.
```

Pero la PWA permite la promesa fuerte:

> El usuario ve y aprueba lo que sale de su dispositivo antes de enviarlo.

Y, en modo privado:

> Prevengen recibe solo la versiÃ³n reducida aprobada, no el texto sensible original.

La PWA sirve para validar confianza:

```text
- Â¿El usuario valora ver quÃ© se envÃ­a?
- Â¿El usuario entiende el vault local?
- Â¿El usuario se siente mÃ¡s seguro escribiendo datos sensibles?
- Â¿La tokenizaciÃ³n local aumenta el uso?
- Â¿La privacidad visible es una ventaja comercial real?
```

La frase interna:

> **Telegram valida la utilidad. La PWA valida la confianza.**

Y la confianza es el alma de Prevengen.

### EstimaciÃ³n realista de dificultad

Una estimaciÃ³n razonable:

```text
Telegram MVP funcional:
3â€“10 dÃ­as, si el backend y la llamada a LLM ya existen.

PWA mÃ­nima sin vault fuerte:
2â€“4 semanas.

PWA mÃ­nima con privacy preview + token vault bÃ¡sico:
4â€“8 semanas.

PWA mÃ¡s sÃ³lida, auditable, con cifrado local, sync, logs y buen UX:
2â€“4 meses.
```

Depende mucho de la persona que programe, pero el punto importante es:

> Una PWA mÃ­nima no es una app nativa compleja. Es una web privada con chat, privacidad local y vista previa.

### QuÃ© deberÃ­a incluir la primera PWA mÃ­nima

No debe intentar resolverlo todo.

Debe incluir solo lo esencial:

```text
1. Login.
2. Pantalla tipo chat.
3. DetecciÃ³n local de importes y entidades.
4. Token vault local bÃ¡sico.
5. Vista previa:
   - esto se queda en tu dispositivo;
   - esto se enviarÃ¡.
6. BotÃ³n enviar.
7. Prevengen recibe solo texto reducido.
8. Respuesta del LLM.
9. Propuesta de memoria:
   guardar / editar / ignorar.
10. Registro bÃ¡sico de privacidad.
```

Ejemplo:

```text
Texto original:
Tengo 800.000 euros en Caixabank. Â¿CÃ³mo invierto?

Vault local:
BANCO_CLIENTE_1 = Caixabank
PATRIMONIO_CLIENTE_1 = 800.000 euros

Texto enviable:
El usuario tiene un relaciones financiero alto en una entidad financiera. Â¿CÃ³mo deberÃ­a pensar sobre la inversiÃ³n?
```

Esto ya demuestra la tesis fuerte.

### Partes fÃ¡ciles

Son relativamente manejables:

```text
- interfaz bÃ¡sica de chat;
- login;
- envÃ­o de texto reducido al backend;
- respuesta del modelo;
- detecciÃ³n local de importes;
- detecciÃ³n local de bancos conocidos;
- sustituciÃ³n por tokens;
- vista previa de salida.
```

### Partes mÃ¡s difÃ­ciles

Son mÃ¡s delicadas:

```text
- cifrado local bien hecho;
- recuperaciÃ³n si el usuario pierde el dispositivo;
- uso en varios dispositivos;
- sincronizaciÃ³n del vault cifrado;
- evitar que logs o crash reports filtren datos;
- gestiÃ³n segura de sesiones;
- preview del paquete completo: pregunta + wiki + contexto;
- ediciÃ³n cÃ³moda de tokens;
- control de versiones de la wiki;
- auditorÃ­a u open source de la capa de privacidad.
```

No son ciencia ficciÃ³n, pero no deben meterse todas en el primer sprint.

### RecomendaciÃ³n estratÃ©gica

No abandonar Telegram todavÃ­a.

Usarlo como laboratorio rÃ¡pido.

Pero empezar la PWA privada cuanto antes como producto verdadero.

Orden recomendado:

```text
1. Mantener Telegram para beta rÃ¡pida.
2. Empezar PWA privada mÃ­nima.
3. No esperar a una app nativa.
4. No intentar LLM local al inicio.
5. Crear primero un vault determinista simple.
6. Validar si el usuario valora ver y aprobar quÃ© sale del dispositivo.
```

La frase clave:

> **No necesitamos una app nativa para empezar. Necesitamos una sala privada verificable.**

Y la decisiÃ³n prÃ¡ctica:

> Telegram es el prototipo de utilidad. La PWA es el prototipo de confianza.


## 3. Principio clave: confidencialidad Ãºtil, no anonimizaciÃ³n mÃ¡xima

Esta idea es muy importante.

Copiloto Relaciones no debe anonimizar todo lo que parezca ligeramente sensible.

La regla correcta no es:

> Ocultar todo lo sospechoso.

La regla correcta es:

> Exponer solo lo necesario para obtener una buena respuesta.

O, de forma mÃ¡s simple:

> La confidencialidad no consiste en ocultarlo todo. Consiste en ocultar lo que no hace falta para responder bien.

Si se anonimiza demasiado, la respuesta se vuelve genÃ©rica y pierde utilidad.

Si se anonimiza demasiado poco, la confidencialidad se debilita.

Por tanto, el producto debe gestionar una tensiÃ³n:

```text
utilidad de la respuesta
vs
riesgo de exposiciÃ³n
```

La meta es:

> MÃ¡xima utilidad con mÃ­nima exposiciÃ³n necesaria.

### Ejemplo: 800.000 euros en Caixabank

Pregunta original del usuario:

```text
Tengo 800.000 euros en Caixabank. Â¿CÃ³mo invierto?
```

Una anonimizaciÃ³n demasiado agresiva serÃ­a:

```text
Tengo CLIENT_WEALTH_1 en CLIENT_BANK_1. Â¿CÃ³mo invierto?
```

O:

```text
Tengo un importe alto en una entidad financiera. Â¿CÃ³mo invierto?
```

Esto protege mÃ¡s, pero puede perder informaciÃ³n Ãºtil.

En muchos casos, `Caixabank` sÃ­ puede ser relevante:

```text
- comisiones;
- fondos propios;
- conflictos de interÃ©s;
- asesoramiento bancario;
- productos estructurados;
- depÃ³sitos;
- gestiÃ³n discrecional;
- custodia;
- contexto de banca minorista espaÃ±ola.
```

En cambio, el importe exacto `800.000 euros` probablemente no siempre es necesario.

Puede bastar con:

```text
relaciones financiero alto
```

O:

```text
importe alto de seis cifras
```

O, si la respuesta necesita mÃ¡s precisiÃ³n:

```text
entre 500.000 y 1.000.000 de euros
```

Una buena versiÃ³n enviable podrÃ­a ser:

```text
Tengo un relaciones financiero alto en Caixabank.
Â¿CÃ³mo deberÃ­a analizar mis opciones de inversiÃ³n?
```

O, si se quiere proteger mÃ¡s:

```text
Tengo un relaciones financiero alto en una gran entidad bancaria espaÃ±ola.
Â¿CÃ³mo deberÃ­a analizar mis opciones de inversiÃ³n?
```

La decisiÃ³n depende del nivel de privacidad elegido por el cliente y de la utilidad esperada.

### La identidad debe ocultarse casi siempre

Hay datos que casi nunca son necesarios para una buena respuesta:

```text
- nombre real;
- email;
- telÃ©fono;
- DNI/NIF;
- direcciÃ³n exacta;
- identificadores de cuenta;
- nombres de familiares si no son necesarios.
```

Estos deben ocultarse por defecto.

En cambio, otros datos pueden ser Ãºtiles para la respuesta:

```text
- paÃ­s fiscal;
- tipo de banco;
- nombre del banco si afecta a productos o comisiones;
- rango patrimonial;
- horizonte temporal;
- edad aproximada;
- tolerancia al riesgo;
- situaciÃ³n familiar general;
- objetivo financiero.
```

La privacidad debe ser selectiva.

### Privacidad por categorÃ­as

La PWA deberÃ­a clasificar cada elemento sensible por tipo y decidir una acciÃ³n por defecto.

Ejemplo:

| Elemento | Tipo | AcciÃ³n por defecto | Motivo |
|---|---|---|---|
| Jordi Molins | Identidad | Ocultar | No es necesario |
| 800.000 euros | Relaciones exacto | Convertir a rango | El exacto rara vez es imprescindible |
| Caixabank | Entidad financiera | Mantener si es relevante | Puede afectar comisiones/productos/conflictos |
| Barcelona | Ciudad | Generalizar | Normalmente basta paÃ­s/regiÃ³n |
| JubilaciÃ³n en 7 aÃ±os | Horizonte temporal | Mantener | Es muy relevante |
| Marc | Nombre familiar | Tokenizar/ocultar | La identidad concreta rara vez es necesaria |

### Perfiles de privacidad

No todos los clientes querrÃ¡n lo mismo.

Por eso el producto puede ofrecer perfiles:

```text
Modo equilibrado:
- oculta identidad;
- convierte importes exactos en rangos;
- mantiene entidades relevantes si ayudan a responder;
- generaliza ciudad salvo que sea necesaria.

Modo estricto:
- oculta tambiÃ©n bancos, ciudades, empresas y nombres de terceros;
- usa mÃ¡s abstracciones;
- reduce mÃ¡s la especificidad.

Modo personalizado:
- el cliente decide categorÃ­a por categorÃ­a:
  â€œoculta siempre mi bancoâ€,
  â€œconvierte siempre importes en rangosâ€,
  â€œmantÃ©n siempre el paÃ­s fiscalâ€,
  â€œno incluyas familia salvo aprobaciÃ³n explÃ­citaâ€.
```

Para la mayorÃ­a de usuarios, el modo equilibrado serÃ¡ mejor, porque protege lo esencial sin destruir la utilidad.

Para una minorÃ­a de usuarios muy sensibles, el modo estricto serÃ¡ necesario.

### Ejemplo de vista previa

```text
Texto original:
Tengo 800.000 euros en Caixabank. Â¿CÃ³mo invierto?

VersiÃ³n sugerida:
Tengo un relaciones financiero alto en Caixabank.
Â¿CÃ³mo deberÃ­a analizar mis opciones de inversiÃ³n?

Cambios de privacidad:
- Identidad personal: no incluida.
- Importe exacto: 800.000 euros â†’ relaciones financiero alto.
- Entidad financiera: Caixabank se mantiene porque puede ser relevante para comisiones, productos y conflictos de interÃ©s.

Riesgo antes de reducir: 7/10
Riesgo despuÃ©s de reducir: 3/10

[Enviar]
[Ocultar tambiÃ©n Caixabank]
[Editar]
[Cancelar]
```

Si el usuario elige ocultar tambiÃ©n Caixabank:

```text
Tengo un relaciones financiero alto en una gran entidad bancaria espaÃ±ola.
Â¿CÃ³mo deberÃ­a analizar mis opciones de inversiÃ³n?
```

### Principio de producto

La frase estratÃ©gica:

> Prevengen no maximiza la anonimizaciÃ³n. Maximiza la confidencialidad Ãºtil.

O:

> Suficiente verdad para responder bien. Suficiente reducciÃ³n para proteger al usuario.

El producto debe ser discerniente, no paranoico.


## 4. Moat inicial: minimizaciÃ³n visible + juicio de dominio

Prevengen no debe venderse como una promesa de secreto perfecto.

La ventaja inicial no es:

> Nadie puede copiar esta idea.

La ventaja inicial es mÃ¡s realista:

> Prevengen combina privacidad visible, memoria controlada y juicio especÃ­fico por dominio.

La frase central:

> **Prevengen no compite por tener el modelo mÃ¡s inteligente. Compite por ser la sala mÃ¡s segura para usar los modelos mÃ¡s inteligentes.**

El edge se puede formular asÃ­:

> **Prevengenâ€™s edge is not perfect secrecy. Prevengenâ€™s edge is visible minimization + domain judgment.**

En espaÃ±ol:

> **La ventaja de Prevengen no es la confidencialidad perfecta. Es la minimizaciÃ³n visible + el juicio de dominio.**

### 4.1. MinimizaciÃ³n visible

El usuario no solo recibe una promesa legal de privacidad.

Ve el proceso.

Ve:

```text
- quÃ© escribiÃ³ originalmente;
- quÃ© se queda en su dispositivo;
- quÃ© se transforma;
- quÃ© se enviarÃ¡ a Prevengen;
- quÃ© recibirÃ¡ la IA externa;
- quÃ© no se enviarÃ¡.
```

Esto no es privacidad mÃ¡gica ni perfecta.

Es una mejora material y visible frente a preguntar directamente a una IA generalista desde una cuenta personal.

La promesa correcta no debe ser:

> Confidencialidad 100% perfecta.

La promesa correcta debe ser:

> Confidencialidad materialmente mejor que preguntar directamente a una IA generalista, y ademÃ¡s visible para el usuario.

Ese â€œvisibleâ€ es esencial.

El cliente no solo confÃ­a en Prevengen.

Puede ver la versiÃ³n protegida antes de enviarla.

### 4.2. Juicio especÃ­fico por dominio

El modelo externo aporta inteligencia general.

Prevengen aporta mÃ©todo.

Para cada vertical, Prevengen aÃ±ade:

```text
- skills;
- estructura de respuesta;
- checklists;
- lÃ­mites;
- preguntas relevantes;
- criterios de comparaciÃ³n;
- reglas de seguridad;
- protocolos de decisiÃ³n.
```

En relaciones, eso puede incluir:

```text
- anÃ¡lisis de propuestas bancarias;
- detecciÃ³n de conflictos de interÃ©s;
- comparaciÃ³n banco vs asesor independiente;
- preguntas para asesores regulados;
- advertencias fiscales y legales;
- estructura para decidir sin vender productos.
```

En relaciones, salud, familia o trabajo, las skills serÃ¡n distintas.

La arquitectura de privacidad puede ser comÃºn.

El juicio no debe ser genÃ©rico.

La fÃ³rmula estratÃ©gica:

```text
Prevengen Core = workflow de confidencialidad
Copilotos verticales = secret sauce / skills / juicio de dominio
LLM externo = motor de inteligencia reemplazable
```

### 4.3. Memoria Ãºtil, pero no imprudente

Prevengen no debe competir diciendo:

> Recordamos todo sobre ti.

Eso puede sonar Ãºtil, pero tambiÃ©n peligroso.

La promesa debe ser distinta:

> Recordamos lo suficiente para ayudarte, exponiendo lo mÃ­nimo posible.

La memoria debe ser:

```text
- visible;
- editable;
- tokenizada cuando haga falta;
- aprobada por el usuario;
- no silenciosa;
- controlada por perfiles de privacidad.
```

La frase:

> **No â€œrecordar todoâ€. Recordar bien, con control.**

### 4.4. Por quÃ© esto puede crear un moat

El moat no es enorme al principio.

No es un moat tÃ©cnico imposible de copiar.

Pero sÃ­ puede ser un moat de confianza, workflow y dominio.

La combinaciÃ³n es difÃ­cil de ejecutar bien:

```text
privacy UX
+ local token vault
+ lenguaje de confianza
+ memoria visible
+ skills especÃ­ficas por dominio
+ orquestaciÃ³n cuidadosa del LLM externo
+ posicionamiento independiente
```

Big Tech tiene los modelos, pero su tendencia natural es saber mÃ¡s del usuario y mantener la relaciÃ³n directa con Ã©l.

Los bancos tienen relaciÃ³n con el cliente, pero suelen tener conflictos de producto.

Las apps de memoria tienen recall, pero no necesariamente minimizaciÃ³n.

Las apps de privacidad tienen privacidad, pero no necesariamente skills verticales de decisiÃ³n.

Prevengen puede ocupar el espacio intermedio:

> Ayudar al usuario a pensar sobre cosas importantes exponiendo menos de lo que el modelo querrÃ­a y menos de lo que el mercado suele tomar.

### 4.5. Frase de posicionamiento

La frase fuerte:

> **No competimos por tener el modelo mÃ¡s inteligente. Competimos por ser la sala mÃ¡s segura para usar los modelos mÃ¡s inteligentes.**

Otra versiÃ³n:

> **Prevengen convierte modelos externos potentes en copilotos privados, estructurados y orientados a decisiones importantes.**

Y la intuiciÃ³n comercial:

> Si el usuario siente â€œpuedo contarle esto a Prevengen, pero no se lo preguntarÃ­a directamente a ChatGPT, Gemini o Claudeâ€, entonces hay una ventaja real.

Esa ventaja puede empezar pequeÃ±a, pero puede acumularse con confianza, memoria y dominio.

## 5. Idea clave para clientes: Prevengen separa a la persona del modelo

**Esta idea debe estar en el centro del mensaje comercial:**

> Cuando preguntas directamente a una IA generalista desde tu cuenta personal, la plataforma puede asociar esa pregunta con tu cuenta, tu sesiÃ³n, tu dispositivo, tu IP y tu historial de uso.
>
> Cuando preguntas a travÃ©s de Prevengen, la IA externa ve a Prevengen como solicitante, no al cliente final.
>
> Y si Prevengen anonimiza y reduce la pregunta antes de enviarla, la IA externa recibe un caso patrimonial abstracto, no una persona identificable.

Dicho de forma simple:

> **Prevengen se coloca entre la persona y el modelo.**
>
> **Quitamos identidad antes de aplicar inteligencia.**

Esto no significa que todo sea anÃ³nimo automÃ¡ticamente.

Si el usuario escribe datos muy concretos, como su nombre, ciudad, banco o importe exacto, esos datos pueden identificarlo.

Por eso Copiloto Relaciones debe hacer tres cosas antes de usar una IA externa:

```text
1. Detectar datos sensibles.
2. Reducir o anonimizar la pregunta.
3. Enviar solo lo necesario para obtener una buena respuesta.
```

Ejemplo de pregunta de alto riesgo:

```text
Soy Jordi Molins, vivo en Barcelona, tengo 800.000 euros en Caixabank,
vendÃ­ mi empresa y quiero jubilarme en 7 aÃ±os.
```

VersiÃ³n reducida:

```text
El usuario tiene un relaciones financiero alto en una entidad espaÃ±ola,
ha tenido un evento de liquidez empresarial y quiere valorar su jubilaciÃ³n
en un horizonte de medio plazo.
```

La diferencia es esencial.

En el primer caso, la IA recibe una persona.

En el segundo caso, la IA recibe un caso.

Esta es una de las grandes promesas de Copiloto Relaciones:

> **No enviamos tu vida privada a una IA externa si podemos enviar una versiÃ³n suficiente, reducida y menos identificable de tu caso.**

La frase estratÃ©gica:

> **Nosotros somos la capa de confidencialidad entre tÃº y la IA.**

O, mÃ¡s simple:

> **La IA ayuda a pensar. Prevengen ayuda a proteger lo que la IA no necesita saber.**

## 6. DistinciÃ³n esencial: proteger del modelo externo vs proteger tambiÃ©n de Prevengen

Esta distinciÃ³n es muy importante.

No todos los modos de uso ofrecen el mismo nivel de confidencialidad.

### Modo Telegram

En un bot normal de Telegram, el flujo es:

```text
Usuario escribe en Telegram
â†’ Telegram recibe el mensaje
â†’ Telegram lo envÃ­a al servidor de Prevengen
â†’ Prevengen calcula el riesgo de confidencialidad
â†’ Prevengen reduce o anonimiza si hace falta
â†’ Prevengen envÃ­a solo la versiÃ³n reducida a la IA externa
```

Por tanto, en el modo Telegram:

> Prevengen protege al usuario antes de que la IA externa vea el contenido.

Pero hay que ser honestos:

> En modo Telegram, Prevengen recibe el texto original y puede tÃ©cnicamente verlo.

La promesa correcta no es:

> Prevengen no puede leer tu mensaje.

La promesa correcta es:

> Prevengen no vende tus datos, no entrena modelos con tus conversaciones privadas, restringe y registra el acceso humano, y evita enviar informaciÃ³n sensible a una IA externa sin reducciÃ³n y aprobaciÃ³n.

Esto ya es Ãºtil, porque protege al cliente frente a la exposiciÃ³n directa ante modelos externos.

Pero no es el nivel mÃ¡ximo de privacidad.

### Modo Privado Web/App

En una app propia o en una web privada, el flujo puede ser distinto:

```text
Usuario escribe en la app/web de Prevengen
â†’ el navegador o app calcula localmente el riesgo de confidencialidad
â†’ el navegador o app detecta datos sensibles
â†’ el navegador o app anonimiza o reduce el texto
â†’ el usuario ve quÃ© se va a enviar
â†’ solo la versiÃ³n aprobada sale del dispositivo
â†’ Prevengen recibe la misma versiÃ³n anonimizada que recibirÃ¡ la IA externa
```

En este modo:

> Prevengen protege al usuario antes de que Prevengen vea el contenido sensible.

Esta es una diferencia estratÃ©gica enorme.

La frase simple:

> Modo Telegram: te protegemos de la IA externa.  
> Modo Privado: te protegemos tambiÃ©n de nosotros.

O, de forma mÃ¡s comercial:

> En Modo Privado, Prevengen ve el mismo caso anonimizado que la IA externa. Sabemos quiÃ©n es el cliente por motivos de cuenta y servicio, pero no necesitamos ver los datos sensibles que se han eliminado localmente antes del envÃ­o.

Esta deberÃ­a ser una promesa central del producto.

## 7. Verificabilidad: no solo prometer, sino mostrar quÃ© se envÃ­a

La confianza no debe basarse solo en decir â€œconfÃ­a en nosotrosâ€.

El producto debe mostrar al usuario quÃ© informaciÃ³n sale de su dispositivo.

Ejemplo de pantalla en Modo Privado:

```text
Modo Privado

Tu pregunta original permanece en este dispositivo.

Riesgo antes de reducir: 8/10
Motivos:
- contiene una entidad financiera concreta
- contiene un importe concreto
- menciona una venta de empresa
- menciona planificaciÃ³n de jubilaciÃ³n

Esto es lo que se enviarÃ¡ a Prevengen y a la IA externa:

"El usuario tiene un relaciones financiero alto en una entidad financiera,
ha tenido un evento de liquidez empresarial y quiere valorar su jubilaciÃ³n
en un horizonte de medio plazo."

Riesgo despuÃ©s de reducir: 3/10

[Editar versiÃ³n anonimizada]
[Enviar versiÃ³n anonimizada]
[Cancelar]
```

Esto convierte la confidencialidad en algo visible.

El usuario entiende:

```text
Texto original: se queda en mi dispositivo.
Texto anonimizado: sale hacia Prevengen.
IA externa: recibe solo el caso reducido.
```

AdemÃ¡s, el producto deberÃ­a tener un registro visible:

```text
/privacy_log
```

Ejemplo:

```text
10:42 â€” Riesgo local antes de reducir: 8/10
10:42 â€” ReducciÃ³n local: SÃ­
10:42 â€” Texto original enviado a Prevengen: No
10:42 â€” Texto enviado a IA externa: versiÃ³n anonimizada
10:42 â€” Memoria actualizada: No / SÃ­, cifrada localmente
```

Esto no sustituye una auditorÃ­a tÃ©cnica, pero crea control psicolÃ³gico y claridad prÃ¡ctica.

## 8. Open source de la capa de privacidad

Para dar mÃ¡s confianza, Prevengen puede publicar como cÃ³digo abierto solo la parte crÃ­tica de privacidad.

No hace falta abrir todo el producto.

Se puede abrir:

```text
- cÃ¡lculo del score de confidencialidad;
- reglas de detecciÃ³n de datos sensibles;
- reglas de anonimizaciÃ³n;
- generaciÃ³n de la vista previa de envÃ­o;
- cifrado local de la wiki;
- lÃ³gica que decide quÃ© sale del dispositivo.
```

Se puede mantener privado:

```text
- backend;
- prompts comerciales;
- workflows de asesoramiento;
- lÃ³gica de negocio;
- facturaciÃ³n;
- gestiÃ³n de usuarios;
- integraciones internas.
```

La promesa serÃ­a:

> No te pedimos que confÃ­es solo en una promesa invisible. Te mostramos quÃ© se envÃ­a y hacemos auditable la capa que decide quÃ© datos salen de tu dispositivo.

Esto es especialmente importante para clientes patrimoniales, porque la confianza debe sentirse y tambiÃ©n poder verificarse.

## 9. No necesitamos construir â€œotro Telegramâ€

La fase privada no requiere crear una red social ni una app de mensajerÃ­a completa.

No hace falta:

```text
- chats entre usuarios;
- grupos;
- contactos;
- llamadas;
- multimedia compleja;
- moderaciÃ³n social;
- descubrimiento de usuarios;
- canales pÃºblicos.
```

Solo hace falta:

```text
Usuario â†” Copiloto Relaciones
```

Es decir:

> Una interfaz privada de conversaciÃ³n para preguntas patrimoniales sensibles.

La versiÃ³n mÃ¡s simple puede ser una web:

```text
app.prevengen.com
```

Con:

```text
1. Login.
2. Pantalla de chat.
3. CÃ¡lculo local de riesgo.
4. AnonimizaciÃ³n local.
5. Vista previa de envÃ­o.
6. Respuesta del modelo.
7. Registro de privacidad.
8. MÃ¡s adelante, wiki cifrada.
```

Esto es mucho menos complejo que construir Telegram.

La frase estratÃ©gica:

> No construimos un mensajero generalista. Construimos una sala privada para pensar decisiones patrimoniales importantes.


## 10. Por quÃ© una PWA puede ser la soluciÃ³n ideal

Para la segunda fase, la mejor soluciÃ³n probablemente no es una app nativa de Android o iOS.

La mejor soluciÃ³n probablemente es una **PWA**: una Progressive Web App.

En tÃ©rminos simples:

> Una PWA es una web que puede sentirse como una app.

El usuario puede abrir:

```text
app.prevengen.com
```

Y en Android puede instalarla en la pantalla principal con un icono, como si fuera una app normal.

La PWA puede tener:

```text
- icono propio;
- pantalla de inicio;
- experiencia de chat;
- login;
- vista previa de privacidad;
- registro de privacidad;
- almacenamiento local;
- algunas capacidades offline;
- notificaciones push;
- en muchos casos, avisos de mensajes no leÃ­dos.
```

Esto encaja muy bien con Copiloto Relaciones porque la primera necesidad no es usar funciones profundas del mÃ³vil.

La primera necesidad es:

```text
1. El usuario escribe una pregunta sensible.
2. El navegador calcula localmente el riesgo.
3. El navegador anonimiza localmente.
4. El usuario ve quÃ© se enviarÃ¡.
5. Solo la versiÃ³n aprobada sale del dispositivo.
6. Prevengen y la IA externa reciben el mismo caso anonimizado.
```

Esto puede hacerse con JavaScript en el navegador.

### Ventaja principal

La PWA permite combinar tres cosas:

```text
1. Experiencia parecida a una app para usuarios normales.
2. CÃ³digo web mÃ¡s fÃ¡cil de desarrollar y mantener.
3. MÃ¡s transparencia tÃ©cnica que una app nativa.
```

Una persona tÃ©cnica puede abrir las herramientas del navegador y comprobar en la pestaÃ±a de red si se envÃ­a el texto original o solo la versiÃ³n anonimizada.

AdemÃ¡s, Prevengen puede abrir como cÃ³digo abierto la capa de privacidad:

```text
- score de confidencialidad;
- detecciÃ³n de datos sensibles;
- anonimizaciÃ³n;
- vista previa de envÃ­o;
- cifrado local de la wiki.
```

Esto hace que la promesa sea mÃ¡s verificable.

La frase simple:

> App-like para el usuario normal.  
> Inspeccionable como una web para el usuario tÃ©cnico.

### Avisos de mensajes no leÃ­dos

En Android, una PWA instalada puede mostrar avisos o badges de notificaciones no leÃ­das, dependiendo del navegador, del sistema operativo y del launcher del usuario.

Esto puede servir para:

```text
- una respuesta nueva;
- una pregunta pendiente de aprobaciÃ³n;
- una alerta de privacidad;
- un recordatorio de seguimiento patrimonial.
```

Pero no debe ser una pieza crÃ­tica del producto, porque el comportamiento exacto del badge no siempre estÃ¡ bajo control de Prevengen.

La privacidad y la confianza no deben depender del badge.

Deben depender de:

```text
- anonimizaciÃ³n local;
- vista previa antes de enviar;
- registro de privacidad;
- memoria cifrada;
- control visible del usuario.
```

### LÃ­mites de una PWA

Una PWA no es perfecta.

Puede tener lÃ­mites en:

```text
- integraciÃ³n profunda con el sistema operativo;
- almacenamiento seguro de claves;
- biometrÃ­a;
- notificaciones avanzadas;
- tareas en segundo plano;
- acceso a archivos;
- escaneo de documentos;
- comportamiento en iOS;
- experiencia mÃ³vil muy pulida.
```

En Android suele ser mÃ¡s potente.

En iOS puede funcionar, pero con mÃ¡s limitaciones.

Por eso la PWA es ideal para una fase 2, pero no necesariamente para todas las fases futuras.

La frase honesta:

> Una PWA es probablemente el mejor equilibrio entre privacidad, velocidad de desarrollo, transparencia y experiencia de usuario.

## 11. Por quÃ© una app nativa es mÃ¡s compleja

Una app nativa no es simplemente una web instalada.

Es un producto dentro del ecosistema de Android y/o iOS.

Eso aÃ±ade complejidad:

```text
- dos plataformas diferentes;
- reglas de Google Play y Apple App Store;
- permisos del dispositivo;
- almacenamiento seguro;
- biometrÃ­a;
- notificaciones;
- versiones del sistema operativo;
- tamaÃ±os de pantalla;
- firma de builds;
- publicaciÃ³n y revisiÃ³n;
- crash reports;
- backups;
- logs;
- actualizaciones;
- privacidad frente a teclados, capturas y servicios del sistema.
```

En un producto de privacidad, esto importa mucho.

Si la app guarda informaciÃ³n sensible, hay que pensar:

```text
- Â¿se copia en backups del sistema?
- Â¿aparece en logs?
- Â¿aparece en crash reports?
- Â¿puede leerla el teclado?
- Â¿se guardan capturas en el sistema?
- Â¿cÃ³mo se protege la clave local?
- Â¿quÃ© pasa si el usuario cambia de mÃ³vil?
```

Todo esto se puede resolver, pero no conviene hacerlo demasiado pronto.

Por eso el orden razonable es:

```text
Fase 1: Telegram MVP.
Fase 2: Web privada / PWA.
Fase 3: Wiki cifrada en cliente.
Fase 4: PWA mÃ¡s madura, con experiencia casi de app.
Fase 5: App nativa solo si los usuarios o clientes premium la necesitan.
```

La frase clave:

> No hace falta construir una app nativa para demostrar la tesis de privacidad.  
> Primero hay que demostrar que el usuario valora ver y aprobar lo que sale de su dispositivo.



## 12. Punto crÃ­tico: dÃ³nde se monta el prompt final

Esta es la correcciÃ³n arquitectÃ³nica mÃ¡s importante.

Para responder bien, el modelo externo necesita dos tipos de contexto:

```text
1. Instrucciones de producto
   CÃ³mo debe responder Copiloto Relaciones:
   independencia, estructura, disclaimers, forma de comparar opciones,
   preguntas para asesores, lÃ­mites legales y financieros.

2. Contexto privado del usuario
   Fragmentos de su wiki, preferencias, situaciÃ³n patrimonial,
   horizonte temporal, familia, decisiones previas, etc.
```

Las instrucciones de producto no son privadas.

Prevengen puede guardarlas en el servidor y aÃ±adirlas al prompt final sin problema.

El contexto privado del usuario es distinto.

Si el servidor de Prevengen descifra la wiki, selecciona fragmentos y monta el prompt final con contenido privado bruto, entonces Prevengen puede leer ese contenido.

No hay magia tÃ©cnica:

> Si Prevengen monta el prompt con la wiki descifrada, Prevengen puede leer la wiki.

Por eso hay que distinguir dos arquitecturas.

### Arquitectura dÃ©bil: prompt montado en servidor con wiki privada

```text
Usuario escribe
â†’ Prevengen recibe texto original
â†’ Prevengen lee wiki del usuario
â†’ Prevengen selecciona contexto
â†’ Prevengen monta el prompt final
â†’ Prevengen envÃ­a el prompt a la IA externa
```

Esta arquitectura es simple.

Pero la promesa honesta es limitada:

> Prevengen protege al usuario frente a exposiciÃ³n innecesaria ante la IA externa.

No puede prometer:

> Prevengen no puede leer la informaciÃ³n privada del usuario.

Porque tÃ©cnicamente sÃ­ puede.

### Arquitectura fuerte: contexto privado seleccionado localmente

En Modo Privado Web/PWA, el flujo debe ser diferente:

```text
Usuario escribe en la PWA
â†’ el navegador tiene o descifra la wiki localmente
â†’ el navegador selecciona fragmentos relevantes de la wiki
â†’ el navegador anonimiza y reduce esos fragmentos
â†’ el usuario ve la vista previa
â†’ solo el paquete reducido aprobado llega a Prevengen
â†’ Prevengen aÃ±ade instrucciones de producto
â†’ Prevengen envÃ­a el prompt final a la IA externa
```

En esta arquitectura, Prevengen puede montar el prompt final, pero solo con contexto privado ya reducido y aprobado.

Prevengen ve:

```text
- instrucciones propias de Copiloto Relaciones;
- pregunta anonimizada;
- fragmentos de wiki anonimizados y seleccionados localmente.
```

Prevengen no ve:

```text
- pregunta original;
- wiki completa;
- fragmentos privados brutos;
- bancos concretos eliminados localmente;
- importes exactos eliminados localmente;
- nombres, ciudades o datos familiares eliminados localmente.
```

La frase tÃ©cnica clave:

> El prompt final puede montarse en Prevengen, pero el contexto privado incluido en ese prompt debe haber sido seleccionado y anonimizado antes en el dispositivo del usuario.

La frase comercial:

> En Modo Privado, tu dispositivo decide quÃ© contexto privado sale. Prevengen recibe solo el caso reducido que tÃº apruebas.

### Ejemplo

Wiki local privada:

```text
El usuario tiene 800.000 euros en Caixabank.
El usuario vive en Barcelona.
El usuario vendiÃ³ una empresa concreta.
El usuario tiene un hijo llamado Marc.
```

Fragmentos enviados a Prevengen:

```text
El usuario tiene un relaciones financiero alto en una entidad espaÃ±ola.
El usuario tuvo un evento de liquidez empresarial.
El usuario tiene responsabilidades familiares relevantes.
```

Esto salva la idea de confidencialidad.

La privacidad no depende de que el servidor sea â€œbuenoâ€.

Depende de que el servidor no reciba la parte que no necesita.

## 13. ActualizaciÃ³n de la wiki: no recordar silenciosamente

La wiki necesita actualizarse.

Pero eso no significa que Prevengen tenga que leer toda la conversaciÃ³n ni editar la wiki en servidor.

Hay tres niveles posibles.

### Nivel 1 â€” MVP servidor

En Telegram, lo mÃ¡s simple es:

```text
Usuario conversa en Telegram
â†’ Prevengen recibe el texto
â†’ Prevengen calcula riesgo
â†’ Prevengen puede proponer o actualizar memoria
```

Esto es Ãºtil, pero la privacidad es mÃ¡s dÃ©bil.

Promesa honesta:

> En el MVP de Telegram, Prevengen procesa texto en servidor para ofrecer memoria y protecciÃ³n frente a IA externa.

### Nivel 2 â€” PWA con memoria explÃ­cita y aprobada

En Modo Privado, la memoria puede actualizarse de forma visible:

```text
DespuÃ©s de una conversaciÃ³n:
â€œÂ¿Quieres guardar algo en tu wiki privada?â€

Propuesta:
- El usuario estÃ¡ comparando una propuesta bancaria con asesoramiento independiente.
- El usuario quiere evitar exponer bancos e importes exactos.
- El usuario considera su jubilaciÃ³n en un horizonte de medio plazo.

[Guardar]
[Editar]
[Ignorar]
```

La propuesta puede generarse desde la versiÃ³n anonimizada ya enviada al modelo, no desde el texto bruto.

Esto permite avanzar sin una IA local compleja.

La frase de confianza:

> Copiloto no recuerda nada silenciosamente.

### Nivel 3 â€” Memory clerk local

MÃ¡s adelante, se puede aÃ±adir un pequeÃ±o â€œmemory clerkâ€ local.

Su funciÃ³n no serÃ­a responder como una IA grande.

SerÃ­a hacer tareas estrechas:

```text
- detectar hechos Ãºtiles;
- proponer actualizaciones de wiki;
- reescribir en lenguaje anonimizado;
- eliminar identificadores;
- pedir aprobaciÃ³n al usuario.
```

Esto puede hacerse con reglas, con modelos pequeÃ±os locales, o con una mezcla.

Pero no es necesario para demostrar la primera tesis de privacidad.

La prioridad es:

```text
1. Pregunta sensible se reduce localmente.
2. Fragmentos de wiki se seleccionan localmente.
3. El usuario ve quÃ© sale.
4. Prevengen recibe solo el paquete aprobado.
5. La memoria se actualiza solo con aprobaciÃ³n visible.
```

La promesa realista no es:

> Todo ocurre localmente.

La promesa realista es:

> El contenido sensible bruto y la wiki completa se quedan en el dispositivo. Prevengen recibe solo el contexto reducido que el usuario aprueba.


## 14. Wiki tokenizada y diccionario privado local

Esta idea resuelve una tensiÃ³n importante.

La wiki debe ser Ãºtil para el usuario, pero no debe exponer datos exactos a Prevengen ni a la IA externa si no es necesario.

La soluciÃ³n puede ser una **wiki tokenizada**:

```text
Texto real del usuario:
Tengo 800.000 euros en Caixabank.

Wiki tokenizada:
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.

Diccionario privado local:
CLIENT_WEALTH_1 = 800.000 euros
CLIENT_BANK_1 = Caixabank
```

La wiki que puede usar Prevengen o la IA externa no contiene el dato exacto.

Los valores reales se guardan en un diccionario privado local, cifrado en el dispositivo del usuario.

La frase simple:

> La wiki puede contener etiquetas. El significado exacto de esas etiquetas vive solo en el dispositivo del usuario.

### Tres vistas de la misma informaciÃ³n

El producto puede mostrar tres niveles.

#### 1. Vista privada exacta

Solo para el usuario, renderizada localmente:

```text
El usuario tiene 800.000 euros en Caixabank.
```

#### 2. Vista tokenizada

Guardada como wiki estructurada:

```text
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.
```

#### 3. Vista enviable a la IA externa

MÃ¡s abstracta y menos identificable:

```text
El usuario tiene un relaciones financiero alto en una entidad financiera.
```

Esto permite combinar:

```text
utilidad para el usuario
+ memoria estructurada
+ privacidad frente a Prevengen
+ minimizaciÃ³n frente a la IA externa
```

### Ejemplo con varios datos sensibles

Texto original:

```text
Tengo 800.000 euros en Caixabank, 250.000 euros en Indexa Capital,
vivo en Barcelona y quiero jubilarme en 7 aÃ±os.
```

Diccionario privado local:

```json
{
  "CLIENT_WEALTH_1": "800.000 euros",
  "CLIENT_BANK_1": "Caixabank",
  "CLIENT_WEALTH_2": "250.000 euros",
  "CLIENT_PLATFORM_1": "Indexa Capital",
  "CLIENT_CITY_1": "Barcelona",
  "CLIENT_RETIREMENT_HORIZON_1": "7 aÃ±os"
}
```

Wiki tokenizada:

```text
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.
El usuario tiene CLIENT_WEALTH_2 en CLIENT_PLATFORM_1.
El usuario vive en CLIENT_CITY_1.
El usuario quiere valorar su jubilaciÃ³n en CLIENT_RETIREMENT_HORIZON_1.
```

VersiÃ³n enviable:

```text
El usuario tiene un relaciones financiero alto repartido entre una entidad financiera
y una plataforma de inversiÃ³n, vive en una ciudad espaÃ±ola y quiere valorar su jubilaciÃ³n
en un horizonte de medio plazo.
```

### Hover o vista personal

Cuando el usuario lee la wiki, la PWA puede mostrar algo asÃ­:

```text
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.
```

Y al pasar el ratÃ³n o tocar la etiqueta:

```text
CLIENT_WEALTH_1 â†’ 800.000 euros
CLIENT_BANK_1 â†’ Caixabank
```

TambiÃ©n puede haber un interruptor:

```text
[Vista privada] [Vista tokenizada] [Vista enviable]
```

En vista privada, el usuario ve los datos reales.

En vista tokenizada, ve las etiquetas.

En vista enviable, ve lo que podrÃ­a salir hacia Prevengen y la IA externa.

Esto hace visible la privacidad.

### QuiÃ©n ve quÃ©

```text
Usuario:
- ve la wiki tokenizada;
- puede ver los valores reales localmente;
- puede editar el diccionario privado;
- decide quÃ© se envÃ­a.

PWA / navegador:
- descifra el diccionario local;
- sustituye valores reales por tokens;
- genera la vista enviable;
- cifra y sincroniza si hace falta.

Prevengen:
- ve la pregunta aprobada;
- ve fragmentos tokenizados o abstractos;
- no ve el diccionario privado local;
- no necesita saber que CLIENT_BANK_1 = Caixabank.

IA externa:
- ve solo la versiÃ³n aprobada;
- idealmente ve descripciones abstractas, no valores exactos.
```

### Tokens vs abstracciones

Hay que distinguir dos cosas.

Un token conserva estructura:

```text
CLIENT_BANK_1
```

Una abstracciÃ³n reduce identificaciÃ³n:

```text
una entidad financiera
```

Para la wiki local, los tokens son Ãºtiles.

Para la IA externa, muchas veces serÃ¡ mejor enviar abstracciones en lugar de tokens.

Ejemplo:

```text
Wiki tokenizada:
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.

Contexto enviado a IA externa:
El usuario tiene un relaciones financiero alto en una entidad financiera.
```

AsÃ­ la IA recibe suficiente contexto para razonar, pero no recibe el valor exacto ni el nombre de la entidad.

### ActualizaciÃ³n de wiki con tokens

Si el usuario escribe una nueva pregunta con datos sensibles, la PWA puede detectar esos datos localmente.

Ejemplo:

```text
Caixabank detectado como entidad financiera.
800.000 euros detectado como importe patrimonial.
```

La PWA puede proponer:

```text
Crear tokens locales:
CLIENT_BANK_1 = Caixabank
CLIENT_WEALTH_1 = 800.000 euros

Usar en la wiki:
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.

[Guardar] [Editar] [Ignorar]
```

La IA externa puede ayudar a mejorar la wiki, pero solo sobre la versiÃ³n ya anonimizada.

Por ejemplo, puede proponer:

```text
AÃ±adir a la wiki:
- El usuario compara asesoramiento bancario con asesoramiento independiente.
- El usuario quiere evitar recomendaciones influidas por venta de productos propios.
- El usuario prefiere no exponer bancos ni importes exactos.
```

Pero no debe gestionar el diccionario privado local.

El diccionario privado local lo gestiona la PWA, con aprobaciÃ³n del usuario.

### Principio de producto

La promesa no debe ser que la IA recuerda todo mÃ¡gicamente.

La promesa debe ser:

> Copiloto ayuda a mantener una memoria privada, tokenizada y controlada por el usuario.

Y tambiÃ©n:

> Los valores sensibles pueden vivir en tu dispositivo. El sistema puede razonar con etiquetas o abstracciones.

Frase comercial posible:

> Tus datos exactos se quedan en tu diccionario privado. La IA trabaja con el caso que necesita, no con tu identidad completa.


## 15. Flujo preciso de Fase 2 y riesgos a evitar

El flujo de Fase 2 debe ser muy claro, porque aquÃ­ se juega la promesa de confidencialidad.

Ejemplo inicial:

```text
Usuario escribe en la PWA:
"Tengo 800.000 euros en Caixabank. Â¿CÃ³mo invierto?"
```

La PWA no debe enviar inmediatamente ese texto a Prevengen.

Primero, el navegador ejecuta localmente la capa de privacidad:

```text
1. Detecta "800.000 euros" como importe sensible.
2. Detecta "Caixabank" como entidad financiera concreta.
3. Crea tokens locales si hace falta.
4. Guarda los valores exactos en el diccionario privado local.
5. Genera una versiÃ³n enviable.
6. Muestra al usuario quÃ© saldrÃ¡ del dispositivo.
7. Solo si el usuario aprueba, se envÃ­a el paquete reducido.
```

Ejemplo de diccionario privado local:

```json
{
  "CLIENT_WEALTH_1": "800.000 euros",
  "CLIENT_BANK_1": "Caixabank"
}
```

Ejemplo de wiki tokenizada:

```text
El usuario tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.
```

Ejemplo de versiÃ³n enviable:

```text
El usuario tiene un relaciones financiero alto en una entidad financiera.
Pregunta: Â¿CÃ³mo deberÃ­a pensar sobre la inversiÃ³n?
```

La versiÃ³n enviable puede usar tokens o abstracciones. Pero para la IA externa, muchas veces serÃ¡ mejor usar abstracciones:

```text
Mejor para privacidad:
"un relaciones financiero alto en una entidad financiera"

Menos abstracto:
"CLIENT_WEALTH_1 en CLIENT_BANK_1"
```

Los tokens son muy Ãºtiles para la wiki local y para la experiencia del usuario. Las abstracciones suelen ser mejores para reducir identificaciÃ³n frente a la IA externa.

### Evitar identificadores estables innecesarios

No conviene enviar algo como:

```text
[CLIENTE1493] tiene CLIENT_WEALTH_1 en CLIENT_BANK_1.
```

Aunque no sea el nombre real, `CLIENTE1493` puede funcionar como identificador estable. Permite que un proveedor externo vincule muchas consultas del mismo cliente a lo largo del tiempo.

Mejor:

```text
The user has a high patrimonial amount in a financial institution.
```

O, en espaÃ±ol:

```text
El usuario tiene un relaciones financiero alto en una entidad financiera.
```

Prevengen ya sabe quÃ© cuenta estÃ¡ usando el servicio. La IA externa no necesita un identificador estable del cliente.

### El paquete final que debe aprobar el usuario

El usuario no solo debe aprobar la pregunta reescrita.

Debe aprobar el paquete completo que saldrÃ¡ del dispositivo:

```text
1. Pregunta reducida.
2. Fragmentos de wiki seleccionados localmente.
3. Nivel de abstracciÃ³n usado.
4. Riesgo antes de reducir.
5. Riesgo despuÃ©s de reducir.
```

Ejemplo de vista previa:

```text
Paquete que se enviarÃ¡

Pregunta:
"El usuario tiene un relaciones financiero alto en una entidad financiera. Â¿CÃ³mo deberÃ­a pensar sobre la inversiÃ³n?"

Contexto seleccionado de la wiki:
- El usuario estÃ¡ comparando asesoramiento bancario con asesoramiento independiente.
- El usuario quiere evitar recomendaciones influidas por venta de productos propios.
- El usuario quiere valorar jubilaciÃ³n en un horizonte de medio plazo.

No se enviarÃ¡:
- importe exacto;
- nombre de la entidad financiera;
- nombre real del usuario;
- ciudad concreta;
- wiki completa.

Riesgo antes de reducir: 8/10
Riesgo despuÃ©s de reducir: 3/10

[Enviar] [Editar] [Cancelar]
```

La regla es:

> Hay que puntuar el riesgo del paquete final, no solo de la pregunta original.

Una pregunta puede estar bien anonimizada, pero los fragmentos de wiki aÃ±adidos pueden reidentificar al usuario si son demasiados o demasiado especÃ­ficos.

### QuÃ© ve cada parte

```text
Usuario:
- ve el texto original;
- ve tokens y valores reales en su dispositivo;
- aprueba quÃ© sale;
- controla la wiki y el diccionario privado.

PWA:
- procesa localmente;
- detecta datos sensibles;
- crea tokens;
- genera abstracciones;
- cifra el diccionario privado.

Prevengen:
- recibe solo el paquete aprobado;
- aÃ±ade instrucciones de producto y skills;
- no recibe el texto bruto si estÃ¡ en Modo Privado;
- no recibe el diccionario privado local.

IA externa:
- recibe el caso reducido;
- recibe instrucciones de producto;
- no recibe identidad de cuenta;
- no recibe importes exactos ni entidades concretas si han sido eliminadas localmente.
```

### Respuesta y actualizaciÃ³n de wiki

La IA externa puede responder la pregunta y tambiÃ©n proponer una actualizaciÃ³n de la wiki, pero no debe modificarla directamente.

Flujo correcto:

```text
IA externa responde.
IA externa propone actualizaciÃ³n de wiki usando solo informaciÃ³n anonimizada.
PWA muestra la propuesta al usuario.
Usuario guarda, edita o ignora.
PWA actualiza wiki/token vault localmente.
```

Ejemplo de propuesta de actualizaciÃ³n:

```text
Propuesta para la wiki:
- El usuario quiere comparar asesoramiento bancario con asesoramiento independiente.
- El usuario quiere evitar recomendaciones influidas por venta de productos propios.
- El usuario prefiere no exponer bancos ni importes exactos.

[Guardar] [Editar] [Ignorar]
```

Principio:

> La IA externa propone. El usuario aprueba. Copiloto no recuerda nada silenciosamente.

### Riesgos principales de esta estrategia

#### 1. â€œProvable to anybodyâ€ es demasiado fuerte

Una persona tÃ©cnica puede inspeccionar el trÃ¡fico de red del navegador y comprobar si se envÃ­a texto bruto o solo texto reducido.

Pero un usuario normal no puede probar todo por sÃ­ mismo.

La promesa correcta es:

> La app muestra quÃ© se enviarÃ¡, la capa de privacidad puede ser open source y usuarios tÃ©cnicos o auditores pueden verificar que el Modo Privado envÃ­a solo el paquete aprobado.

#### 2. El JavaScript puede cambiar

Como Prevengen sirve la web, Prevengen podrÃ­a cambiar el JavaScript en una versiÃ³n futura.

Mitigaciones:

```text
- open source de la capa de privacidad;
- versiÃ³n visible del mÃ³dulo de privacidad;
- hashes pÃºblicos;
- changelog pÃºblico;
- auditorÃ­as externas;
- eventualmente releases firmadas o extensiÃ³n de navegador para usuarios avanzados.
```

#### 3. Los tokens pueden filtrar estructura

`CLIENT_BANK_1` no revela â€œCaixabankâ€, pero sÃ­ revela que existe una entidad concreta oculta.

A veces eso estÃ¡ bien. A veces conviene abstraer mÃ¡s:

```text
CLIENT_BANK_1 â†’ una entidad financiera
CLIENT_WEALTH_1 â†’ un relaciones financiero alto
CLIENT_CITY_1 â†’ una ciudad espaÃ±ola
```

#### 4. La IA puede necesitar rangos Ãºtiles

Para dar una respuesta Ãºtil, la IA externa puede necesitar algo mÃ¡s que â€œun importe altoâ€.

SoluciÃ³n: enviar rangos, no valores exactos.

```text
No enviar:
800.000 euros

Mejor:
importe alto de seis cifras

O si hace falta:
entre 500.000 y 1.000.000 de euros
```

Para una entidad:

```text
No enviar:
Caixabank

Mejor:
una gran entidad bancaria espaÃ±ola
```

#### 5. La wiki anonimizada puede reidentificar si se envÃ­a demasiado

Incluso sin nombres, una combinaciÃ³n de datos puede identificar a una persona.

Ejemplo de riesgo:

```text
relaciones alto
venta de empresa
ciudad concreta
hijo dependiente
jubilaciÃ³n en 7 aÃ±os
banco espaÃ±ol concreto
```

MitigaciÃ³n:

```text
- no enviar la wiki completa;
- seleccionar solo fragmentos relevantes;
- reducir detalles innecesarios;
- puntuar el paquete final;
- mostrar la vista previa completa al usuario.
```

#### 6. La IA externa no debe sobrescribir memoria

La IA externa debe proponer memoria, no escribirla.

Esto evita:

```text
- errores silenciosos;
- recuerdos falsos;
- acumulaciÃ³n de datos innecesarios;
- sensaciÃ³n de dossier oculto.
```

#### 7. Hay que elegir bien proveedores externos

Aunque la informaciÃ³n estÃ© reducida, Prevengen debe usar proveedores/API con condiciones adecuadas:

```text
- no entrenamiento con prompts privados por defecto;
- retenciÃ³n limitada si es posible;
- configuraciÃ³n empresarial/API;
- contratos y polÃ­ticas claras.
```

### Flujo fuerte corregido

```text
Usuario escribe:
"Tengo 800.000 euros en Caixabank. Â¿CÃ³mo invierto?"

PWA local:
- detecta importe y banco;
- crea tokens locales;
- guarda valores exactos en diccionario privado cifrado;
- genera versiÃ³n enviable abstracta;
- selecciona fragmentos relevantes de la wiki;
- reduce esos fragmentos;
- muestra paquete final;
- calcula riesgo del paquete final.

Usuario aprueba.

Prevengen recibe:
- pregunta reducida;
- fragmentos de wiki reducidos;
- no texto original;
- no diccionario privado local.

Prevengen aÃ±ade:
- instrucciones de Copiloto;
- skills;
- formato de respuesta;
- lÃ­mites legales/fiscales/financieros.

IA externa recibe:
- caso reducido;
- instrucciones de producto;
- no identidad de cuenta;
- no banco exacto;
- no importe exacto.

IA externa devuelve:
- respuesta;
- propuesta de actualizaciÃ³n de wiki.

Usuario aprueba o edita.

PWA guarda:
- wiki tokenizada/anÃ³nima;
- valores exactos solo en diccionario privado local cifrado.
```

La frase de arquitectura:

> La PWA posee la verdad privada. Prevengen y la IA externa reciben solo la abstracciÃ³n Ãºtil aprobada por el usuario.



## 16. Competidores y hueco de mercado

Hay empresas y proyectos cercanos, pero no parecen competir exactamente con la tesis de Prevengen.

El mercado se puede ordenar en varias familias.

### 13.1. Apps de memoria personal o â€œinfinite memoryâ€

Ejemplos:

```text
Rewind / Limitless
Screenpipe
Personal.ai
```

Estas herramientas intentan recordar mÃ¡s cosas sobre el usuario: conversaciones, reuniones, archivos, pantalla, voz, recuerdos o informaciÃ³n personal.

Su idea principal suele ser:

> La IA puede ayudarte mejor si recuerda mÃ¡s sobre ti.

Esto estÃ¡ cerca de Prevengen por el lado de la memoria.

Pero no es lo mismo.

Prevengen no quiere simplemente recordar mÃ¡s.

Quiere:

> Recordar lo suficiente para ayudar, exponiendo lo mÃ­nimo posible.

La diferencia es importante.

Una app de memoria puede acabar creando un dossier muy Ãºtil pero demasiado legible.

Prevengen debe crear una memoria Ãºtil, visible, editable, tokenizada y controlada.

### 13.2. Asistentes privados de IA

Ejemplo claro:

```text
Proton Lumo
```

Este tipo de producto compite por confianza.

Su promesa es:

```text
- privacidad;
- cifrado;
- no logs;
- no entrenamiento con conversaciones;
- control del usuario;
- cÃ³digo auditable.
```

Esto estÃ¡ cerca del espÃ­ritu de Prevengen.

Pero sigue siendo distinto.

Un asistente privado generalista responde preguntas.

Prevengen debe ser una capa de decisiÃ³n confidencial, con:

```text
- verticales sensibles;
- skills especÃ­ficas;
- memoria estructurada;
- tokenizaciÃ³n local;
- vista previa de salida;
- control de quÃ© contexto se envÃ­a;
- independencia frente a proveedores con incentivos.
```

Lumo puede ser una buena referencia de confianza.

Pero Prevengen no debe limitarse a ser â€œotro chatbot privadoâ€.

### 13.3. Capas de memoria para agentes

Ejemplos:

```text
Zep
Mem0
Letta
```

Estas plataformas ayudan a agentes de IA a tener memoria.

Suelen permitir:

```text
- guardar recuerdos;
- recuperar contexto;
- montar prompts mejores;
- personalizar respuestas;
- alimentar llamadas a LLMs externos.
```

Son relevantes tÃ©cnicamente.

Pero normalmente estÃ¡n pensadas para desarrolladores y agentes, no para un usuario final que quiere decidir quÃ© informaciÃ³n sensible sale de su dispositivo.

Su objetivo principal suele ser:

> Dar mÃ¡s contexto al agente.

El objetivo de Prevengen debe ser distinto:

> Dar al agente solo el contexto necesario y seguro.

### 13.4. InvestigaciÃ³n sobre memoria privada

Ejemplo:

```text
Opal: private memory for personal AI
```

Este tipo de investigaciÃ³n es muy relevante porque intenta resolver el problema profundo:

> Â¿Puede una IA usar memoria personal sin que el proveedor de la aplicaciÃ³n lea esa memoria?

Pero es una lÃ­nea mÃ¡s tÃ©cnica y avanzada, vinculada a enclaves, hardware seguro o arquitecturas complejas.

Prevengen no necesita empezar por ahÃ­.

Puede empezar con una soluciÃ³n mÃ¡s prÃ¡ctica:

```text
PWA privada
+ anonimizaciÃ³n local
+ diccionario privado local
+ wiki tokenizada
+ vista previa de salida
+ aprobaciÃ³n del usuario
```

### 13.5. ConclusiÃ³n competitiva

La conclusiÃ³n no es que â€œno hay competidores porque Relaciones sea un nichoâ€.

La conclusiÃ³n es mÃ¡s fuerte:

> Hay productos de memoria.  
> Hay productos de IA privada.  
> Hay infraestructura de memoria para agentes.  
> Pero no parece haber un producto centrado en decisiones sensibles que combine memoria, confidencialidad, tokenizaciÃ³n local, vista previa de salida y skills de decisiÃ³n por vertical.

El hueco no es solo patrimonial.

El hueco es:

> IA confidencial para decisiones humanas importantes.

Copiloto Relaciones es el primer caso de uso.

Pero la categorÃ­a puede ser mayor.

## 17. Prevengen como metodologÃ­a transversal

Prevengen no deberÃ­a entenderse solo como una empresa de relaciones.

Copiloto Relaciones puede ser el primer vertical, pero la metodologÃ­a puede aplicarse a otros temas sensibles.

La tesis general:

> Prevengen es una capa privada de decisiÃ³n para temas que el usuario no quiere exponer casualmente.

El patrÃ³n comÃºn es:

```text
1. El usuario tiene una pregunta sensible.
2. El dispositivo detecta datos privados.
3. Los datos exactos se tokenizan o abstraen localmente.
4. El usuario ve quÃ© saldrÃ¡ del dispositivo.
5. Prevengen recibe solo el paquete aprobado.
6. El LLM externo recibe solo el caso reducido.
7. Las skills del vertical guÃ­an la respuesta.
8. La memoria se actualiza solo con aprobaciÃ³n.
```

Este mÃ©todo puede aplicarse a varios copilotos.

### 14.1. Copiloto Relaciones

Datos sensibles tÃ­picos:

```text
CLIENT_WEALTH_1
CLIENT_BANK_1
CLIENT_ADVISOR_1
CLIENT_COMPANY_SALE_1
CLIENT_RETIREMENT_HORIZON_1
CLIENT_TAX_COUNTRY_1
```

Skills necesarias:

```text
- anÃ¡lisis de propuestas bancarias;
- detecciÃ³n de conflictos de interÃ©s;
- preguntas para asesores regulados;
- comparaciÃ³n de escenarios;
- riesgos fiscales y legales;
- lÃ­mites claros: no sustituir asesoramiento regulado.
```

### 14.2. Copiloto Salud

Datos sensibles tÃ­picos:

```text
CLIENT_CONDITION_1
CLIENT_MEDICATION_1
CLIENT_DOCTOR_1
CLIENT_TEST_RESULT_1
CLIENT_SYMPTOM_1
CLIENT_HEALTH_HISTORY_1
```

Skills necesarias:

```text
- organizar sÃ­ntomas;
- preparar visita mÃ©dica;
- identificar seÃ±ales de alarma;
- explicar conceptos mÃ©dicos con cautela;
- recomendar atenciÃ³n profesional cuando corresponda;
- no diagnosticar como autoridad final.
```

AquÃ­ el riesgo es mayor que en relaciones.

Una mala respuesta puede afectar la salud.

Por eso el vertical de salud necesita reglas estrictas, lenguaje prudente y escalado claro a profesionales.

### 14.3. Copiloto Relaciones

Datos sensibles tÃ­picos:

```text
PARTNER_1
EX_PARTNER_1
CHILD_1
CONFLICT_EVENT_1
BOUNDARY_1
RELATIONSHIP_PATTERN_1
```

Skills necesarias:

```text
- aclarar necesidades;
- preparar conversaciones difÃ­ciles;
- detectar patrones;
- diferenciar lÃ­mites sanos de control;
- detectar seÃ±ales de abuso o coerciÃ³n;
- evitar dar certeza falsa sobre las intenciones de otra persona.
```

AquÃ­ el riesgo no es regulatorio en el mismo sentido que salud o relaciones, pero es emocionalmente delicado.

El sistema no debe alimentar paranoia, dependencia, idealizaciÃ³n ni decisiones impulsivas.

### 14.4. Copiloto Familia / Dependencia

Datos sensibles tÃ­picos:

```text
FAMILY_MEMBER_1
DEPENDENCY_STATUS_1
CARE_NEED_1
SCHOOL_OR_CENTER_1
PUBLIC_SERVICE_1
LEGAL_GUARDIANSHIP_1
```

Skills necesarias:

```text
- ordenar trÃ¡mites;
- preparar preguntas para servicios sociales;
- organizar documentos;
- priorizar tareas;
- explicar opciones sin sustituir asesoramiento profesional;
- reducir carga emocional y burocrÃ¡tica.
```

### 14.5. Copiloto Trabajo / Carrera

Datos sensibles tÃ­picos:

```text
EMPLOYER_1
CLIENT_1
SALARY_1
BUSINESS_OPPORTUNITY_1
CONFLICT_1
NEGOTIATION_1
```

Skills necesarias:

```text
- preparar negociaciones;
- ordenar oportunidades;
- analizar riesgos;
- redactar mensajes;
- proteger informaciÃ³n comercial;
- evitar compartir datos innecesarios con modelos externos.
```

### 14.6. Lo comÃºn y lo distinto

Lo comÃºn en todos los copilotos:

```text
- privacidad local;
- anonimizaciÃ³n;
- tokenizaciÃ³n;
- diccionario privado;
- vista previa de salida;
- memoria visible;
- control del usuario;
- no recordar silenciosamente.
```

Lo distinto en cada copiloto:

```text
- skills;
- lÃ­mites;
- protocolos de seguridad;
- lenguaje;
- riesgos legales, mÃ©dicos, financieros o emocionales.
```

La arquitectura de privacidad puede ser comÃºn.

La lÃ³gica de asesoramiento no debe ser genÃ©rica.

La frase estratÃ©gica:

> Prevengen Core protege la informaciÃ³n.  
> Cada Copiloto aporta el juicio especÃ­fico del dominio.

### 14.7. Por quÃ© el hueco competitivo sigue existiendo fuera de relaciones

Si Prevengen lanzara salud, relaciones o familia, el hueco seguirÃ­a siendo parecido.

No porque no existan apps de salud, terapia, journaling, finanzas o relaciones.

Existen muchas.

Pero pocas parecen estar construidas alrededor de esta combinaciÃ³n:

```text
1. Preguntas sensibles.
2. Memoria persistente.
3. TokenizaciÃ³n local.
4. Diccionario privado local.
5. Vista previa de salida.
6. External LLM minimization.
7. Skills especÃ­ficas por dominio.
8. Memoria aprobada por el usuario.
```

La falta de competidores directos no depende de que â€œrelacionesâ€ sea especial.

Depende de que el mercado todavÃ­a tiende a optimizar para:

```text
- mÃ¡s memoria;
- mÃ¡s personalizaciÃ³n;
- mÃ¡s automatizaciÃ³n;
- mÃ¡s comodidad.
```

Prevengen debe optimizar para otra cosa:

```text
- suficiente memoria;
- mÃ­nima exposiciÃ³n;
- mÃ¡ximo control;
- mejor decisiÃ³n.
```

Esa puede ser la categorÃ­a:

> Confidential AI for consequential life decisions.

En espaÃ±ol:

> IA confidencial para decisiones importantes de vida.

Copiloto Relaciones serÃ­a la primera prueba de esta categorÃ­a.


## 18. Posicionamiento

Copiloto Relaciones puede ocupar una categorÃ­a distinta:

> Un copiloto confidencial e independiente para decisiones patrimoniales importantes.

No sustituye a un asesor financiero regulado, fiscalista o abogado.

Su funciÃ³n es previa y complementaria:

- ayudar al usuario a entender su situaciÃ³n;
- ordenar la informaciÃ³n;
- detectar riesgos;
- preparar preguntas;
- comparar propuestas;
- reducir exposiciÃ³n de datos sensibles;
- ayudar al usuario a decidir mejor antes de hablar con un banco, asesor o proveedor.

La frase estratÃ©gica podrÃ­a ser:

> Para las decisiones demasiado importantes para preguntÃ¡rselas a Google.

O, mÃ¡s sobrio:

> IA privada para decisiones que importan.

O:

> Piensa tu relaciones con confidencialidad, independencia y control.

## 19. Por quÃ© existe la oportunidad

Mucha gente empieza a sentirse incÃ³moda con una IA integrada en todo: buscador, correo, calendario, documentos, fotos, compras, mapas y pagos.

El problema no es solo la IA.

El problema es la combinaciÃ³n de:

- mucha personalizaciÃ³n;
- muchos datos personales;
- incentivos comerciales;
- posibles conflictos de interÃ©s;
- poca claridad sobre quiÃ©n accede a quÃ©;
- poca sensaciÃ³n de control.

En temas de baja importancia, el usuario acepta este intercambio.

Pero en temas de alta importancia, el usuario quiere otra cosa:

> Un espacio protegido.

Copiloto Relaciones debe ser ese espacio.

## 20. Enemigo claro

El enemigo no es Google como empresa.

El enemigo es:

- consejo con incentivos ocultos;
- venta disfrazada de asesoramiento;
- bancos recomendando productos propios;
- IA que recuerda demasiado sin mostrar quÃ© recuerda;
- datos personales convertidos en un dossier opaco;
- recomendaciones sin trazabilidad;
- decisiones importantes tomadas sin claridad.

Copiloto Relaciones debe posicionarse contra eso.

No como una herramienta â€œanti-tecnologÃ­aâ€, sino como una herramienta de soberanÃ­a.

## 21. Promesa del producto

Promesa funcional:

> Te ayudo a entender, ordenar y preparar tus decisiones patrimoniales sin exponerte innecesariamente.

Promesa emocional:

> Puedes pensar aquÃ­ sin sentir que estÃ¡s siendo observado, vendido o empujado.

Promesa Ã©tica:

> No gano dinero vendiÃ©ndote productos financieros. Mi trabajo es ayudarte a pensar mejor.

Promesa de control:

> Puedes ver, editar, exportar y borrar lo que el sistema recuerda.

## 22. Arquitectura de privacidad

La arquitectura debe separar tres cosas:

```text
1. Identidad
   nombre, email, login, facturaciÃ³n, consentimientos

2. Memoria
   wiki privada y anonimizada del usuario

3. Datos de mejora
   mÃ©tricas agregadas, datos sintÃ©ticos, ejemplos anonimizados u opt-in
```

La identidad y la memoria no deben mezclarse de forma casual.

La idea comercial es:

> Memoria personal de IA sin convertir al usuario en un dossier legible.

## 23. Memoria visible y anonimizada

La memoria no debe ser una base de datos oculta.

Debe ser una wiki visible por el usuario.

Ejemplo correcto:

```text
El usuario tiene un hijo.
El usuario estÃ¡ valorando su jubilaciÃ³n.
El usuario estÃ¡ comparando una propuesta bancaria con una opciÃ³n independiente.
El usuario vendiÃ³ una empresa en el pasado.
```

Ejemplo incorrecto:

```text
Jordi tiene un hijo llamado Marc.
Jordi vendiÃ³ su empresa en Barcelona.
Jordi tiene 800.000 euros en Caixabank.
```

La memoria debe usar lenguaje por roles, no nombres reales cuando no sean necesarios.

Ejemplos:

```text
mi banco â†’ una entidad financiera
mi asesor â†’ un asesor financiero
mi hijo â†’ el hijo del usuario
Barcelona â†’ una ciudad
800.000 euros â†’ un importe patrimonial alto
```

## 24. Confidencialidad antes de inteligencia

La regla central:

> Antes de responder bien, el sistema debe reducir el riesgo de exposiciÃ³n.

Por eso el flujo debe ser:

```text
Texto del usuario
â†’ detecciÃ³n de riesgo de privacidad
â†’ reducciÃ³n o anonimizaciÃ³n local si hace falta
â†’ aprobaciÃ³n del usuario si el riesgo es alto
â†’ envÃ­o mÃ­nimo necesario al modelo
â†’ respuesta
â†’ logs y memoria controlada
```

Esto convierte la privacidad en parte del producto, no en una nota legal al final.

## 25. Modos de privacidad

Copiloto Relaciones puede tener varios modos.

### Modo estÃ¡ndar

- Memoria visible y anonimizada.
- Solo se envÃ­an al modelo los fragmentos necesarios.
- No se entrena con conversaciones privadas por defecto.
- Acceso humano restringido, registrado y minimizado.

### Modo memoria privada

- La wiki se cifra en el dispositivo del usuario.
- La empresa no tiene la clave de descifrado.
- La selecciÃ³n de memoria relevante ocurre localmente.
- El servidor almacena solo datos cifrados.

### Modo inferencia confidencial

- El dispositivo selecciona fragmentos anonimizados.
- El prompt se envÃ­a cifrado a un entorno seguro de GPU.
- El backend normal no puede leer prompt ni respuesta.
- Es un modo premium para usuarios que necesitan mÃ¡xima confianza.

### Modo local

- Todo ocurre en el dispositivo.
- Preguntas, memoria y respuestas permanecen localmente.
- Menor calidad posible, pero mÃ¡xima privacidad.

## 26. Afirmaciones honestas

Hay que distinguir entre dos niveles.

### AfirmaciÃ³n dÃ©bil

```text
Los datos estÃ¡n cifrados en reposo.
La empresa controla las claves.
```

Esto no significa que la empresa no pueda leerlos.

Frase honesta:

> El acceso estÃ¡ restringido, registrado y minimizado.

### AfirmaciÃ³n fuerte

```text
La memoria estÃ¡ cifrada en el dispositivo.
El usuario controla la clave.
La empresa solo almacena texto cifrado.
```

Entonces sÃ­ se puede decir:

> No podemos leer tu memoria privada almacenada porque no tenemos la clave.

Solo hay que usar esta promesa si es tÃ©cnicamente cierta.

## 27. Control visible para el usuario

Para personas normales, la confianza no viene solo de cumplimiento legal.

Viene de sentir control.

Por eso el producto debe tener comandos claros:

```text
/privacy
/export
/delete_all
/forget_topic
/pause_memory
/show_memory
/support_unlock 30min
```

Ejemplo:

```text
/privacy
```

Respuesta posible:

```text
Estado de privacidad

Ãšltimo acceso humano a tus datos: Nunca
Ãšltima actualizaciÃ³n del sistema: 22 de mayo de 2026
Ãšltima ediciÃ³n de memoria: Hoy
ExportaciÃ³n disponible: SÃ­
Borrar todos los datos: SÃ­
Soporte desbloqueado: No
```

La idea emocional es sencilla:

> Nadie entra salvo que tÃº abras la puerta.

## 28. Soporte humano

Por defecto, nadie deberÃ­a acceder al contenido del usuario.

Si hace falta soporte:

```text
/support_unlock 30min
```

Esto concede acceso temporal durante 30 minutos.

Condiciones:

- consentimiento explÃ­cito;
- acceso limitado;
- acceso registrado;
- expiraciÃ³n automÃ¡tica;
- notificaciÃ³n al usuario;
- posibilidad de revocar.

Durante pruebas tempranas, se debe ser transparente:

> Durante la fase de pruebas, algunos testers pueden autorizar revisiÃ³n humana de wikis anonimizadas para mejorar la calidad de anonimizaciÃ³n y memoria.

No hay que fingir â€œcero conocimientoâ€ si todavÃ­a hay revisiÃ³n humana.

## 29. MVP recomendado

Primera versiÃ³n:

```text
1. Bot de Telegram.
2. DetecciÃ³n de riesgo de confidencialidad en servidor.
3. Umbral de revisiÃ³n manual.
4. AnonimizaciÃ³n/reducciÃ³n de prompts de alto riesgo.
5. AprobaciÃ³n del usuario antes de enviar contenido sensible a una IA externa.
6. Respuestas estructuradas.
7. Logs bÃ¡sicos.
8. Wiki visible y editable.
9. Comandos /privacy, /export, /delete_all, /forget_topic.
```

Promesa honesta del MVP:

> En Telegram, Prevengen recibe el texto original, pero protege al cliente antes de enviar contenido a una IA externa.

Siguiente mejora clave:

```text
Modo Privado Web/App:
- score de confidencialidad calculado localmente;
- anonimizaciÃ³n local;
- vista previa de lo que se enviarÃ¡;
- Prevengen recibe solo la versiÃ³n aprobada y reducida.
```

La primera ventaja competitiva no debe ser tener â€œla mejor IAâ€.

Debe ser:

> La IA patrimonial que trata tus datos como algo sagrado.


## 30. Enclaves, atestaciÃ³n remota e inferencia local

Esta conversaciÃ³n aÃ±ade una pieza importante al mapa de privacidad: la posibilidad de usar un **servidor de computaciÃ³n confidencial** como una sala sellada donde se combinan temporalmente datos del cliente, skills propietarias de Prevengen y, en una fase futura, incluso un modelo abierto ejecutÃ¡ndose localmente.

La palabra tÃ©cnica inglesa **attestation** puede traducirse al catalÃ¡n como:

```text
atestaciÃ³
atestaciÃ³ remota
verificaciÃ³ criptogrÃ fica
prova verificable d'execuciÃ³
```

Para el producto, la expresiÃ³n mÃ¡s Ãºtil probablemente es:

> **atestaciÃ³n remota** / **atestaciÃ³ remota**.

La idea no es que el usuario â€œconfÃ­e en un administrador buenoâ€. La idea correcta es que el usuario, Prevengen o ambos puedan verificar criptogrÃ¡ficamente que el cÃ³digo esperado estÃ¡ ejecutÃ¡ndose dentro de un entorno protegido antes de enviar secretos.

### 30.1. Por quÃ© el proveedor del enclave no deberÃ­a poder leer los datos

Un VPS normal no basta para esta promesa.

En un VPS normal, el proveedor de nube controla el hipervisor y la infraestructura. Aunque los datos estÃ©n cifrados en reposo y en trÃ¡nsito, durante el procesamiento aparecen en claro en memoria. En teorÃ­a, un administrador con suficiente control sobre la infraestructura podrÃ­a inspeccionar memoria, snapshots, discos, logs o procesos.

En un enclave o confidential VM, la promesa tÃ©cnica es distinta:

```text
1. El hardware crea una regiÃ³n aislada de ejecuciÃ³n.
2. La memoria usada por esa regiÃ³n estÃ¡ protegida/cifrada por hardware.
3. El sistema operativo, el hipervisor y el administrador cloud no deberÃ­an poder leer el contenido en claro.
4. Los secretos se entregan solo despuÃ©s de verificar la atestaciÃ³n remota.
5. El cÃ³digo dentro del enclave descifra y procesa los datos temporalmente.
6. Fuera del enclave solo deberÃ­an verse blobs cifrados, metadatos y consumo de recursos.
```

La metÃ¡fora:

> El enclave es una sala sellada dentro del edificio del proveedor cloud. El proveedor puede ver que la sala existe, cuÃ¡nta electricidad consume y quÃ© trÃ¡fico entra y sale, pero no deberÃ­a poder abrir la sala ni leer lo que ocurre dentro.

Lo esencial es que el cliente no envÃ­a la clave a â€œun servidorâ€, sino a un cÃ³digo concreto verificado por atestaciÃ³n.

Sin atestaciÃ³n, el proveedor podrÃ­a ejecutar otro cÃ³digo que filtrara los secretos.

Con atestaciÃ³n, el flujo correcto es:

```text
Cliente / Prevengen
â†’ verifica el hash del cÃ³digo y la identidad del enclave
â†’ comprueba que se ejecuta en hardware confidencial genuino
â†’ solo entonces entrega claves o secretos
â†’ el enclave procesa datos en memoria protegida
â†’ el resultado sale reducido, cifrado o controlado
```

La promesa no debe formularse como seguridad perfecta.

La promesa honesta es:

> Un enclave reduce de forma material la necesidad de confiar en el proveedor cloud y en el administrador del servidor. No elimina todos los riesgos, pero cambia el modelo de confianza.

### 30.2. Riesgos y lÃ­mites de los enclaves

Confidential computing no es magia.

Hay riesgos a vigilar:

```text
- ataques de canal lateral;
- vulnerabilidades de CPU o firmware;
- cÃ³digo de enclave mal escrito;
- logs accidentales;
- respuestas o prompts enviados fuera del enclave;
- dependencias de software comprometidas;
- errores en la gestiÃ³n de claves;
- filtraciÃ³n por metadatos o patrones de trÃ¡fico;
- confianza residual en el fabricante del hardware y en la cadena de suministro.
```

Por eso la fÃ³rmula correcta no es:

> Nadie puede ver nada jamÃ¡s.

La fÃ³rmula correcta es:

> El sistema estÃ¡ diseÃ±ado para que ni Prevengen, ni el proveedor cloud, ni la IA externa reciban datos brutos que no necesitan, y para que el acceso al procesamiento sensible estÃ© limitado por hardware, atestaciÃ³n y minimizaciÃ³n.

### 30.3. Tres arquitecturas de inferencia

Hay tres niveles relevantes para Prevengen.

#### Nivel 1 â€” Orquestador en enclave + LLM externo

```text
PWA / cliente
â†’ datos reducidos o cifrados
â†’ enclave de Prevengen
â†’ composiciÃ³n del prompt / reducciÃ³n adicional / skills
â†’ LLM externo
```

Ventajas:

```text
- mÃ¡s fÃ¡cil;
- coste bajo o moderado;
- permite usar los mejores modelos externos;
- buena fase inicial o premium temprana;
- protege mejor el punto donde se combinan contexto privado y skills propietarias.
```

LimitaciÃ³n:

```text
El LLM externo sigue viendo el prompt final reducido.
```

Por eso este nivel debe combinarse con minimizaciÃ³n, abstracciÃ³n, no envÃ­o de identificadores estables y proveedores de IA con condiciones empresariales adecuadas.

#### Nivel 2 â€” Modelo abierto pequeÃ±o/medio dentro del enclave

```text
PWA / cliente
â†’ enclave
â†’ modelo abierto local dentro del enclave
â†’ respuesta generada dentro del enclave
```

AquÃ­ el LLM externo deja de ver el prompt y la respuesta.

Esto es muy interesante para Prevengen porque muchos trabajos sensibles no requieren necesariamente un frontier model:

```text
- selecciÃ³n y resumen de memoria;
- memory clerk;
- clasificaciÃ³n de riesgo;
- anonimizaciÃ³n asistida;
- preguntas de seguimiento;
- estructuraciÃ³n de documentos;
- razonamiento patrimonial guiado por skills;
- preparaciÃ³n de conversaciones con asesores.
```

Modelos abiertos de **7Bâ€“14B** parÃ¡metros parecen el rango mÃ¡s cÃ³modo para empezar en esta arquitectura.

No porque sean perfectos, sino porque combinan:

```text
- coste razonable;
- facilidad de despliegue;
- menor consumo de RAM/VRAM;
- suficiente capacidad para tareas estructuradas;
- buena compatibilidad con cuantizaciÃ³n;
- posibilidad de correr como modo privado premium o interno.
```

#### Nivel 3 â€” Modelo abierto grande dentro del enclave

Un modelo de unos **27B parÃ¡metros** tambiÃ©n puede ser viable, pero ya no debe verse como â€œun VPS sencilloâ€.

Debe verse como infraestructura seria de startup.

EstimaciÃ³n orientativa para un modelo 27B cuantizado:

```text
27B a 4-bit, contexto corto/medio:
18â€“24 GB de VRAM pueden bastar en algunos setups.

Objetivo mÃ¡s cÃ³modo de producciÃ³n:
32 GB de VRAM.

Contextos largos o mucha concurrencia:
40â€“80 GB de VRAM pueden volverse relevantes.
```

La conclusiÃ³n prÃ¡ctica:

> 7Bâ€“14B es el rango natural para una primera inferencia confidencial local. 27B es posible, pero probablemente como modo premium o fase posterior. 70B+ ya entra en una categorÃ­a mucho mÃ¡s cara y compleja.

### 30.4. El problema especial de las GPUs

La CPU confidencial es mÃ¡s madura que la GPU confidencial.

Pero los LLMs grandes suelen necesitar GPU para ser rÃ¡pidos y rentables.

Por eso el cuello de botella no es solo â€œÂ¿puede existir un enclave?â€, sino:

```text
- Â¿hay GPU confidencial disponible?
- Â¿hay atestaciÃ³n de GPU?
- Â¿el runtime soporta inferencia eficiente?
- Â¿quÃ© overhead introduce el modo confidencial?
- Â¿cuÃ¡nto cuesta mantener capacidad GPU reservada?
```

La tendencia del mercado apunta hacia **confidential AI** con GPUs protegidas, pero para una startup conviene no depender de eso en el MVP.

La estrategia mÃ¡s razonable:

```text
1. Usar APIs externas para mÃ¡xima calidad.
2. Reducir datos antes de enviar.
3. AÃ±adir enclave para orquestaciÃ³n sensible.
4. AÃ±adir modelos abiertos pequeÃ±os/medios dentro del enclave.
5. Reservar modelos 27B+ confidenciales para premium o enterprise.
```

### 30.5. Costes y esfuerzo aproximados

Para tener orden de magnitud:

#### MVP normal sin enclave

```text
Telegram / backend / LLM externo:
3â€“10 dÃ­as si la base ya existe.

PWA mÃ­nima:
2â€“4 semanas.

PWA con preview de privacidad y vault bÃ¡sico:
4â€“8 semanas.
```

Coste cloud inicial:

```text
decenas a pocos cientos de euros al mes,
si el trÃ¡fico es bajo y el coste principal es la API del LLM.
```

#### AÃ±adir enclave solo para orquestaciÃ³n sensible

EstimaciÃ³n de esfuerzo adicional:

```text
80â€“300 horas de ingenierÃ­a adicional.
2â€“8 semanas extra.
1 backend/security engineer competente.
```

Coste de uso:

```text
aproximadamente 1,2xâ€“3x sobre el coste compute normal,
no 100x.
```

Para una startup temprana, podrÃ­a ser algo como:

```text
+100 a +1.000 euros/mes al inicio,
segÃºn trÃ¡fico, cloud y arquitectura.
```

No es trivial, pero tampoco es ciencia ficciÃ³n.

#### Modelo abierto 7Bâ€“14B dentro de enclave

EstimaciÃ³n:

```text
startup-feasible;
probablemente bajo miles de euros/mes si hay uso real;
puede empezar como modo limitado, interno o premium;
requiere MLOps/inferencia mÃ¡s cuidadosa.
```

Es adecuado para:

```text
- clasificaciÃ³n;
- memory clerk;
- privacidad;
- resumen;
- razonamiento estructurado;
- respuestas patrimoniales guiadas por skills.
```

#### Modelo 27B dentro de enclave

EstimaciÃ³n:

```text
factible, pero ya no barato por defecto;
probablemente premium-tier;
necesita GPU/VRAM seria;
la concurrencia y el contexto largo cambian mucho el coste.
```

Orden de magnitud:

```text
miles de euros/mes si se mantiene infraestructura dedicada o uso relevante;
puede subir mÃ¡s si hay alta concurrencia, largos contextos o GPUs confidenciales caras.
```

La recomendaciÃ³n:

> No hacer del 27B confidencial el primer producto. Mantenerlo como fase premium/futura.

### 30.6. Estrategia hÃ­brida probable

La arquitectura mÃ¡s elegante a medio plazo puede ser hÃ­brida:

```text
Tareas muy sensibles y estructuradas
â†’ modelo abierto pequeÃ±o/medio dentro del enclave.

Preguntas complejas que requieren mÃ¡xima inteligencia
â†’ LLM externo, pero solo con contexto reducido y aprobado.

Clientes premium o enterprise
â†’ 27B dentro del enclave o inferencia confidencial dedicada.
```

Esto permite combinar:

```text
- privacidad fuerte donde mÃ¡s importa;
- calidad alta cuando el modelo externo aporta mucho;
- coste controlado;
- evoluciÃ³n gradual hacia soberanÃ­a tÃ©cnica.
```

La frase estratÃ©gica:

> La inteligencia debe acercarse al usuario; no obligar al usuario a desnudarse ante la inteligencia.

Y para Prevengen:

> Primero reducimos lo que sale. DespuÃ©s sellamos dÃ³nde se procesa. MÃ¡s adelante, llevamos tambiÃ©n el modelo dentro de la sala sellada.

### 30.7. Encaje en el roadmap de Prevengen

Roadmap tÃ©cnico refinado:

```text
Fase 1:
Telegram MVP + reducciÃ³n en servidor.

Fase 2:
PWA privada + reducciÃ³n local + vista previa.

Fase 3:
Wiki cifrada en cliente + diccionario privado local.

Fase 4:
Enclave de orquestaciÃ³n con atestaciÃ³n remota.

Fase 5:
Modelo abierto 7Bâ€“14B dentro del enclave para tareas sensibles.

Fase 6:
Modo premium con modelo 27B confidencial, si el coste y la demanda lo justifican.

Fase 7:
Modo local o soberano para usuarios de mÃ¡xima privacidad.
```

La idea final:

> El primer moat no es tener el modelo mÃ¡s potente. El primer moat es construir la sala mÃ¡s confiable. Luego, poco a poco, mÃ¡s inteligencia puede moverse dentro de esa sala.


## 31. Roadmap

### Fase 1 â€” Telegram MVP

- Bot de Telegram.
- Score de confidencialidad en servidor.
- ReducciÃ³n/anonimizaciÃ³n antes de enviar a la IA externa.
- AprobaciÃ³n del usuario cuando el riesgo sea alto.
- Promesa principal: proteger al cliente frente a exposiciÃ³n innecesaria ante modelos externos.

### Fase 2 â€” Modo Privado Web / PWA

- Interfaz privada de chat en web, idealmente como PWA instalable.
- CÃ¡lculo local del score de confidencialidad.
- AnonimizaciÃ³n basada en reglas en el dispositivo.
- SelecciÃ³n local de fragmentos relevantes de la wiki.
- ReducciÃ³n local de esos fragmentos antes de enviarlos.
- Vista previa: â€œesto es lo que se enviarÃ¡â€.
- Prevengen recibe solo el paquete reducido aprobado.
- Prevengen aÃ±ade instrucciones de producto, no wiki privada bruta.
- Open source de la capa de privacidad.
- Icono instalable en Android y escritorio.
- Posibles notificaciones o avisos de mensajes no leÃ­dos, sin depender de ello como funciÃ³n crÃ­tica.

### Fase 3 â€” Wiki cifrada en cliente

- Wiki visible y anonimizada.
- Identidad separada de memoria.
- Wiki cifrada en el dispositivo.
- RecuperaciÃ³n de memoria local.
- SelecciÃ³n local de fragmentos de wiki para cada consulta.
- Actualizaciones de memoria explÃ­citas: guardar, editar o ignorar.
- Principio: Copiloto no recuerda nada silenciosamente.
- La empresa no puede leer la memoria almacenada.

### Fase 4 â€” PWA madura / app-like

- Experiencia mÃ¡s parecida a una app nativa.
- Misma base web, pero instalable en mÃ³vil y escritorio.
- Mejor almacenamiento local.
- Mejor sensaciÃ³n de espacio privado.
- Mejor gestiÃ³n de notificaciones, privacidad local y experiencia mÃ³vil.

### Fase 5 â€” Inferencia confidencial premium

- Prompt cifrado a enclave seguro.
- Backend normal sin acceso a prompt ni respuesta.
- Modo para usuarios que requieren mÃ¡xima confianza.

### Fase 6 â€” Modo totalmente local

- Modo totalmente local para usuarios de mÃ¡xima privacidad.
- Menor calidad posible, pero mÃ¡xima privacidad.

## 32. DiferenciaciÃ³n frente a bancos y Big Tech

Frente a un banco:

> El banco puede tener buenos asesores, pero suele tener productos propios que vender.

Frente a Big Tech:

> Big Tech puede tener IA potente, pero su modelo depende de datos, ecosistemas, publicidad, compras o integraciÃ³n comercial.

Copiloto Relaciones debe decir:

> No vendo productos financieros.  
> No necesito saber mÃ¡s de lo necesario.  
> No quiero capturarte.  
> Quiero ayudarte a pensar mejor antes de decidir.

## 33. Frases simples para la web

```text
Tu relaciones no es una bÃºsqueda cualquiera.
```

```text
No preguntes decisiones importantes a una IA con incentivos opacos.
```

```text
Primero privacidad. Luego inteligencia.
```

```text
Un espacio privado para pensar antes de hablar con tu banco.
```

```text
Compara propuestas financieras sin exponer mÃ¡s datos de los necesarios.
```

```text
La memoria de la IA debe estar bajo tu control.
```

```text
Puedes ver, editar, exportar o borrar lo que el sistema recuerda.
```

```text
Para decisiones patrimoniales, la confianza importa tanto como la respuesta.
```

```text
Modo Telegram: te protegemos de la IA externa.
Modo Privado: te protegemos tambiÃ©n de nosotros.
```

```text
En Modo Privado, Prevengen ve el mismo caso anonimizado que la IA externa.
```

```text
No construimos otro Telegram. Construimos una sala privada para pensar decisiones patrimoniales importantes.
```

```text
La PWA es el puente natural: se siente como app, pero conserva transparencia web.
```

```text
El usuario ve y aprueba quÃ© sale de su dispositivo antes de enviar.
```

```text
No necesitamos una app nativa para empezar. Necesitamos una sala privada verificable.
```

```text
El prompt final puede montarse en Prevengen, pero el contexto privado debe llegar ya reducido desde el dispositivo.
```

```text
Copiloto no recuerda nada silenciosamente: propone, tÃº apruebas.
```

```text
El servidor no debe recibir la wiki completa si no la necesita.
```


```text
La PWA posee la verdad privada. Prevengen y la IA externa reciben solo la abstracciÃ³n Ãºtil aprobada por el usuario.
```

```text
No envÃ­es identificadores estables al modelo externo si no son necesarios.
```

```text
El riesgo se calcula sobre el paquete final: pregunta + contexto + fragmentos de wiki.
```

```text
La IA externa propone memoria; el usuario decide si se guarda.
```


```text
AtestaciÃ³n remota: no enviamos secretos hasta verificar quÃ© cÃ³digo se ejecuta dentro de la sala sellada.
```

```text
Primero reducimos lo que sale. DespuÃ©s sellamos dÃ³nde se procesa. MÃ¡s adelante, llevamos el modelo dentro de la sala sellada.
```

```text
La nube puede alojar la sala, pero no deberÃ­a poder abrirla.
```

```text
7Bâ€“14B dentro de enclave: modo privado factible. 27B dentro de enclave: modo premium posible.
```

## 34. Tesis final

Copiloto Relaciones debe ser una respuesta directa a la ansiedad que genera la IA generalista integrada en todo.

No compite con Google en comodidad.

Compite en confianza.

No promete saberlo todo.

Promete proteger mejor las preguntas que importan.

La versiÃ³n corta:

> Google es para lo rÃ¡pido.  
> Copiloto Relaciones es para lo importante.

La versiÃ³n mÃ¡s estratÃ©gica:

> Copiloto Relaciones es una IA independiente y confidencial para preparar decisiones patrimoniales importantes, reduciendo exposiciÃ³n de datos, conflictos de interÃ©s y dependencia de asesores con incentivos opacos.

La versiÃ³n mÃ¡s emocional:

> Un lugar protegido donde pensar sobre tu dinero, tu futuro y tu familia sin sentirte observado ni vendido.

