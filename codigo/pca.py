
# pca.py - reduce las caracteristicas a tres componentes y las grafica en 3D

import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from mpl_toolkits.mplot3d import Axes3D

features = pd.read_csv('datos/features.csv')

X = features.drop(columns=['ventana', 'etiqueta'])
y = features['etiqueta']

# Estandarizar los datos
X_esc = StandardScaler().fit_transform(X)

# PCA con tres componentes
pca = PCA(n_components=3)
componentes = pca.fit_transform(X_esc)

print("Varianza explicada por cada componente:", pca.explained_variance_ratio_)
print("Varianza acumulada de las tres:", pca.explained_variance_ratio_.sum())

# Crear grafica tridimensional
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar cada clase con un color diferente
for etiqueta in y.unique():
    mascara = y == etiqueta

    ax.scatter(
        componentes[mascara, 0],
        componentes[mascara, 1],
        componentes[mascara, 2],
        label=etiqueta,
        alpha=0.7
    )

# Porcentajes de varianza
pc1 = pca.explained_variance_ratio_[0] * 100
pc2 = pca.explained_variance_ratio_[1] * 100
pc3 = pca.explained_variance_ratio_[2] * 100

# Etiquetas de los ejes
ax.set_xlabel(f'PC1 ({pc1:.2f}%)')
ax.set_ylabel(f'PC2 ({pc2:.2f}%)')
ax.set_zlabel(f'PC3 ({pc3:.2f}%)')

ax.set_title('PCA 3D - Reduccion de caracteristicas por tipo de pieza')

ax.legend(title='Tipo de pieza')

plt.tight_layout()

# Crear carpeta figuras si no existe
os.makedirs('figuras', exist_ok=True)

# Guardar grafica
plt.savefig('figuras/pca_3d.png', dpi=300)

plt.show()

print("Grafica guardada en figuras/pca_3d.png")
