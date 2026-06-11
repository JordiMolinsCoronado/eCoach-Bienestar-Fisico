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


## 11. Wiki tokenizada y diccionario privado local

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


## 12. Flujo preciso de Fase 2 y riesgos a evitar

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



## 13. Competidores y hueco de mercado

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

## 14. Prevengen como metodologÃ­a transversal

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


## 15. Posicionamiento

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

## 16. Por quÃ© existe la oportunidad

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

## 17. Enemigo claro

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

## 18. Promesa del producto

Promesa funcional:

> Te ayudo a entender, ordenar y preparar tus decisiones patrimoniales sin exponerte innecesariamente.

Promesa emocional:

> Puedes pensar aquÃ­ sin sentir que estÃ¡s siendo observado, vendido o empujado.

Promesa Ã©tica:

> No gano dinero vendiÃ©ndote productos financieros. Mi trabajo es ayudarte a pensar mejor.

Promesa de control:

> Puedes ver, editar, exportar y borrar lo que el sistema recuerda.

## 19. Arquitectura de privacidad

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

## 20. Memoria visible y anonimizada

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

## 21. Confidencialidad antes de inteligencia

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

## 22. Modos de privacidad

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

## 23. Afirmaciones honestas

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

## 24. Control visible para el usuario

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

## 25. Soporte humano

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

## 26. MVP recomendado

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

## 27. Roadmap

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

## 28. DiferenciaciÃ³n frente a bancos y Big Tech

Frente a un banco:

> El banco puede tener buenos asesores, pero suele tener productos propios que vender.

Frente a Big Tech:

> Big Tech puede tener IA potente, pero su modelo depende de datos, ecosistemas, publicidad, compras o integraciÃ³n comercial.

Copiloto Relaciones debe decir:

> No vendo productos financieros.  
> No necesito saber mÃ¡s de lo necesario.  
> No quiero capturarte.  
> Quiero ayudarte a pensar mejor antes de decidir.

## 29. Frases simples para la web

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

## 30. Tesis final

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

