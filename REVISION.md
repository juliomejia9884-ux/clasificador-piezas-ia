# Retroalimentacion

Esto lo llena tu asesor despues de cada revision de avances (semanas 9, 14 y
17). Lo ves haciendo un `git pull` normal de tu repositorio. No lo edites:
crece con una seccion nueva en cada revision, las anteriores no se borran.

Los niveles son los de la rubrica de `evaluacion/individual`: **Excelente**,
**Bueno**, **Suficiente**, **Insuficiente**.

Evidencias, en este curso, es tu codigo en `codigo/`, tus datos en `datos/`,
tus figuras en `figuras/` y la demo del bucle de control.

---

### Nota rápida (2026-09-14) - s02
Tus tres líneas de ejemplo del bloque 1 mezclan texto con el dato (`Tiempo: 300 us   Distancia: 5.2 cm, Tamaño: Chico`), aunque tu propia respuesta a la pregunta 3 explica bien por qué el Arduino no debe mandar texto. Cuando lo cargues el miércoles, la línea real que mande tu `sensor.ino` debe ser solo el número. Aparte, tu `sensor.ino` quedó guardado en `codigo/sensor/sensor.ino` en vez de `codigo/sensor.ino`: conviene moverlo antes de que la ruta se use en otro script.

### Nota rápida (2026-09-14) - s03
En el bloque 1 de la semana 3, la pregunta de las columnas de `datos.csv` quedó contestada solo con "Tres" (sin decir cuáles), y el ejemplo de "cinco filas" que pusiste (`5.2,chico`) tiene dos columnas, no las cuatro (`ventana,t,valor,etiqueta`) que pide el formato. No hay carpeta `datos/` en tu repositorio, así que probablemente esto quedó en la parte de diseño y todavía no hiciste la captura; la semana 4 ya la brincaste sin datos que limpiar. Vale la pena volver al bloque 1 de esta semana antes de seguir, porque si el formato de columnas no queda claro ahora, cuesta más corregirlo después con datos ya capturados. Aparte, `sensor.ino` sigue en `codigo/sensor/sensor.ino` en vez de `codigo/sensor.ino`, el mismo problema que ya se comentó la semana pasada.

### Nota rápida (2026-09-14) - s04
Esto es más grave de lo que parece a primera vista: tu repositorio no tiene carpeta `datos/` (ni `datos.csv` ni nada), el mismo hueco que ya te había comentado la semana pasada. Tu `codigo/limpiar.py` está bien escrito (filtro por rango, media móvil por ventana con `groupby`, manejo correcto de los NaN de las orillas), pero como no existe `datos/datos.csv` no puede haberse ejecutado nunca sobre datos reales: por ahora es código de plantilla, no una limpieza real. Por eso no hay bloque 2 ni `datos_limpios.csv`, y el "Avance del proyecto" de tu bitácora no describe qué le hiciste a tu señal (solo menciona haber creado carpetas). Además `sensor.ino` sigue en `codigo/sensor/sensor.ino` en vez de `codigo/sensor.ino`, lo mismo que se comentó la semana pasada. Lo más urgente ahora es volver a la semana 3: capturar y subir tu `datos.csv` real, porque sin eso las semanas 4, 5 y 6 no tienen sobre qué trabajar.

### Nota rápida (2026-09-21) - s05
No veo commits de la semana 05 (`s05 bloque 1`/`s05 bloque 2`). Si tuviste un problema, cuéntamelo para que quede en la bitácora.

### Nota rápida (2026-10-19) - s06
No veo commits de la semana 06 (`s06 bloque 1`/`s06 bloque 2`). Si tuviste un problema, cuéntamelo para que quede en la bitácora.

### Nota rápida (2026-10-19) - s07
Veo tu commit del bloque 1 de la semana 2, bien que te estés poniendo al día. De la semana 07 todavía no veo commits (`s07 bloque 1`/`s07 bloque 2`). Si tuviste un problema, cuéntamelo para que quede en la bitácora.
