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

## SEMANA 5 
### BLOQUE 1
| Característica | ¿Por qué debería distinguir mis clases? |
|---|---|
| Media | Permite conocer la distancia promedio detectada por el sensor durante el paso de cada pieza. |
| Desviación estándar | Ayuda a identificar las variaciones de distancia que se producen durante la detección. |
| Mínimo | Identifica la menor distancia registrada, que puede cambiar dependiendo del tamaño y posición de la pieza. |
| Máximo | Permite conocer la distancia máxima registrada durante cada ventana. |
| Rango | Mide la diferencia entre el valor máximo y mínimo, ayudando a comparar los cambios de distancia. |
| Duración del evento | Permite conocer cuántas muestras permanece una pieza frente al sensor, lo que podría ayudar a distinguir piezas chicas, medianas y grandes. |

### BLOQUE 2  
1. ¿Cuántas filas y cuántas columnas quedó tu features.csv, y por qué ese número de filas?
- Mi archivo features.csv contiene 8 columnas y al menos 8 filas de datos. Cada fila representa una ventana capturada por el sensor ultrasónico y cada columna contiene una característica calculada o su identificación. En la gráfica se observan 8 puntos de la clase grande. Para confirmar el número exacto de filas, es necesario revisar el archivo CSV.

2. ¿Qué par de características separa mejor tus clases, con la gráfica que lo muestra?
- Seleccioné las características de rango y duración del evento, representadas en la gráfica features.png. Se observan diferencias entre las mediciones de las piezas grandes, pero todavía no puedo determinar si estas características separan correctamente las tres clases, porque únicamente aparecen datos de la clase grande.

3. Si hay dos clases que se encimen, ¿cuáles y qué vas a hacer?
- Por el momento no puedo identificar qué clases se enciman, ya que la gráfica solamente muestra la clase grande. Para comprobarlo, necesito capturar y procesar también las piezas chicas y medianas. Después compararé sus características y, si existe un traslape, revisaré el umbral de detección y otras características que permitan diferenciarlas mejor.

## SEMANA 6
### BLOQUE 1
### Semana 6 - Características en el dominio de la frecuencia

### Antes de la clase
1. Frecuencia de muestreo (fs)
- Se utiliza un sensor ultrasónico conectado a Arduino. El programa contiene un retardo de 100 milisegundos entre mediciones, por lo que se estima una frecuencia de muestreo máxima aproximada de 10 Hz. La frecuencia real puede ser menor debido al tiempo que tarda el sensor en realizar cada medición.

2. Frecuencia de Nyquist
- La frecuencia de Nyquist se calcula dividiendo la frecuencia de muestreo entre dos.
fN = 10 / 2 = 5 Hz
Se obtiene un valor aproximado máximo de 5 Hz. Esto significa que las frecuencias superiores a ese límite no pueden representarse correctamente con dicho muestreo y pueden producir aliasing.

3. Resolución en frecuencia
- Se identificaron 8 ventanas con un promedio de 194.875 muestras por ventana. Para el cálculo se utiliza un tamaño representativo de 195 muestras.
Δf = 10 / 195 = 0.0513 Hz
La resolución estimada es de aproximadamente 0.0513 Hz. Este resultado deberá verificarse con la frecuencia de muestreo real.

4. Predicción sobre la separación de clases
- Considero que las características en frecuencia podrían aportar información adicional para distinguir los diferentes tipos de piezas. Sin embargo, debido a que el sensor ultrasónico mide principalmente cambios de distancia durante el paso de las piezas, es posible que las características del dominio del tiempo sean más útiles. Esto se comprobará mediante el análisis de los espectros.

