# Bitacora del Proyecto
## SEMANA 1 - Encuadre y configuración del entorno

### Antes de la clase

Comenzamos con la planeacion de todo lo que haremos y se instalaron las cosas necesarias para realizar las actividades, se busca realizar las cosas de manera eficaz utilizando material adquirido, se configuraron los entornos y todo lo que se necesita

1. ¿Cuál es la diferencia entre programar la regla y aprender la regla? 
- Es de codigo que uno le pone y el otro de como de que aprende
2. ¿Cuál es tu dominio y cuáles son tus tres tipos de pieza?
- Clasificacion por tamaño (Chico, Mediano, Grande)
3. Describe el bucle de control de tu sistema: qué mide tu sensor, qué tiene que decidir el modelo y qué haría el actuador con cada uno de tus tres tipos.
- El HC-SR04 mide la distancia entre el sensor y la pieza. El modelo analiza esa medida para decidir si la pieza es Chica, Mediana o Grande.Después, el actuador realiza una acción diferente para cada tamaño: Chica → la desvía al área 1, Mediana → al área 2 y Grande → al área 3.

## SEMANA 2 
### BLOQUE 1
1. ¿Qué sensor vas a usar y qué tipo de salida tiene?
 - HC-SR04, sensor ultrasónico que tiene una salida digital, cuyo tiempo permite calcular la distancia.
2. Tres líneas de ejemplo tal como se van a ver saliendo de tu Arduino, con valores plausibles para tu caso.
  - 5.2
  - 10.4
  - 16.8
3. Por qué el Arduino no puede mandar Serial.println("Leyendo...").
 - El Arduino no puede mandar solo Serial.println("Leyendo...") porque el modelo necesita datos numéricos del sensor para poder analizar la distancia y clasificar la pieza como chica, mediana o grande.

###  BLOQUE 2
1. ¿Cuánto tarda tu pieza en cruzar frente al sensor?
- Aproximadamente 1 segundo.
2. ¿Qué delay() eliges para tener al menos 20 muestras del evento?
- Elegiría un delay(50) ms, porque:
1000 ms ÷ 50 ms = 20 muestras.
3. ¿Cuántas muestras te da eso mientras la pieza pasa?
- Me da aproximadamente 20 muestras mientras la pieza cruza frente al sensor.b
## SEMANA 3 
### BLOQUE 1
1. Las columnas exactas de tu datos.csv, con el nombre de cada una y qué guarda.
- Tres
2. Tus tres etiquetas, escritas tal como van a aparecer en el archivo (una palabra, minúsculas, sin acentos).
- Chico Mediano Grande
3. Cinco filas de ejemplo de tu tabla, con valores plausibles para tu sensor.
- 5.2,chico
- 6.1,chico
- 10.4,mediano
- 11.2,mediano
- 16.5,grande

### BLOQUE 2
1. Cuántas ventanas por clase vas a capturar.
- Capturaré 30 ventanas por cada clase, para un total de 90 ventanas. Las clases serán chico, mediano y grande.
2. En qué orden.
- chico, mediano, grande, y repetiré el orden hasta completar las 30 ventanas de cada clase.
3. Cómo vas a mantener pareja la velocidad de la mano, en concreto: qué vas a marcar, medir o fijar.
- Marcaré un punto de inicio y uno de final en la mesa, usando siempre el mismo recorrido. Intentaré mantener una velocidad aproximada de un segundo por recorrido.
4. A qué distancia del sensor va a pasar la pieza.
- Mantendré la pieza aproximadamente a 5 cm del sensor HC-SR04 durante el recorrido, utilizando una guía para mantener una posición constante.

## SEMANA 4 
### BLOQUE 1
1. Qué tipo de ruido ves en tu señal y de dónde crees que viene.
- Se observa principalmente ruido aleatorio o pequeñas variaciones en la señal. Puede venir de cambios en la medición del sensor ultrasónico, objetos que reflejan el sonido, interferencias o pequeñas variaciones en el tiempo de lectura.
2. Qué rango físico tiene tu sensor y qué valores estás descartando por imposibles.
- El sensor ultrasónico HC-SR04 tiene un rango aproximado de 2 a 400 cm. Por eso se descartan los valores menores a 2 cm y mayores a 400 cm, ya que están fuera de su rango de medición.
3. Qué tamaño de filtro elegiste y por qué, en relación con la duración de tu evento.
- Elegí un filtro de media móvil de 5 muestras porque permite reducir el ruido de la señal sin afectar demasiado los cambios del evento. El tamaño del filtro es pequeño en comparación con la duración del evento, por lo que conserva sus características principales.

### BLOQUE 2
1. ¿Cuánto se movió tu línea base entre la primera y la última ventana de la sesión?
- En la gráfica de la ventana 0 se observa que la señal original comienza aproximadamente en 28 cm y presenta variaciones durante la captura. Después de aplicar el filtrado y la corrección de línea base, se reducen las variaciones de la señal. Sin embargo, para determinar cuánto se movió la línea base entre la primera y la última ventana, es necesario comparar ambas capturas, ya que la gráfica únicamente muestra la ventana 0.

2. ¿Qué normalización elegiste y por qué?
- Elegí la normalización Min-Max, porque permite transformar los valores de la señal a un rango de 0 a 1. Esto facilita la comparación de las mediciones del sensor ultrasónico y permite trabajar con datos en una escala uniforme, lo que será útil para el entrenamiento del modelo de inteligencia artificial.

3. Al comparar antes y después, ¿se parecen más entre sí las ventanas de una misma clase?
- Al comparar las gráficas antes y después de la limpieza, se observa que la señal procesada presenta menos variaciones bruscas y una forma más suavizada. Esto permite identificar mejor el comportamiento de la señal. Aunque se espera que las ventanas de una misma clase sean más consistentes después del procesamiento, sería necesario comparar varias ventanas de la misma clase para confirmarlo.

### Avance del proyecto

Se comenzo con todo lo que tenemos que ver para crear carpetas, guardarlas de forma segura, lo commit y guardar.

Prueba agregar
Este es el procedimiento para hacer push:
- Para hacer push primero edito
- Luego hago git add .
- Luego git commit
- Luego git push

