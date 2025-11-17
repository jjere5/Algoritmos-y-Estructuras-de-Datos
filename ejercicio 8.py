#Ejercicio 8:
#Escribir un método que dada una matriz de enteros y un entero, devuelva la posición de la
#matriz en la que se encuentra ese entero, o un valor que indique que el entero no se
#encuentra en la matriz.

matriz = [[1,2,3],[4,5,6],[7,8,9]]

def busqueda(numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return (i, j)
    return None

pos = busqueda(3)

if pos is None:
    print("El numero no se encuentra ")

else: 
    print("La posicion es: fila ",pos[0], "columna ", pos[1])