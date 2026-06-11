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

## 3. Posicionamiento

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

## 4. Por quÃ© existe la oportunidad

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

## 5. Enemigo claro

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

## 6. Promesa del producto

Promesa funcional:

> Te ayudo a entender, ordenar y preparar tus decisiones patrimoniales sin exponerte innecesariamente.

Promesa emocional:

> Puedes pensar aquÃ­ sin sentir que estÃ¡s siendo observado, vendido o empujado.

Promesa Ã©tica:

> No gano dinero vendiÃ©ndote productos financieros. Mi trabajo es ayudarte a pensar mejor.

Promesa de control:

> Puedes ver, editar, exportar y borrar lo que el sistema recuerda.

## 7. Arquitectura de privacidad

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

## 8. Memoria visible y anonimizada

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

## 9. Confidencialidad antes de inteligencia

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

## 10. Modos de privacidad

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

## 11. Afirmaciones honestas

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

## 12. Control visible para el usuario

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

## 13. Soporte humano

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

## 14. MVP recomendado

Primera versiÃ³n:

```text
1. Bot de Telegram.
2. DetecciÃ³n de riesgo de confidencialidad.
3. Umbral de revisiÃ³n manual.
4. AnonimizaciÃ³n/reducciÃ³n de prompts de alto riesgo.
5. AprobaciÃ³n del usuario antes de enviar contenido sensible.
6. Respuestas estructuradas.
7. Logs bÃ¡sicos.
8. Wiki visible y editable.
9. Comandos /privacy, /export, /delete_all, /forget_topic.
```

La primera ventaja competitiva no debe ser tener â€œla mejor IAâ€.

Debe ser:

> La IA patrimonial que trata tus datos como algo sagrado.

## 15. Roadmap

### Fase 1

- Wiki visible y anonimizada.
- Identidad separada de memoria.
- Solo fragmentos relevantes enviados al modelo.
- RevisiÃ³n opt-in de testers.

### Fase 2

- DetecciÃ³n local de PII.
- AnonimizaciÃ³n basada en reglas.
- Vista previa: â€œesto es lo que se enviarÃ¡ a la IAâ€.

### Fase 3

- Wiki cifrada en cliente.
- RecuperaciÃ³n de memoria local.
- Actualizaciones de memoria propuestas localmente.
- La empresa no puede leer la memoria almacenada.

### Fase 4

- Inferencia confidencial premium.
- Prompt cifrado a enclave seguro.
- Backend normal sin acceso a prompt ni respuesta.

### Fase 5

- Modo totalmente local para usuarios de mÃ¡xima privacidad.

## 16. DiferenciaciÃ³n frente a bancos y Big Tech

Frente a un banco:

> El banco puede tener buenos asesores, pero suele tener productos propios que vender.

Frente a Big Tech:

> Big Tech puede tener IA potente, pero su modelo depende de datos, ecosistemas, publicidad, compras o integraciÃ³n comercial.

Copiloto Relaciones debe decir:

> No vendo productos financieros.  
> No necesito saber mÃ¡s de lo necesario.  
> No quiero capturarte.  
> Quiero ayudarte a pensar mejor antes de decidir.

## 17. Frases simples para la web

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

## 18. Tesis final

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

