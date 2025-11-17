#Ejercicio 11:
#Escribir un método que dada una matriz de enteros y dos enteros que representan índices de
#fila, intercambie las filas correspondientes de la matriz.

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
def cambio(fila, fila2):

    matriz[fila], matriz[fila2] = matriz[fila2], matriz[fila] 
    
    return matriz


print(cambio(0, 2))
