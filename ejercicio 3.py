#Ejercicio 3:
#Escribir un método que dada una matriz de enteros y un entero que representa un índice de
#fila, devuelva la columna que contiene el máximo elemento de esa fila.

matriz = [[1,2,3],[4,5,6],[7,8,9]]

def columnaconmayor(fila):
    filal = matriz[fila]
    col = 0
    numero = filal[0]
    for j in range(len(filal)):
        numeroahora = filal[j]
        if numeroahora > numero:
            numero = numeroahora
            col = j

    return col

print(columnaconmayor(0)) 
            