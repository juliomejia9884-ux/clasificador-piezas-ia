
# clustering.py - agrupa el dataset sin usar las etiquetas

import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

features = pd.read_csv('datos/features.csv')

X = features.drop(columns=['ventana', 'etiqueta'])
y = features['etiqueta']  # solo para comparar al final

# Estandarizar los datos
X_esc = StandardScaler().fit_transform(X)

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
grupos = kmeans.fit_predict(X_esc)

# Tabla que compara las etiquetas reales con los grupos encontrados
print("Comparacion entre etiquetas reales y grupos:")
print(pd.crosstab(y, grupos))

# Aplicar PCA para reducir a dos dimensiones
pca = PCA(n_components=2)
componentes = pca.fit_transform(X_esc)

# Crear grafica
plt.figure(figsize=(9, 6))

# Graficar los datos coloreando por grupo
for grupo in sorted(set(grupos)):
    mascara = grupos == grupo

    plt.scatter(
        componentes[mascara, 0],
        componentes[mascara, 1],
        label=f'Grupo {grupo}',
        alpha=0.7
    )

# Etiquetas de los ejes
pc1 = pca.explained_variance_ratio_[0] * 100
pc2 = pca.explained_variance_ratio_[1] * 100

plt.xlabel(f'PC1 ({pc1:.2f}% de varianza)')
plt.ylabel(f'PC2 ({pc2:.2f}% de varianza)')

plt.title('Clustering K-Means - Grupos encontrados')
plt.legend(title='Grupos')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Crear carpeta figuras si no existe
os.makedirs('figuras', exist_ok=True)

# Guardar grafica
plt.savefig('figuras/clustering.png', dpi=300)

plt.show()

print("Grafica guardada en figuras/clustering.png")
