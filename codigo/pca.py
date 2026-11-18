
# pca.py - reduce las caracteristicas a dos componentes y las grafica

import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

features = pd.read_csv('datos/features.csv')

X = features.drop(columns=['ventana', 'etiqueta'])
y = features['etiqueta']  # NO se usa para calcular el PCA, solo para colorear

X_esc = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
componentes = pca.fit_transform(X_esc)

print("Varianza explicada por cada componente:", pca.explained_variance_ratio_)
print("Varianza acumulada de las dos:", pca.explained_variance_ratio_.sum())

# Grafica de los dos componentes principales
plt.figure(figsize=(9, 6))

for etiqueta in y.unique():
    mascara = y == etiqueta
    plt.scatter(
        componentes[mascara, 0],
        componentes[mascara, 1],
        label=etiqueta,
        alpha=0.7
    )

# Porcentajes de varianza explicada
pc1 = pca.explained_variance_ratio_[0] * 100
pc2 = pca.explained_variance_ratio_[1] * 100

# Etiquetas y titulo
plt.xlabel(f'PC1 ({pc1:.2f}% de varianza)')
plt.ylabel(f'PC2 ({pc2:.2f}% de varianza)')
plt.title('PCA - Reduccion de caracteristicas por tipo de pieza')

plt.legend(title='Tipo de pieza')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Crear carpeta figuras si no existe
os.makedirs('figuras', exist_ok=True)

# Guardar la figura
plt.savefig('figuras/pca.png', dpi=300)

plt.show()

print("Grafica guardada en figuras/pca.png")
