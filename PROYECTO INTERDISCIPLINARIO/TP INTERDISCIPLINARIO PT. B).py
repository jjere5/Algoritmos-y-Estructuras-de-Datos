# =====================================================
# TP INTERDISCIPLINARIO – CÓDIGO FINAL PARA LA PARTE B
# FUENTE: resultados_sql_simulados.csv (Estructura de Base de Datos / Notas 5-10)
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# --- CONFIGURACIÓN DE PARÁMETROS ---
CSV_FILENAME = 'resultados_sql_simulados.csv' 



# I. FUNCIONES AUXILIARES

def tiempo_a_segundos(t):
    """
    Convierte el formato de tiempo ('1m 20s') usado en el CSV simulado a un valor entero en segundos.
    """
    if pd.isna(t) or t is None:
        return 0 
    
    t = str(t).strip()
    segundos = 0
    
    # Asume formato 'Xm Ys'
    for parte in t.split():
        if 'm' in parte:
            segundos += int(parte.replace('m', '').strip()) * 60
        elif 's' in parte:
            segundos += int(parte.replace('s', '').strip())
    return segundos

def generar_informe_completo(df, top_p, top_v, ganadores, distribucion):
    """Genera y guarda los 4 gráficos y las estadísticas descriptivas del análisis."""
    print("\n--- INICIO DE AUTOMATIZACIÓN DE INFORME ---")
    
    # 1. Guardar estadísticas generales
    distribucion.to_csv('informe_estadisticas_generales_B.csv', header=True)
    
    # 2. Gráfico 1: Top 10 Puntajes
    plt.figure(figsize=(10, 6))
    plt.barh(top_p['Alumno'], top_p['Puntaje'])
    plt.xlabel('Puntaje (Nota)')
    plt.ylabel('Alumno')
    plt.title('1. Top 10 Mejores Puntajes (SQL)')
    plt.gca().invert_yaxis() 
    plt.tight_layout()
    plt.savefig('informe_grafico_1_top10_puntajes_B.png')
    plt.close()

    # 3. Gráfico 2: Top 10 Veloces
    plt.figure(figsize=(10, 6))
    plt.barh(top_v['Alumno'], top_v['Tiempo_Segundos'])
    plt.xlabel('Tiempo de Respuesta (Segundos)')
    plt.ylabel('Alumno')
    plt.title('2. Top 10 Alumnos Más Veloces (SQL)')
    plt.gca().invert_yaxis() 
    plt.tight_layout()
    plt.savefig('informe_grafico_2_top10_veloces_B.png')
    plt.close()

    # 4. Gráfico 3: Ganadores por Fecha
    plt.figure(figsize=(10, 6))
    # Usamos SoloFecha que ya fue convertida a tipo date
    plt.plot(ganadores['SoloFecha'], ganadores['Puntaje'], marker='o', linestyle='-')
    plt.title('3. Evolución del Puntaje Máximo por Fecha (SQL)')
    plt.xlabel('Fecha')
    plt.ylabel('Puntaje Máximo')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('informe_grafico_3_ganadores_fecha_B.png')
    plt.close()

    # 5. Gráfico 4: Histograma de Distribución (Ajustado para Notas 5-10)
    plt.figure(figsize=(10, 6))
    
    # Bins ajustados para notas (5-10)
    bins_ajustados = [4.5, 6.5, 7.5, 8.5, 9.5, 10.5] 
    
    plt.hist(df['Puntaje'], bins=bins_ajustados, edgecolor='black', alpha=0.8) 
    
    # Etiquetas para el eje X
    plt.xticks([5, 6, 7, 8, 9, 10]) 
    
    plt.title('4. Distribución de Puntajes (Histograma SQL)')
    plt.xlabel('Rango de Puntaje')
    plt.ylabel('Cantidad de Alumnos')
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.savefig('informe_grafico_4_distribucion_puntajes_B.png')
    plt.close()

    print("--- INFORME COMPLETADO: Archivos de la Parte B generados en la carpeta local. ---")


# II. INGESTA DE DATOS


df_torneo = pd.DataFrame() 


print(f"--- PARTE A: Carga desde CSV (Archivo: {CSV_FILENAME}) ---")
try:
    df_torneo = pd.read_csv(CSV_FILENAME)
    print(f"Éxito: Datos cargados desde '{CSV_FILENAME}'.")
except FileNotFoundError:
    print(f"ERROR: Archivo '{CSV_FILENAME}' no encontrado. Análisis abortado.")
    exit()


# =====================================================
# III. LIMPIEZA Y ANÁLISIS
# =====================================================

# 1. Renombrar y crear columnas clave
df_torneo['Alumno'] = df_torneo['NOMBRE'] + ' ' + df_torneo['APELLIDO']

df_torneo = df_torneo.rename(columns={
    'NOTA': 'Puntaje', 
    'FECHAENVIO': 'Fecha',
    'TIEMPO_RESPUESTA': 'TiempoRespuesta'
})

# 2. Conversión de Tipos
df_torneo['Puntaje'] = pd.to_numeric(df_torneo['Puntaje'], errors='coerce')
df_torneo['Fecha'] = pd.to_datetime(df_torneo['Fecha'], errors='coerce')

# 3. Normalización de Tiempos
df_torneo['Tiempo_Segundos'] = df_torneo['TiempoRespuesta'].apply(tiempo_a_segundos)

# 4. Manejo de Nulos 
df_torneo.dropna(subset=['Puntaje', 'Tiempo_Segundos'], inplace=True)
print("\n--- LIMPIEZA COMPLETADA: Filas con datos faltantes eliminadas. ---")

# 5. Análisis Estadístico

# 5.1 Top 10-Mejores Puntajes
top_puntajes = df_torneo.sort_values(by='Puntaje', ascending=False).head(10)
print("\n-- Top 10 Mejores Puntajes --")
print(top_puntajes[['Alumno', 'Puntaje']])

# 5.2 Top 10 - Alumnos Más Veloces
top_veloces = df_torneo.sort_values(by='Tiempo_Segundos', ascending=True).head(10)
print("\n-- Top 10 Alumnos Más Veloces --")
print(top_veloces[['Alumno', 'Tiempo_Segundos']])

# 5.3 Ganadores por Fechas
df_torneo['SoloFecha'] = df_torneo['Fecha'].dt.date
ganadores_por_fecha = df_torneo.loc[df_torneo.groupby('SoloFecha')['Puntaje'].idxmax()]
print("\n-- Ganadores por Fecha --")
print(ganadores_por_fecha[['SoloFecha', 'Alumno', 'Puntaje']])

# 5.4 Distribución de Puntajes
distribucion_puntajes = df_torneo['Puntaje'].describe()
print("\n-- Distribución General de Puntajes --")
print(distribucion_puntajes)

# =====================================================
# IV. AUTOMATIZACIÓN Y ENTREGA
# =====================================================

generar_informe_completo(df_torneo, top_puntajes, top_veloces, ganadores_por_fecha, distribucion_puntajes)