#Ejercicio 1:
#Escribir un método que dada una matriz de enteros devuelva la suma de los elementos que
#contiene la matriz.

matriz = [[1,2,3],[4,5,6],[7,8,9]]

def sumartodosloselementos():
    sumo = 0
    for i in matriz:
        for j in i:
            sumo += j

    return sumo

print(sumartodosloselementos())