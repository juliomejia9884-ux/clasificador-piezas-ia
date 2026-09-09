// sensor.ino - envia la lectura del sensor ultrasonico por el puerto serial
// Formato: un valor por linea. Sin mensajes de texto.

const int PIN_TRIG = 7;
const int PIN_ECHO = 6;

void setup() {
  Serial.begin(9600);

  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
}

void loop() {
  // Generar pulso de disparo
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  // Medir el tiempo que tarda en regresar el pulso
  long duracion = pulseIn(PIN_ECHO, HIGH);

  // Convertir el tiempo a distancia en centímetros
  int distancia = duracion * 0.0343 / 2;

  // Enviar solamente el valor
  Serial.println(distancia);

  delay(10);  // 100 muestras por segundo aproximadamente
}