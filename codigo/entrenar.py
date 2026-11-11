
# entrenar.py - Entrena el clasificador y lo guarda en modelo.pkl

import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

# ==========================================
# RUTAS DEL PROYECTO
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CARPETA_DATOS = os.path.join(BASE_DIR, "datos")
CARPETA_FIGURAS = os.path.join(BASE_DIR, "figuras")

os.makedirs(CARPETA_FIGURAS, exist_ok=True)

ARCHIVO_ENTRADA = os.path.join(
    CARPETA_DATOS, "features.csv"
)

ARCHIVO_MODELO = os.path.join(
    BASE_DIR, "modelo.pkl"
)

ARCHIVO_GRAFICA = os.path.join(
    CARPETA_FIGURAS, "confusion.png"
)

# ==========================================
# CARGAR DATASET
# ==========================================

if not os.path.exists(ARCHIVO_ENTRADA):
    raise FileNotFoundError(
        f"No se encontro el archivo: {ARCHIVO_ENTRADA}"
    )

features = pd.read_csv(ARCHIVO_ENTRADA)

if features.empty:
    raise ValueError("El archivo features.csv esta vacio.")

if not all(c in features.columns for c in ["ventana", "etiqueta"]):
    raise ValueError(
        "El CSV debe contener las columnas ventana y etiqueta."
    )

# Separar caracteristicas y etiquetas

X = features.drop(
    columns=["ventana", "etiqueta"]
)

y = features["etiqueta"].astype(str).str.strip().str.lower()

# Comprobar que las caracteristicas sean numericas

X = X.apply(pd.to_numeric, errors="coerce")

# Eliminar filas con datos faltantes

validos = X.notna().all(axis=1) & y.notna() & (y != "")

X = X.loc[validos].copy()
y = y.loc[validos].copy()

if X.empty:
    raise ValueError("No hay datos validos para entrenar.")

# Comprobar que existan suficientes ejemplos por clase

conteo = y.value_counts()

print("========== DATASET ==========")
print("Total de ejemplos:", len(X))
print("\nEjemplos por clase:")
print(conteo)

if len(conteo) < 2:
    raise ValueError("Se necesitan al menos dos clases.")

if conteo.min() < 2:
    raise ValueError(
        "Cada clase necesita al menos dos ejemplos para dividir los datos."
    )

# ==========================================
# DIVIDIR DATOS: 80% ENTRENAMIENTO / 20% PRUEBA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\n========== DIVISION DE DATOS ==========")
print("Datos para entrenamiento:", len(X_train))
print("Datos para prueba:", len(X_test))

# ==========================================
# NORMALIZAR CARACTERISTICAS
# ==========================================

escalador = StandardScaler()

X_train_esc = escalador.fit_transform(X_train)

X_test_esc = escalador.transform(X_test)

# ==========================================
# ENTRENAR MODELO KNN
# ==========================================

modelo = KNeighborsClassifier(
    n_neighbors=5
)

modelo.fit(X_train_esc, y_train)

# ==========================================
# REALIZAR PREDICCIONES
# ==========================================

y_pred = modelo.predict(X_test_esc)

# ==========================================
# EVALUAR MODELO
# ==========================================

exactitud = accuracy_score(y_test, y_pred)

clases = sorted(y.unique())

matriz = confusion_matrix(
    y_test,
    y_pred,
    labels=clases
)

print("\n========== RESULTADOS ==========")

print(f"Exactitud del modelo: {exactitud * 100:.2f}%")

print("\nMatriz de confusion:")
print(matriz)

print("\nOrden de las clases:")
print(clases)

print("\nReporte de clasificacion:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=clases,
        zero_division=0
    )
)

# ==========================================
# GRAFICAR MATRIZ DE CONFUSION
# ==========================================

display = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=clases
)

fig, ax = plt.subplots(figsize=(8, 6))

display.plot(
    ax=ax,
    cmap="Blues",
    values_format="d",
    colorbar=False
)

plt.title("Matriz de confusion - Clasificador KNN")
plt.tight_layout()

plt.savefig(
    ARCHIVO_GRAFICA,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGrafica guardada en:", ARCHIVO_GRAFICA)

# ==========================================
# GUARDAR MODELO Y ESCALADOR
# ==========================================

joblib.dump(
    {
        "modelo": modelo,
        "escalador": escalador,
        "columnas": list(X.columns)
    },
    ARCHIVO_MODELO
)

print("\nModelo guardado en:", ARCHIVO_MODELO)

print("\nProceso de entrenamiento completado correctamente.")
