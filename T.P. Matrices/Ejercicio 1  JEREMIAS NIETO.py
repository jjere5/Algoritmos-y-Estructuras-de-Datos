matriz = [
    [1, 2, 4],  
    [3, 4, 5],
    [2, 2, 2]
]
resultado = 0
for i in matriz:
    for numero in i:
        resultado = resultado + numero
print(resultado)