### BLOQUE 2 
1. Frecuencia dominante y sentido físico
- La frecuencia dominante representa la frecuencia en la que se presenta la mayor magnitud de la señal del sensor HC-SR04. En este proyecto, la frecuencia dominante permite identificar las principales variaciones que ocurren cuando una pieza pasa frente al sensor.
Debido a que el proceso de detección es relativamente lento, se espera que las frecuencias dominantes sean bajas. Esto tiene sentido físico porque el sensor detecta cambios de distancia conforme las piezas pasan frente a él, en lugar de medir vibraciones de alta frecuencia.
2. ¿Las características de frecuencia separan las clases?
- Las características espectrales permiten analizar el comportamiento de la señal para las tres clases: chico, mediano y grande.
Sin embargo, estas características no necesariamente permiten distinguir las clases por sí solas, ya que el sensor HC-SR04 mide principalmente cambios de distancia y no las dimensiones directamente mediante frecuencias.
Para comprobarlo, se utiliza la gráfica espectro.png, donde se comparan las frecuencias de una ventana de cada clase. Si los espectros presentan formas y magnitudes similares, significa que las características de frecuencia no ofrecen una separación clara entre las piezas.
3. Decisión final
- Por el momento, se conservarán las características espectrales para realizar las pruebas de comparación con las características del dominio del tiempo.
Sin embargo, si después de analizar las gráficas se observa que no existe una diferencia importante entre las clases, se eliminarán de features.csv, ya que no estarían aportando información útil para mejorar la clasificación.
Se dará prioridad a las características que permitan distinguir correctamente las piezas chicas, medianas y grandes.

## SEMANA 7 
### BLOQUE 1

**1. ¿Con cuántos ejemplos voy a entrenar y con cuántos voy a probar?**
- Actualmente mi dataset cuenta con 114 ventanas. Voy a utilizar aproximadamente el 80% de los datos para entrenar el modelo y el 20% para probarlo.
- Datos de entrenamiento: 91 ventanas.
- Datos de prueba: 23 ventanas.
De esta manera, el modelo podrá aprender con la mayoría de los ejemplos y después comprobaré qué tan bien clasifica datos que no ha visto anteriormente.

**2. ¿Qué algoritmo elijo para empezar y por qué?**
- Para comenzar voy a utilizar un árbol de decisión (Decision Tree), porque es un algoritmo sencillo de entender y permite clasificar mis piezas de acuerdo con sus características. En mi proyecto necesito distinguir tres tamaños: chico, mediano y grande. Además, puedo observar las decisiones que toma el modelo para realizar la clasificación.

**3. ¿Por qué un modelo que acierta 100% en los datos de entrenamiento puede ser inútil?**
- Porque puede estar memorizando los datos con los que fue entrenado en lugar de aprender a identificar correctamente las características de cada clase. Esto provoca que cuando recibe datos nuevos pueda equivocarse. Por eso es importante probar el modelo con datos que no haya utilizado durante el entrenamiento.

### BLOQUE 2 
**1. ¿Cuál fue mi exactitud en el conjunto de prueba?**

- Mi modelo KNN obtuvo una exactitud del 56.52% en el conjunto de prueba. Esto significa que clasificó correctamente 13 de las 23 muestras evaluadas. El resultado indica que todavía hay aspectos que se pueden mejorar para conseguir una clasificación más precisa.

**2. ¿Qué par de clases se confunde más?**

- Las clases que más se confunden son chico y grande. En la matriz de confusión se observa que algunas piezas grandes fueron clasificadas como chicas y también algunas piezas chicas fueron clasificadas como grandes. Esto puede deberse a que sus características no tienen una separación suficientemente clara para el modelo.

**3. ¿El resultado coincidió con lo que predije en la semana 6?**

- Los resultados muestran que existe dificultad para separar correctamente algunas clases. Esto permite relacionar el comportamiento del modelo con el análisis de las características realizado en la semana 6. También me permite identificar que necesito mejorar la separación de las clases para conseguir mejores resultados en la clasificación.

### Avance del proyecto

Se comenzo con todo lo que tenemos que ver para crear carpetas, guardarlas de forma segura, lo commit y guardar.

Prueba agregar
Este es el procedimiento para hacer push:
- Para hacer push primero edito
- Luego hago git add .
- Luego git commit
- Luego git push

