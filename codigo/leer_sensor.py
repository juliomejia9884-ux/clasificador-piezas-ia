# leer_sensor.py - lee la señal del sensor y grafica una ventana
import serial
import time
import matplotlib.pyplot as plt

PUERTO = 'COM3'
BAUDIOS = 115200
N_MUESTRAS = 200

ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)

valores = []
print("Leyendo... pasa la pieza frente al sensor")

while len(valores) < N_MUESTRAS:
    linea = ser.readline().decode('utf-8').strip()
    try:
        valor = float(linea)
    except ValueError:
        continue
    valores.append(valor)
    print(valor)

ser.close()
print(f"Listas {len(valores)} muestras")

# Graficar los valores
plt.plot(valores)
plt.xlabel("Muestra")
plt.ylabel("Valor del sensor")
plt.title("Señal del sensor TCRT5000")
plt.grid(True)

# Guardar la gráfica
plt.savefig("../figuras/senal.png")

# Mostrar la gráfica
plt.show()