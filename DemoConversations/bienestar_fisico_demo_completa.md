# eCoach Bienestar Físico — Demo completa

## Archivos

Usar exactamente:

```text
Analisi_Sang_Cerba_ANONIMIZADO_20250808.pdf
genome_APOE_ANONIMIZADO.txt
```

No usar el genoma completo de 16 MB.

## 0. Reinicio

```text
/reset_client
```

## 1. Mensaje inicial de Laura

```text
Me llamo Laura, tengo 48 años y vivo en Barcelona.

Mido 1,65 m y peso 84,4 kg. Quiero perder peso.

He ido al médico porque en la analítica tengo el colesterol un poco elevado. El médico me ha dicho que no es preocupante, pero que debería hacer más ejercicio, comer mejor y cambiar algunos hábitos.

Sé que tiene razón, pero la visita duró solo quince minutos y no pudimos convertirlo en un plan concreto.

Tengo la analítica reciente y también los datos de una prueba genética que hice hace tiempo para conocer mis orígenes. ¿Puedo subirlos?
```

## 2. Subir documentos

Subir los dos archivos. Debe aparecer:

```text
Documentos recibidos en esta sesión: 2.
```

Pulsa:

```text
Analizar documentos de salud
```

## 3. Diagnóstico documental

Debe incluir:

- LDL 3,09 mmol/L / 119 mg/dL.
- Glucosa 5,4 mmol/L dentro de rango.
- Creatinina 100 µmol/L.
- eGFR 76 mL/min/1,73 m².
- Urea 8,8 mmol/L.
- rs429358 CT + rs7412 CC, compatible con APOE ε3/ε4.
- APOE como susceptibilidad, no diagnóstico ni destino.
- Limitación de prueba directa al consumidor.
- Llevar LDL y APOE juntos al médico.

No debe incluir todavía preguntas para el médico ni plan de hábitos.

Pulsa:

```text
Crear Mi Plan
```

## 4. Mi Plan

Debe incluir:

- caminar cada día;
- mínimo para días difíciles;
- fuerza dos veces por semana;
- proteína y fibra;
- reducir bebidas azucaradas y ultraprocesados;
- sueño, hidratación, peso y cintura;
- IMC aproximado 31;
- semaglutida y tirzepatida;
- resultados medios de ensayos como contexto, no predicción;
- protección de masa muscular;
- preguntas para el médico.

Al final pulsa:

```text
Activar seguimiento de demo — en 1 minuto
```

Debe confirmar que el seguimiento llegará aproximadamente en un minuto.

## 5. Mensaje proactivo

Esperar uno o dos minutos sin escribir nada.

Debe mencionar:

- sueño peor que la línea base;
- frecuencia cardiaca en reposo más alta;
- HRV más baja;
- ansiedad relacional como posible causa;
- síntomas de alarma;
- posibilidad de guardar ECG del wearable;
- revisión médica si persiste o hay síntomas preocupantes.

## 6. Respuesta de Laura

```text
Sí, creo que se debe sobre todo a la ansiedad que me está generando la relación con ese hombre. He dormido mal y he estado bastante activada.

No tengo dolor en el pecho, falta de aire, fiebre ni mareos. Alguna vez noto el corazón más rápido, pero creo que coincide con los momentos de ansiedad.

Aun así, prefiero no darlo por supuesto. Voy a seguir observando el sueño, la frecuencia cardiaca en reposo y la HRV, y estoy de acuerdo en comentarlo con el médico.

También quiero llevarle el LDL, el resultado APOE ε3/ε4 y preguntarle por semaglutida o tirzepatida, teniendo en cuenta que mido 1,65 m y peso 84,4 kg.

Tengo cita con el médico el 22 de junio de 2026 a las 10:30. Recuérdame el día anterior a las 08:00 que prepare lo que tengo que llevar y preguntar.
```

## 7. Verificar recordatorio

```text
/followups
```

Debe aparecer:

```text
2026-06-21 08:00
```

## Final

```text
eCoach Bienestar Físico no es un médico de IA. Es una capa de agencia diaria entre consultas: integra datos, ayuda a actuar, detecta cambios y prepara mejor la conversación clínica.
```
