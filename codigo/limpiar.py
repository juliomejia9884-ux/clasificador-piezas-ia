# limpiar.py - quita ruido y normaliza el dataset
import pandas as pd

datos = pd.read_csv('datos/datos.csv')

# TODO 1: quita los valores fuera del rango fisico de tu sensor
# -----------------------------------------------------------
# Para un sensor ultrasónico/IR normalmente el rango físico son unos
# pocos cm hasta ~1-4 m (según el modelo). AJUSTA estos límites a
# la hoja de datos de tu sensor específico.
DIST_MIN = 2      # cm - ajusta al mínimo real de tu sensor
DIST_MAX = 400     # cm - ajusta al máximo real de tu sensor

datos = datos[(datos['valor'] >= DIST_MIN) & (datos['valor'] <= DIST_MAX)]

# TODO 2: aplica el filtro de media movil a la columna 'valor',
#         ventana por ventana
# -----------------------------------------------------------
# La clave: NO se filtra la columna completa de un jalón, porque eso
# mezclaría el final de una ventana con el inicio de la siguiente.
# Se filtra grupo por grupo usando groupby + transform.

TAMANO_FILTRO = 5  # empieza aquí y compara contra la duración de tu evento

datos['valor_filtrado'] = (
    datos.groupby('ventana')['valor']
         .transform(lambda serie: serie.rolling(window=TAMANO_FILTRO, center=True).mean())
)

# TODO 3: decide que hacer con los NaN de las orillas
# -----------------------------------------------------------
# Con center=True y TAMANO_FILTRO=5, las primeras y últimas 2 muestras
# de cada ventana quedan como NaN (no tienen suficientes vecinos).
# Opción elegida aquí: quitarlas (más simple y no inventa datos).
# Alternativa: rellenarlas con bfill/ffill si no quieres perder muestras.

datos = datos.dropna(subset=['valor_filtrado'])

# Guarda el resultado
datos.to_csv('datos/datos_limpios.csv', index=False)

print(f"Filas finales: {len(datos)}")
print(datos.head())