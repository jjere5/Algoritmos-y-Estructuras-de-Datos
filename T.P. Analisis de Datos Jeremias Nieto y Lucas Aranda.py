import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['figure.figsize'] = (12, 7)
plt.style.use('ggplot') 
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_columns', None)




print("--- PASO 0: CREACIÓN Y CARGA DEL DATAFRAME ---")

# 1. Definición de la Base de Datos Venta_De_Gorras
data = {
    'Modelo': ["Duki x New Era", "Luky Brown x New Era", "Gran bebe x New Era", "Travis Scott x New Era", "Jhon Baldimur x New Era"],
    'Region': ["Argentina", "Chile", "Argentina", "Estados Unidos", "Alemania"],
    'Tipo_De_Forma': ["Curva Regulable", "Boina", "Sombrero de Gala", "Cerrada plana", "Casco Medieval"],
    'Color': ["Negra y Roja", "Mostaza y Verde", "Violeta y Amarillo", "Negra y Marron", "Todos los Metalicos(Oro, Plata, Cobre)"],
    'Talle_Disponibles': ["Desde 6/ 7/8 hasta 8/ 1/4", "Desde 5 / 1/4 hasta 5/ 2/4", "Desde 72cm hasta 82cm", "Desde 6/ 7/8 hasta 8/ 1/4", "Desde 72cm hasta 82cm"],
    'Año_De_Lanzamiento': ['2025-08-18', '2025-10-03', '1986-11-04', '2022-07-19', '1571-12-19'],
    'Año_De_Produccion': ['2024-04-12', '2025-10-02', '1800-06-12', '2021-09-21', '1200-03-14'],
    'Precio': [99.99, 1.5, 12000.00, 3200.00, 0.02],
    'Vendidas': [1000000000.0, 2.0, 3000000.0, 50000000.0, 110000000.0],
    'Especificaciones_De_Lavado': ["Remojar en agua cepillo de cerdas suaves", "Con agua y jabon", "Con plancha y jabon", "Remojar en agua cepillo de cerdas suaves", "Encerar y pulir"]
}

df = pd.DataFrame(data)

# 2. Conversión de tipos de datos
df['Año_De_Lanzamiento'] = pd.to_datetime(df['Año_De_Lanzamiento'], errors='coerce')
df['Año_De_Produccion'] = pd.to_datetime(df['Año_De_Produccion'], errors='coerce')
df['Vendidas'] = df['Vendidas'].astype(float)
df['Precio'] = df['Precio'].astype(float)



# 1: COMPRENSIÓN Y CARGA DE DATOS


print("\n\n--- 1: COMPRENSIÓN Y CARGA DE DATOS ---")

# a) ¿Cuántas filas y columnas tiene tu dataset?
print(f"\na) Filas (Observaciones): {df.shape[0]}")
print(f"   Columnas (Variables): {df.shape[1]}")

# b) Identifica el tipo de dato de cada columna
print("\nb) Tipos de Datos (d-types):")
print(df.dtypes.to_string())

# c) Muestra las primeras 5 filas
print("\nc) Primeras 5 Filas:")
print(df.head().to_string())



# 2: LIMPIEZA Y PREPARACIÓN DE DATOS


print("\n\n--- 2: LIMPIEZA Y PREPARACIÓN DE DATOS ---")

# Valores Faltantes (Missing Values)
print("\nValores Faltantes (Missing Values):")
missing_values = df.isnull().sum()
if missing_values.sum() == 0:
    print("a) No se encontraron valores faltantes (NaN) en el dataset.")
else:
    print(missing_values[missing_values > 0])

# Imputación (Simulación de imputación por media)
media_precio = df['Precio'].mean()
print(f"\nb) Imputación (Simulación): La Media de 'Precio' es ${media_precio:,.3f}.")
print("Si hubiese valores faltantes, se usaría: df['Precio'].fillna(media_precio, inplace=True).")

# Inconsistencias y Formato:
# a) Estandarización de Región
df['Region'] = df['Region'].str.strip().str.title()
print("\na) Inconsistencias en Región: Aplicado estandarización con .str.title()")

# b) Verificación de Formato Numérico
print("\nb) Verificación de Formato Numérico:")
print("Las columnas 'Vendidas' y 'Precio' están en formato numérico (float64), lo cual es correcto.")



# 3: ANÁLISIS EXPLORATORIO (EDA) Y ESTADÍSTICA DESCRIPTIVA


print("\n\n--- 3: ANÁLISIS EXPLORATORIO Y ESTADÍSTICA DESCRIPTIVA ---")

# --- Medidas de Tendencia Central ---
print("\n--- MEDIDAS DE TENDENCIA CENTRAL ---")
desc_precio = df['Precio'].describe()

# a) Calcula Media, Mediana y Desviación Estándar
media = desc_precio['mean']
mediana = desc_precio['50%']
std = desc_precio['std']

print("a) Medidas para la columna 'Precio' (Monto_Total por unidad):")
print(f"Media (Promedio): ${media:,.2f}")
print(f"Mediana: ${mediana:,.2f}")
print(f"Desviación Estándar (S): ${std:,.2f}")

# b) Análisis de Sesgo
print("\nb) Análisis de Sesgo:")
if media > mediana:
    print(f"Media (${media:,.2f}) > Mediana (${mediana:,.2f}). La distribución está FUERTEMENTE SESGADA A LA DERECHA.")


# --- Análisis Categórico ---
print("\n--- ANÁLISIS CATEGÓRICO ---")

# Preparar la métrica de Ingreso Total
df['Ingreso_Estimado'] = df['Precio'] * df['Vendidas']

# a) Región con mayor Monto_Total
ingreso_por_region = df.groupby('Region')['Ingreso_Estimado'].sum().sort_values(ascending=False)
print("a) Ingreso Estimado por Región:")
print(ingreso_por_region.to_string())

# b) Producto más vendido
productos_vendidos = df[['Modelo', 'Vendidas']].sort_values(by='Vendidas', ascending=False)
print("\nb) Productos más vendidos (Unidades):")
print(productos_vendidos.to_string(index=False))



# 4: VISUALIZACIÓN (GRÁFICOS) CON MATPLOTLIB


print("\n\n--- 4: VISUALIZACIÓN (GRÁFICOS) CON MATPLOTLIB ---")

# Gráfico 1: Gráfico de Barras - Monto Total por Región (Usando Matplotlib puro)
plt.figure(figsize=(10, 6))


plt.bar(
    ingreso_por_region.index, 
    ingreso_por_region.values, 
    color=['#348ABD', '#A60628', '#7A68A6', '#467821'] # Colores de un estilo Matplotlib
) 


plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0)) 
plt.title('Monto Total Acumulado por Región (Ingreso Estimado)')
plt.xlabel('Región')
plt.ylabel('Ingreso Estimado ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Gráfico 1: Gráfico de Barras Creado con Matplotlib.")



plt.figure(figsize=(10, 6))


plt.hist(
    df['Precio'], 
    bins=5, 
    color='#4c72b0', 
    edgecolor='black'
) 

plt.title('Histograma de la Distribución de Precio')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()
print("\nGráfico 2: Histograma Creado con Matplotlib.")
print("La distribución está fuertemente sesgada a la derecha (cola larga de precios altos).")
