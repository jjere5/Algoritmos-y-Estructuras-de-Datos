def intercambiar_columnas(matriz, col1, col2):
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

intercambiar_columnas(matriz, 0, 2)

for fila in matriz:
    print(fila)
