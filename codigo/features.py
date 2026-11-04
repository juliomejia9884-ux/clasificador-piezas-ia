
# features.py - Semana 6
# Extraccion de caracteristicas en el dominio del tiempo y frecuencia

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

ARCHIVO_ESPECTRO = os.path.join(
    CARPETA_FIGURAS, "espectro.png"
)

# ==========================================
# FRECUENCIA DE MUESTREO
# ==========================================

FS = 100.0  # Frecuencia de muestreo en Hz

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
# EXTRACCION DE CARACTERISTICAS
# ==========================================

UMBRAL = 5.0

filas = []

for ventana, g in datos.groupby("ventana"):

    g = g.sort_values("t")

    x = g[COLUMNA].to_numpy(dtype=float)

    etiqueta = g["etiqueta"].iloc[0]

    duracion = np.sum(np.abs(x) > UMBRAL)

    # ======================================
    # CARACTERISTICAS DEL DOMINIO DEL TIEMPO
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

    # ======================================
    # CARACTERISTICAS DEL DOMINIO DE FRECUENCIA
    # ======================================

    espectro = np.abs(np.fft.rfft(x))[1:]

    frecuencias = np.fft.rfftfreq(
        len(x), 1/FS
    )[1:]

    # Frecuencia dominante
    if len(espectro) > 0 and np.sum(espectro) > 0:

        f_dominante = frecuencias[
            np.argmax(espectro)
        ]

        centroide = (
            np.sum(frecuencias * espectro)
            / np.sum(espectro)
        )

    else:
        f_dominante = 0
        centroide = 0

    fila["f_dominante"] = f_dominante

    fila["centroide"] = centroide

    # Energia espectral total
    fila["energia_total"] = np.sum(espectro**2)

    # Energia de banda baja: 0 a 10 Hz
    fila["banda_baja"] = np.sum(
        espectro[
            (frecuencias >= 0) &
            (frecuencias < 10)
        ]**2
    )

    # Energia de banda media: 10 a 25 Hz
    fila["banda_media"] = np.sum(
        espectro[
            (frecuencias >= 10) &
            (frecuencias < 25)
        ]**2
    )

    # Energia de banda alta: 25 a 50 Hz
    fila["banda_alta"] = np.sum(
        espectro[
            (frecuencias >= 25) &
            (frecuencias <= 50)
        ]**2
    )

    filas.append(fila)

# ==========================================
# CREAR TABLA DE CARACTERISTICAS
# ==========================================

features = pd.DataFrame(filas)

# ==========================================
# GUARDAR FEATURES.CSV
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
# GRAFICA DE CARACTERISTICAS
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

plt.savefig(
    ARCHIVO_GRAFICA,
    dpi=300,
    bbox_inches="tight"
)

print("\nGrafica guardada en:")
print(ARCHIVO_GRAFICA)

# ==========================================
# GRAFICA DE ESPECTROS POR CLASE
# ==========================================

plt.figure(figsize=(10, 6))

for etiqueta, g_clase in datos.groupby("etiqueta"):

    ventana_elegida = g_clase["ventana"].iloc[0]

    g = g_clase[
        g_clase["ventana"] == ventana_elegida
    ].sort_values("t")

    x = g[COLUMNA].to_numpy(dtype=float)

    espectro = np.abs(np.fft.rfft(x))[1:]

    frecuencias = np.fft.rfftfreq(
        len(x), 1/FS
    )[1:]

    plt.plot(
        frecuencias,
        espectro,
        label=f"{etiqueta}",
        linewidth=1.5
    )

plt.title("Espectro de frecuencia por clase")

plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")

plt.legend(title="Tipo de pieza")
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    ARCHIVO_ESPECTRO,
    dpi=300,
    bbox_inches="tight"
)

print("\nEspectro guardado en:")
print(ARCHIVO_ESPECTRO)

# ==========================================
# MOSTRAR GRAFICAS
# ==========================================

plt.show()

print("\nProceso completado correctamente.")
