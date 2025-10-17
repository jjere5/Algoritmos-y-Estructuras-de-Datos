import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("TEST Analisis Datos.xlsx - Participant Data.csv")

# Mostrar las primeras 5 filas para verificar la carga y el formato
print("Primeras 5 filas del DataFrame:")
print(df.head())
print("-" * 50)

# Mostrar información general sobre las columnas (tipos de datos y valores no nulos)
print("Información general del DataFrame:")
print(df.info())
print("-" * 50)

# Mostrar estadísticas descriptivas para las columnas numéricas
print("Estadísticas descriptivas de las columnas numéricas:")
print(df.describe())

# 1. Renombrar columnas
df.rename(columns={
    'Total Questions Attempted': 'Total_Preguntas',
    'Accuracy': 'Precision',
    'Score': 'Puntuacion',
    'Total Time Taken': 'Tiempo_Total'
}, inplace=True)

# 2. Limpiar y convertir 'Precision' a float
# Eliminar el símbolo '%' y convertir a número.
df['Precision'] = df['Precision'].str.replace('%', '').astype(float) / 100

# 3. Convertir 'Tiempo_Total' a segundos
# Se asume el formato 'HH:MM:SS' o similar.
def tiempo_a_segundos(tiempo):
    if pd.isna(tiempo):
        return 0
    try:
        parts = str(tiempo).split(':')
        if len(parts) == 3:
            h, m, s = map(int, parts)
            return h * 3600 + m * 60 + s
        elif len(parts) == 2:
             m, s = map(int, parts)
             return m * 60 + s
        else:
             return 0
    except ValueError:
        return 0 # Manejar valores que no se ajustan al formato

df['Tiempo_Segundos'] = df['Tiempo_Total'].apply(tiempo_a_segundos)

print("\nPrimeras filas después de la limpieza y transformación:")
print(df[['First Name', 'Precision', 'Puntuacion', 'Tiempo_Total', 'Tiempo_Segundos']].head())

promedio_precision = df['Precision'].mean()
promedio_puntuacion = df['Puntuacion'].mean()
promedio_tiempo_seg = df['Tiempo_Segundos'].mean()

print("\n--- Métricas de Rendimiento General ---")
print(f"Precisión media del grupo: {promedio_precision:.2%}")
print(f"Puntuación media del grupo: {promedio_puntuacion:.2f}")
# Convertir el tiempo promedio de segundos a formato minutos:segundos
minutos = int(promedio_tiempo_seg // 60)
segundos = int(promedio_tiempo_seg % 60)
print(f"Tiempo total promedio (Min:Seg): {minutos:02d}:{segundos:02d}")

top_5_puntuacion = df.sort_values(by='Puntuacion', ascending=False).head(5)

print("\n--- Top 5 Participantes por Puntuación ---")
print(top_5_puntuacion[['Rank', 'First Name', 'Puntuacion', 'Precision', 'Tiempo_Total']])

correlacion = df['Puntuacion'].corr(df['Tiempo_Segundos'])

print("\n--- Correlación entre Puntuación y Tiempo ---")
if correlacion > 0.1:
    interpretacion = "positiva (los que puntúan más alto tienden a tomar más tiempo)."
elif correlacion < -0.1:
    interpretacion = "negativa (los que puntúan más alto tienden a tomar menos tiempo - eficiencia)."
else:
    interpretacion = "débil (no hay una relación lineal fuerte)."

print(f"Coeficiente de correlación Puntuación vs. Tiempo: {correlacion:.2f}")
print(f"Interpretación: La correlación es **{interpretacion}**")

respuestas_promedio = df[[' ', 'Incorrect', 'Unattempted']].mean()

print("\n--- Promedio de Tipos de Respuestas por Participante ---")
print(f"Respuestas Correctas promedio: {respuestas_promedio['Correct']:.2f}")
print(f"Respuestas Incorrectas promedio: {respuestas_promedio['Incorrect']:.2f}")
print(f"Preguntas No Intentadas promedio: {respuestas_promedio['Unattempted']:.2f}")








respuestas_promedio = df[['Correct', 'Incorrect', 'Unattempted']].mean()

print("\n--- Promedio de Tipos de Respuestas por Participante ---")
print(f"Respuestas Correctas promedio: {respuestas_promedio['Correct']:.2f}")
print(f"Respuestas Incorrectas promedio: {respuestas_promedio['Incorrect']:.2f}")
print(f"Preguntas No Intentadas promedio: {respuestas_promedio['Unattempted']:.2f}")



# Calcular promedio general de puntuaciones
promedio_general = df['Puntuacion'].mean()
print("\n--- Promedio General ---")
print(f"El puntaje promedio del grupo es: {promedio_general:.2f}")

# Categorizar puntajes bajos
df['Categoria'] = df['Puntuacion'].apply(lambda x: 'Puntaje Bajo' if x < 15000 else 'Puntaje Normal/Alto')

# Mostrar los participantes con puntaje bajo
puntajes_bajos = df[df['Categoria'] == 'Puntaje Bajo']

print("\n--- Participantes con Puntaje Bajo (<15000) ---")
if puntajes_bajos.empty:
    print("Ningún participante tiene un puntaje menor a 15000.")
else:
    print(puntajes_bajos[['First Name', 'Puntuacion']])

print(f"\nCantidad total con Puntaje Bajo: {len(puntajes_bajos)}")