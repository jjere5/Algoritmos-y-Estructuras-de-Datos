import numpy as np 

# Definición de la Matriz (Datos del CSV)
# La matriz contiene los datos, donde cada sub-lista es una fila.
datos_matriz = [
    [1, 'Mateo', None, 45, '76%', 23500, 34, 1, 0, 10, 0, 0, '0:19:58', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [None, 'angel', None, 45, '63%', 20500, 30, 1, 0, 14, 0, 0, '0:17:48', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [3, 'Santiago', None, 45, '59%', 19300, 28, 1, 0, 16, 0, 0, '0:11:16', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [4, 'leonel', None, 45, '59%', 19100, 28, 1, 0, 16, 0, 0, '0:14:39', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [5, 'CaramelosDeColores', None, 45, '59%', 18000, 28, 1, 0, 16, 0, 0, '0:16:12', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [6, 'Bautista', None, 45, '57%', 17600, 27, 1, 0, 17, 0, 0, '0:15:17', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [7, 'Nicolás', None, 45, '53%', 16700, 25, 1, 0, 19, 0, 0, '0:12:30', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [8, 'tucas', None, 45, '49%', 15100, 23, 1, 0, 21, 0, 0, '0:08:29', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [9, 'Benjamín', None, 45, '49%', 14900, 23, 1, 0, 21, 0, 0, '0:16:51', 'Fri 29 Aug 2025,02:43 PM', 'Chrome Mobile on Android', None],
    [10, 'cesar', None, 45, '49%', 14500, 23, 1, 0, 21, 0, 0, '0:18:18', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [11, 'Lautaro', None, 45, '49%', 15000, 23, 1, 0, 21, 0, 0, '0:20:18', 'Fri 29 Aug 2025,02:43 PM', 'Chrome Mobile on Android', None],
    [12, 'Emilio', None, 45, '47%', 14300, 22, 1, 0, 22, 0, 0, '0:19:39', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [13, 'Dylan', None, 40, '43%', 12600, 20, 1, 0, 19, 0, 5, '0:20:16', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [14, 'fidel', None, 45, '37%', 10800, 16, 1, 0, 28, 0, 0, '0:16:51', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None],
    [15, 'Ariadna', None, 3, '0%', 0, 0, 0, 0, 3, 0, 42, '0:00:16', 'Fri 29 Aug 2025,02:43 PM', 'Chrome on Windows', None]
]

# Definición de índices de columna para acceso rápido
INDEX_FIRST_NAME = 1  # Columna 'First Name'
INDEX_SCORE = 5       # Columna 'Score'

# 1. Solicitud de la Condición al Usuario
while True:
    try:
        # Pedimos el valor para la condición de búsqueda
        min_score = int(input("Ingrese el puntaje mínimo de Score que desea buscar: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# 2. Recorrido de la Matriz y Búsqueda Condicional
alumnos_encontrados = []

# Iteración: for fila in datos_matriz:
# El ciclo 'for' recorre la matriz fila por fila.
for fila in datos_matriz:
    try:
        # 3. Acceso y Conversión de Datos
        # Accedemos a la columna 'Score' (índice 5) y la convertimos a entero.
        puntaje = int(fila[INDEX_SCORE]) 
        nombre = fila[INDEX_FIRST_NAME]
        
        # 4. Evaluación de la Condición
        # Si el puntaje cumple la condición, se guarda la fila.
        if puntaje >= min_score:
            alumnos_encontrados.append((nombre, puntaje))
            
    except (ValueError, TypeError):
        # Manejo de error si la columna 'Score' no es un número (ej: está vacía o es 'None')
        continue 

# 5. Mostrar Resultados
print("\n=== Resultados de la Búsqueda ===")
if alumnos_encontrados:
    print(f"Alumnos con Score igual o superior a {min_score} puntos:")
    for nombre, puntaje in alumnos_encontrados:
        print(f" - {nombre}: {puntaje} puntos")
else:
    print("No se encontraron alumnos que cumplan con la condición.")