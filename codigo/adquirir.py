# adquirir.py - captura ventanas etiquetadas y las guarda en datos/datos.csv
import serial
import time
import csv
import os
import pandas as pd

PUERTO = 'COM3'          # el tuyo puede ser otro: COM4, COM5...
BAUDIOS = 9600
N_MUESTRAS = 200          # largo de cada ventana
ARCHIVO = 'datos/datos.csv'

etiqueta = input("Etiqueta de esta pieza (chico/mediano/grande): ")
n_ventanas = int(input("Cuantas ventanas vas a capturar: "))

ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)             # el Arduino se reinicia al abrir el puerto

# TODO 1: si el archivo esta vacio, escribe primero la fila de encabezados
#         ventana,t,valor,etiqueta
archivo_existe = os.path.exists(ARCHIVO) and os.path.getsize(ARCHIVO) > 0

# 'a' = append: no borra lo que ya habias capturado antes
archivo = open(ARCHIVO, 'a', newline='')
escritor = csv.writer(archivo)

if not archivo_existe:
    escritor.writerow(['ventana', 't', 'valor', 'etiqueta'])

# TODO 2: averigua en que numero de ventana te quedaste la vez pasada
#         pista: lee el CSV con pandas y toma el maximo de la columna 'ventana'
if archivo_existe:
    datos_previos = pd.read_csv(ARCHIVO)
    ventana = datos_previos['ventana'].max() + 1
else:
    ventana = 0

for i in range(n_ventanas):
    input(f"\nVentana {ventana} ({etiqueta}). Enter y pasa la pieza...")
    ser.reset_input_buffer()          # tira lo que se acumulo mientras esperabas

    t = 0
    while t < N_MUESTRAS:
        linea = ser.readline().decode('utf-8').strip()
        try:
            valor = float(linea)
        except ValueError:
            continue
        escritor.writerow([ventana, t, valor, etiqueta])
        t += 1

    print(f"  {N_MUESTRAS} muestras guardadas")
    ventana += 1

archivo.close()
ser.close()
print(f"\nListo. Datos en {ARCHIVO}")