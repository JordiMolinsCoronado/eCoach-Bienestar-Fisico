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


## 2. Idea clave para clientes: Prevengen separa a la persona del modelo

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

## 3. DistinciÃ³n esencial: proteger del modelo externo vs proteger tambiÃ©n de Prevengen

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

## 4. Verificabilidad: no solo prometer, sino mostrar quÃ© se envÃ­a

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

## 5. Open source de la capa de privacidad

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

## 6. No necesitamos construir â€œotro Telegramâ€

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


## 7. Por quÃ© una PWA puede ser la soluciÃ³n ideal

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

## 8. Por quÃ© una app nativa es mÃ¡s compleja

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



## 9. Punto crÃ­tico: dÃ³nde se monta el prompt final

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

## 10. ActualizaciÃ³n de la wiki: no recordar silenciosamente

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


## 11. Posicionamiento

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

## 12. Por quÃ© existe la oportunidad

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

## 13. Enemigo claro

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

## 14. Promesa del producto

Promesa funcional:

> Te ayudo a entender, ordenar y preparar tus decisiones patrimoniales sin exponerte innecesariamente.

Promesa emocional:

> Puedes pensar aquÃ­ sin sentir que estÃ¡s siendo observado, vendido o empujado.

Promesa Ã©tica:

> No gano dinero vendiÃ©ndote productos financieros. Mi trabajo es ayudarte a pensar mejor.

Promesa de control:

> Puedes ver, editar, exportar y borrar lo que el sistema recuerda.

## 15. Arquitectura de privacidad

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

## 16. Memoria visible y anonimizada

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

## 17. Confidencialidad antes de inteligencia

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

## 18. Modos de privacidad

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

## 19. Afirmaciones honestas

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

## 20. Control visible para el usuario

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

## 21. Soporte humano

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

## 22. MVP recomendado

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

## 23. Roadmap

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

## 24. DiferenciaciÃ³n frente a bancos y Big Tech

Frente a un banco:

> El banco puede tener buenos asesores, pero suele tener productos propios que vender.

Frente a Big Tech:

> Big Tech puede tener IA potente, pero su modelo depende de datos, ecosistemas, publicidad, compras o integraciÃ³n comercial.

Copiloto Relaciones debe decir:

> No vendo productos financieros.  
> No necesito saber mÃ¡s de lo necesario.  
> No quiero capturarte.  
> Quiero ayudarte a pensar mejor antes de decidir.

## 25. Frases simples para la web

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

## 26. Tesis final

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

