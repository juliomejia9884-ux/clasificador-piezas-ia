
# limpiar.py - Semana 4
# Limpieza, filtrado, correccion de linea base,
# normalizacion y generacion de grafica.

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
# CARGAR DATOS
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
    raise ValueError("No hay muestras validas.")

originales = datos.copy()

ventanas_originales = datos["ventana"].nunique()

print("Muestras originales:", len(datos))
print("Ventanas originales:", ventanas_originales)

# ==========================================
# TODO 1: ELIMINAR VALORES ATIPICOS
# ==========================================

DIST_MIN = 2
DIST_MAX = 400

datos = datos[
    (datos["valor"] >= DIST_MIN) &
    (datos["valor"] <= DIST_MAX)
].copy()

print("Muestras dentro del rango:", len(datos))

# ==========================================
# TODO 2: FILTRO DE MEDIA MOVIL
# ==========================================

TAMANO_FILTRO = 5

datos["valor_filtrado"] = (
    datos.groupby("ventana")["valor"]
    .transform(
        lambda serie: serie.rolling(
            window=TAMANO_FILTRO,
            center=True,
            min_periods=1
        ).mean()
    )
)

# ==========================================
# TODO 3: CORREGIR LINEA BASE
# ==========================================

N_BASE = 20

def calcular_base(grupo):

    primeras = grupo[
        grupo["t"] < N_BASE
    ]["valor_filtrado"]

    # Si no hay muestras en las primeras 20,
    # utilizar la media de la ventana disponible.
    if primeras.empty:
        return grupo["valor_filtrado"].mean()

    return primeras.mean()


base = datos.groupby("ventana").apply(
    calcular_base,
    include_groups=False
)

datos["linea_base"] = datos["ventana"].map(base)

datos["valor_corregido"] = (
    datos["valor_filtrado"] - datos["linea_base"]
)

# ==========================================
# TODO 4: NORMALIZACION MIN-MAX
# ==========================================

def normalizar(grupo):

    minimo = grupo["valor_corregido"].min()
    maximo = grupo["valor_corregido"].max()

    if maximo > minimo:
        return (
            (grupo["valor_corregido"] - minimo) /
            (maximo - minimo)
        )

    return pd.Series(
        0.0,
        index=grupo.index
    )


datos["valor_normalizado"] = (
    datos.groupby("ventana", group_keys=False)
    .apply(normalizar, include_groups=False)
    .reset_index(level=0, drop=True)
)

# ==========================================
# GUARDAR DATASET LIMPIO
# ==========================================

datos = datos.sort_values(["ventana", "t"])

datos.to_csv(ARCHIVO_SALIDA, index=False)

ventanas_finales = datos["ventana"].nunique()

print("\n========== RESULTADOS ==========")
print("Ventanas originales:", ventanas_originales)
print("Ventanas finales:", ventanas_finales)
print("Muestras finales:", len(datos))

print("\nVentanas por etiqueta:")
print(
    datos.groupby("etiqueta")["ventana"].nunique()
)

print("\nArchivo guardado:", ARCHIVO_SALIDA)

if ventanas_originales != ventanas_finales:
    print("ADVERTENCIA: Algunas ventanas no tienen muestras validas.")

# ==========================================
# TODO 5: GRAFICA DE LIMPIEZA
# ==========================================

ventana_id = datos["ventana"].iloc[0]

antes = originales[
    originales["ventana"] == ventana_id
]

despues = datos[
    datos["ventana"] == ventana_id
]

fig, ejes = plt.subplots(2, 1, figsize=(11, 8))

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

plt.savefig(
    ARCHIVO_GRAFICA,
    dpi=300,
    bbox_inches="tight"
)

print("\nGrafica guardada:", ARCHIVO_GRAFICA)

plt.show()

print("\nProceso completado correctamente.")
