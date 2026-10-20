// sensor.ino - envia la distancia del sensor por el puerto serial
// Formato: un valor por linea. Sin mensajes de texto.
const int TRIG = 9;
const int ECHO = 10;
void setup() {
  Serial.begin(115200);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}
void loop() {
  // Enviar pulso
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIG, LOW);
  // Medir el tiempo de regreso
  long tiempo = pulseIn(ECHO, HIGH);
  // Convertir el tiempo a distancia en cm
  float distancia = tiempo * 0.0343 / 2.0;
  // Enviar SOLO el numero
  Serial.println(distancia);
  delay(100);
}