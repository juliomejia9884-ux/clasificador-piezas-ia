# leer_sensor.py - lee la distancia del HC-SR04 y grafica una ventana

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
        distancia = float(linea)
    except ValueError:
        continue

    valores.append(distancia)
    print(distancia, "cm")

ser.close()

print(f"Listas {len(valores)} muestras")

# Graficar los valores
plt.plot(valores)
plt.xlabel("Muestra")
plt.ylabel("Distancia (cm)")
plt.title("Señal del sensor HC-SR04")
plt.grid(True)

# Guardar la gráfica
plt.savefig("../figuras/senal.png")

# Mostrar la gráfica
plt.show()