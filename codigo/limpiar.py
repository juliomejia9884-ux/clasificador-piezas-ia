import pandas as pd

# Cargar dataset
datos = pd.read_csv('datos/datos.csv')

# 1. Quitar valores fuera del rango físico del sensor ultrasónico
# HC-SR04: aproximadamente 2 a 400 cm
datos = datos[(datos['valor'] >= 2) & (datos['valor'] <= 400)]

# 2. Aplicar filtro de media móvil por ventana
# Se procesa cada ventana por separado para no mezclar señales
datos['valor_limpio'] = datos.groupby('ventana')['valor'].transform(
    lambda x: x.rolling(window=5, center=True).mean()
)

# 3. Rellenar los NaN de las orillas de cada ventana
datos['valor_limpio'] = datos.groupby('ventana')['valor_limpio'].transform(
    lambda x: x.bfill().ffill()
)

# 4. Normalizar los valores entre 0 y 1
minimo = datos['valor_limpio'].min()
maximo = datos['valor_limpio'].max()

datos['valor_normalizado'] = (
    (datos['valor_limpio'] - minimo) / (maximo - minimo)
)

# 5. Guardar el dataset limpio
datos.to_csv('datos/datos_limpios.csv', index=False)

print("Dataset limpiado y normalizado correctamente.")
print("Archivo guardado en: datos/datos_limpios.csv")