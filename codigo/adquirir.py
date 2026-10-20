
# adquirir.py - Captura ventanas etiquetadas
import serial
import time
import csv
import os
import pandas as pd

PUERTO = 'COM3'
BAUDIOS = 115200
N_MUESTRAS = 200
ARCHIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'datos',
    'datos.csv'
)

# Crear la carpeta datos si no existe
os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)

# Comprobar si el archivo existe y tiene contenido
archivo_existe = (
    os.path.exists(ARCHIVO)
    and os.path.getsize(ARCHIVO) > 0
)

# Crear archivo CSV con encabezados si no existe
if not archivo_existe:
    with open(ARCHIVO, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['ventana', 't', 'valor', 'etiqueta'])
    print("Archivo datos.csv creado correctamente.")

# Recuperar el número de la última ventana
datos_previos = pd.read_csv(ARCHIVO)

if not datos_previos.empty:
    ventana = int(datos_previos['ventana'].max()) + 1
else:
    ventana = 0

# Solicitar información
etiqueta = input(
    "Etiqueta de esta pieza (chico/mediano/grande): "
).strip().lower()

n_ventanas = int(input(
    "Cuantas ventanas vas a capturar: "
))

# Conectar con Arduino
ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)

try:
    with open(ARCHIVO, 'a', newline='') as archivo:
        escritor = csv.writer(archivo)

        for i in range(n_ventanas):
            input(
                f"\nVentana {ventana} ({etiqueta}). "
                "Enter y pasa la pieza..."
            )

            ser.reset_input_buffer()

            t = 0
            while t < N_MUESTRAS:
                linea = ser.readline().decode(
                    'utf-8', errors='ignore'
                ).strip()

                try:
                    valor = float(linea)
                except ValueError:
                    continue

                escritor.writerow([
                    ventana, t, valor, etiqueta
                ])
                t += 1

            archivo.flush()

            print(f"  {N_MUESTRAS} muestras guardadas")
            ventana += 1

finally:
    ser.close()

print(f"\nListo. Datos guardados en {ARCHIVO}")
