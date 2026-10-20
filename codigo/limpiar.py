
# limpiar.py - Semana 4
# Limpieza, filtrado, corrección de línea base,
# normalización y generación de gráfica.

import os
import pandas as pd
import matplotlib.pyplot as plt

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
    CARPETA_DATOS, "datos.csv"
)

ARCHIVO_SALIDA = os.path.join(
    CARPETA_DATOS, "datos_limpios.csv"
)

ARCHIVO_GRAFICA = os.path.join(
    CARPETA_FIGURAS, "limpieza.png"
)

# ==========================================
# CARGAR DATOS ORIGINALES
# ==========================================

if not os.path.exists(ARCHIVO_ENTRADA):
    raise FileNotFoundError(
        f"No se encontro el archivo: {ARCHIVO_ENTRADA}"
    )

datos = pd.read_csv(ARCHIVO_ENTRADA)

columnas = ["ventana", "t", "valor", "etiqueta"]

if not all(c in datos.columns for c in columnas):
    raise ValueError(
        "El CSV debe contener: ventana,t,valor,etiqueta"
    )

for columna in ["ventana", "t", "valor"]:
    datos[columna] = pd.to_numeric(
        datos[columna], errors="coerce"
    )

datos = datos.dropna(subset=columnas).copy()
datos = datos.sort_values(["ventana", "t"])

if datos.empty:
    raise ValueError("El archivo no contiene muestras validas.")

originales = datos.copy()

print("Muestras originales:", len(datos))

# ==========================================
# TODO 1: ELIMINAR VALORES ATIPICOS
# ==========================================

# Ajustar al rango real del sensor ultrasonico
DIST_MIN = 2
DIST_MAX = 400

datos = datos[
    (datos["valor"] >= DIST_MIN) &
    (datos["valor"] <= DIST_MAX)
].copy()

print("Muestras dentro del rango:", len(datos))

if datos.empty:
    raise ValueError(
        "No quedaron muestras dentro del rango fisico."
    )

# ==========================================
# TODO 2: FILTRO DE MEDIA MOVIL
# ==========================================

TAMANO_FILTRO = 5

datos["valor_filtrado"] = (
    datos.groupby("ventana")["valor"]
    .transform(
        lambda serie: serie.rolling(
            window=TAMANO_FILTRO,
            center=True
        ).mean()
    )
)

# ==========================================
# TODO 3: ELIMINAR NaN DE LAS ORILLAS
# ==========================================

datos = datos.dropna(
    subset=["valor_filtrado"]
).copy()

if datos.empty:
    raise ValueError(
        "No quedaron muestras despues del filtro."
    )

# ==========================================
# TODO 4: CORREGIR LINEA BASE
# ==========================================

# Primeras 20 muestras de cada ventana
N_BASE = 20

base = (
    datos[datos["t"] < N_BASE]
    .groupby("ventana")["valor_filtrado"]
    .mean()
)

datos["linea_base"] = datos["ventana"].map(base)

datos = datos.dropna(subset=["linea_base"]).copy()

datos["valor_corregido"] = (
    datos["valor_filtrado"] - datos["linea_base"]
)

# ==========================================
# TODO 5: NORMALIZACION MIN-MAX
# ==========================================

minimo = datos["valor_corregido"].min()
maximo = datos["valor_corregido"].max()

if maximo > minimo:
    datos["valor_normalizado"] = (
        (datos["valor_corregido"] - minimo) /
        (maximo - minimo)
    )
else:
    datos["valor_normalizado"] = 0.0

# ==========================================
# GUARDAR DATASET LIMPIO
# ==========================================

datos.to_csv(ARCHIVO_SALIDA, index=False)

print("\nLimpieza terminada.")
print("Muestras finales:", len(datos))
print("Archivo CSV:", ARCHIVO_SALIDA)

# ==========================================
# TODO 6: CREAR FIGURA DE LIMPIEZA
# ==========================================

# Seleccionar una ventana representativa
ventana_id = datos["ventana"].iloc[0]

antes = originales[
    originales["ventana"] == ventana_id
]

despues = datos[
    datos["ventana"] == ventana_id
]

fig, ejes = plt.subplots(
    2, 1, figsize=(11, 8)
)

# Grafica original
ejes[0].plot(
    antes["t"],
    antes["valor"],
    color="red",
    label="Senal original"
)

ejes[0].set_title(
    f"Ventana {ventana_id} - Antes de limpiar"
)
ejes[0].set_xlabel("Muestra (t)")
ejes[0].set_ylabel("Distancia (cm)")
ejes[0].legend()
ejes[0].grid(True)

# Grafica despues de limpieza
ejes[1].plot(
    despues["t"],
    despues["valor_normalizado"],
    color="blue",
    label="Senal limpia y normalizada"
)

ejes[1].set_title(
    f"Ventana {ventana_id} - Despues de limpiar"
)
ejes[1].set_xlabel("Muestra (t)")
ejes[1].set_ylabel("Valor normalizado")
ejes[1].legend()
ejes[1].grid(True)

plt.suptitle(
    "Comparacion de senal antes y despues de limpieza"
)

plt.tight_layout()

# Guardar la imagen automaticamente
plt.savefig(
    ARCHIVO_GRAFICA,
    dpi=300,
    bbox_inches="tight"
)

print("Grafica guardada:", ARCHIVO_GRAFICA)

# Mostrar la grafica
plt.show()

print("\nProceso completado correctamente.")
