def ordenar(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

valores = [7, 2, 5, 1]
print("Arreglo ordenado en forma ascendente:", ordenar(valores))
