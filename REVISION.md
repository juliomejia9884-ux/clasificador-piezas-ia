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
