
######################################################
# 1) Carga de datos: Opcion A (desde el archivo csv) #
######################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargamos el archivos desde Drive
try:
  df_torneo = pd.read_csv("./torneo_quizizz.csv")
except FileNotFoundError:
  print("Error al cargar archivo 'torneo_quizizz.csv'.")



###################################################
# 2) Limpieza y Preparación de Datos (EDA)          #
###################################################
df_torneo['Score'] = pd.to_numeric(df_torneo['Score'], errors='coerce')
df_torneo['Started At'] = pd.to_datetime(df_torneo['Started At'], format='%a %d %b %Y, %I:%M %p', errors='coerce')

def tiempo_a_segundos(tiempo_str):
    horas, minutos, segundos = map(int, tiempo_str.split(':'))
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Creo una columna con el tiempo expreado en segundos
df_torneo['Total Time Taken Seconds'] = df_torneo['Total Time Taken'].apply(tiempo_a_segundos)

# Elimino los nulos y los remplazo por cero
df_torneo = df_torneo.fillna(0)


###################################################
#  Análisis Estadístico y Generación de Gráficos  #
###################################################

# Ordeno el DataFrame por 'Score' y seleccionar los 10 mayores
top_scores = df_torneo.nlargest(10, 'Score')

# Crear el gráfico de barras horizontales con los mayores puntajes
plt.figure(figsize=(10, 6))
plt.barh(top_scores['First Name'], top_scores['Score'], color='skyblue')
plt.xlabel('Puntaje')
plt.title('Mejores 10 puntajes')
plt.gca().invert_yaxis()  # Invertir el eje y para que el mayor score esté en la parte superior
plt.savefig("mejores-puntajes.png", format="png")
plt.close()

# Crear el gráfico de barras horizontales con los mas veloces
top_times = df_torneo.nsmallest(10, 'Total Time Taken Seconds')
plt.figure(figsize=(10, 6))
plt.barh(top_times['First Name'], top_times['Total Time Taken Seconds'], color='orange')
plt.xlabel('segundos')
plt.title('Alumnos más velocez')
plt.gca().invert_yaxis()  # Invertir el eje y para que el mayor score esté en la parte superior
plt.savefig("mas-veloces.png", format="png")
plt.close()

# Fechas y puntajes de ejemplo para generar la gráfica
fechas_str = ['2025-06-06', '2025-06-27', '2025-08-08', '2025-08-29', '2025-09-26']
puntajes = [0, 5875, 11750, 17625, 23500]

# Creación de DataFrame (simula el resultado de 'ganadores_por_fecha')
ganadores_por_fecha = pd.DataFrame({'Started At': pd.to_datetime(fechas_str), 'Score': puntajes}).sort_values('Started At')

# Gráfico
plt.figure(figsize=(10, 6))
ganadores_por_fecha.plot(x='Started At', y='Score', kind='line', marker='o', ax=plt.gca())

# Etiquetas
plt.title('Evolución del Puntaje del Ganador')
plt.xlabel('Fecha')
plt.ylabel('Puntaje')

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Estadísticas descriptivas básicas
print(" == Estadísticas descriptivas básicas == ")
estadisticas = df_torneo['Score'].describe()
print(estadisticas)
mediana = df_torneo['Score'].median()
print("Mediana:", mediana)
print()


# Histograma de puntajes
bins = range(0, int(df_torneo['Score'].max()), 1000)

# Crear el histograma
plt.hist(df_torneo['Score'], bins=bins, edgecolor='black')


# Añadir etiquetas y título
plt.xlabel('Rangos de Puntaje')
plt.ylabel('Cantidad de alumnos')
plt.title('Distribución de Puntajes en el Torneo')
plt.grid(axis='y')
plt.savefig('histograma.png', format='png') 
plt.show()










