
# features.py - Semana 5
# Extraccion de caracteristicas en el dominio del tiempo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# RUTAS DEL PROYECTO
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CARPETA_DATOS = os.path.join(BASE_DIR, "datos")
CARPETA_FIGURAS = os.path.join(BASE_DIR, "figuras")

os.makedirs(CARPETA_DATOS, exist_ok=True)
os.makedirs(CARPETA_FIGURAS, exist_ok=True)

ARCHIVO_ENTRADA = os.path.join(
    CARPETA_DATOS, "datos_limpios.csv"
)

ARCHIVO_SALIDA = os.path.join(
    CARPETA_DATOS, "features.csv"
)

ARCHIVO_GRAFICA = os.path.join(
    CARPETA_FIGURAS, "features.png"
)

# ==========================================
# CARGAR DATOS LIMPIOS
# ==========================================

if not os.path.exists(ARCHIVO_ENTRADA):
    raise FileNotFoundError(
        "No se encontro datos_limpios.csv"
    )

datos = pd.read_csv(ARCHIVO_ENTRADA)

COLUMNA = "valor_corregido"

columnas = ["ventana", "t", "etiqueta", COLUMNA]

if not all(c in datos.columns for c in columnas):
    raise ValueError(
        "Faltan columnas en datos_limpios.csv. "
        "Ejecuta primero limpiar.py"
    )

datos = datos.dropna(subset=columnas).copy()

if datos.empty:
    raise ValueError("No hay datos para procesar.")

# ==========================================
# TODO 1: DURACION DEL EVENTO
# ==========================================

# Umbral provisional de 5 cm
UMBRAL = 5.0

filas = []

for ventana, g in datos.groupby("ventana"):

    g = g.sort_values("t")

    x = g[COLUMNA].to_numpy(dtype=float)

    etiqueta = g["etiqueta"].iloc[0]

    duracion = np.sum(np.abs(x) > UMBRAL)

    # ======================================
    # TODO 2: SELECCION DE CARACTERISTICAS
    # ======================================

    fila = {
        "ventana": ventana,
        "media": np.mean(x),
        "desv": np.std(x),
        "minimo": np.min(x),
        "maximo": np.max(x),
        "rango": np.max(x) - np.min(x),
        "duracion": int(duracion),
        "etiqueta": etiqueta
    }

    filas.append(fila)

# ==========================================
# CREAR TABLA DE CARACTERISTICAS
# ==========================================

features = pd.DataFrame(filas)

# ==========================================
# TODO 3: GUARDAR FEATURES.CSV
# ==========================================

features.to_csv(ARCHIVO_SALIDA, index=False)

print("\nCaracteristicas extraidas correctamente.")

print("\nPrimeras filas:")
print(features.head())

print("\nVentanas por clase:")
print(features.groupby("etiqueta").size())

print("\nTotal de ventanas:", len(features))

print("\nArchivo guardado en:")
print(ARCHIVO_SALIDA)

# ==========================================
# TODO 4: GENERAR GRAFICA DE CARACTERISTICAS
# ==========================================

plt.figure(figsize=(10, 6))

for etiqueta, g in features.groupby("etiqueta"):
    plt.scatter(
        g["rango"],
        g["duracion"],
        label=etiqueta,
        s=65,
        alpha=0.8
    )

plt.title(
    "Comparacion de caracteristicas por tipo de pieza"
)

plt.xlabel("Rango (cm)")
plt.ylabel("Duracion del evento (muestras)")

plt.legend(title="Tipo de pieza")
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Guardar grafica
plt.savefig(
    ARCHIVO_GRAFICA,
    dpi=300,
    bbox_inches="tight"
)

print("\nGrafica guardada en:")
print(ARCHIVO_GRAFICA)

# Mostrar grafica
plt.show()

print("\nProceso completado correctamente.")
