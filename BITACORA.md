# Bitacora del Proyecto
## Semana 1 - Encuadre y configuración del entorno

### Antes de la clase

Comenzamos con la planeacion de todo lo que haremos y se instalaron las cosas necesarias para realizar las actividades, se busca realizar las cosas de manera eficaz utilizando material adquirido, se configuraron los entornos y todo lo que se necesita

- ¿Cuál es la diferencia entre programar la regla y aprender la regla? 
 Es de codigo que uno le pone y el otro de como de que aprende
- ¿Cuál es tu dominio y cuáles son tus tres tipos de pieza?
 Clasificacion por tamaño (Chico, Mediano, Grande)
- Describe el bucle de control de tu sistema: qué mide tu sensor, qué tiene que decidir el modelo y qué haría el actuador con cada uno de tus tres tipos.
El HC-SR04 mide la distancia entre el sensor y la pieza. El modelo analiza esa medida para decidir si la pieza es Chica, Mediana o Grande.Después, el actuador realiza una acción diferente para cada tamaño: Chica → la desvía al área 1, Mediana → al área 2 y Grande → al área 3.
1. ¿Qué sensor vas a usar y qué tipo de salida tiene?
 HC-SR04, sensor ultrasónico que tiene una salida digital, cuyo tiempo permite calcular la distancia.
2. Tres líneas de ejemplo tal como se van a ver saliendo de tu Arduino, con valores plausibles para tu caso.
  - Tiempo: 300 us   Distancia: 5.2 cm, Tamaño: Chico
  - Tiempo: 600 us   Distancia: 10.4 cm, Tamaño: Mediano
  - Tiempo: 1000 us  Distancia: 16.8 cm, Tamaño: Grande
3. Por qué el Arduino no puede mandar Serial.println("Leyendo...").
 El Arduino no puede mandar solo Serial.println("Leyendo...") porque el modelo necesita datos numéricos del sensor para poder analizar la distancia y clasificar la pieza como chica, mediana o grande.


### Avance del proyecto

Se comenzo con todo lo que tenemos que ver para crear carpetas, guardarlas de forma segura, lo commit y guardar.

Prueba agregar
Este es el procedimiento para hacer push:
- Para hacer push primero edito
- Luego hago git add .
- Luego git commit
- Luego git push

