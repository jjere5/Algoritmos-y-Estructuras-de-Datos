
import random


inventario_tienda = {
    'Oficina': {'Teclado': 1, 'Mouse': 1, 'Monitor': 1, 'Auricular': 3},
    'Computadoras': {'PlacaMadre': 2, 'Procesador': 2, 'SSD': 2, 'RAM': 4, 'Fuente': 2, 'Grafica': 3},
    'DispositivosMóviles': {'Samsung': 8, 'iPhone': 7, 'Motorola': 5, 'Xiaomi': 11}
}

print("----------------------------------------")
print("El inventario de productos es:")
for categoria_actual in inventario_tienda:
    print(categoria_actual, inventario_tienda[categoria_actual])
print("----------------------------------------")


lista_categorias = list(inventario_tienda.keys())
categoria_aleatoria = random.choice(lista_categorias)

for _ in range(3):
    lista_productos = list(inventario_tienda[categoria_aleatoria].keys())
    producto_aleatorio = random.choice(lista_productos)
    stock_actualizado = inventario_tienda[categoria_aleatoria][producto_aleatorio] - 1
    inventario_tienda[categoria_aleatoria][producto_aleatorio] = stock_actualizado
    
    if stock_actualizado > 0:
        print(f"Se ha vendido un {producto_aleatorio}, quedan {stock_actualizado}.")
    else:
        inventario_tienda[categoria_aleatoria].pop(producto_aleatorio)
        print(f"Se terminó el stock de {producto_aleatorio}.")
        
print("----------------------------------------")
print(f"El nuevo inventario es:")
for categoria_actual in inventario_tienda:
    print(categoria_actual, inventario_tienda[categoria_actual])


while True: 
    print("\nIngrese la opción deseada")
    print("1 - Agregar un nuevo producto al inventario")
    print("2 - Agregar stock a un producto existente")
    print("3 - Ver el inventario")
    opcion_elegida = input("> ")

    
    if opcion_elegida == '1':
        nuevo_producto_nombre = input("Ingrese el nombre del producto que desea agregar a su inventario: ")

        print("¿A qué categoría desea agregarlo?")
        categorias_disponibles = list(inventario_tienda.keys())
        for i, nombre_categoria in enumerate(categorias_disponibles, 1):
            print(f"{i} - {nombre_categoria}")
        
        opcion_categoria_elegida = input("> ")

        if opcion_categoria_elegida.isdigit() and 1 <= int(opcion_categoria_elegida) <= len(categorias_disponibles):
            nombre_categoria = categorias_disponibles[int(opcion_categoria_elegida) - 1]
            print(f"Ha elegido la categoría {nombre_categoria}")
            try:
                cantidad_producto_nuevo = int(input("Ingrese el stock de su producto nuevo: "))
                inventario_tienda[nombre_categoria][nuevo_producto_nombre] = cantidad_producto_nuevo
                print("El inventario se ha actualizado correctamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
        else:
            print("No existe una categoría con ese número.")

    elif opcion_elegida == '2':
        categoria_a_reponer = input("Elija la categoría que desea reponer: ")
        if categoria_a_reponer in inventario_tienda:
            print(f"Esta categoría tiene:")
            print(inventario_tienda[categoria_a_reponer])
            producto_a_reponer = input("Elija el producto que desea reponer: ")
            if producto_a_reponer in inventario_tienda[categoria_a_reponer]:
                try:
                    cantidad_reposicion = int(input("Ingrese cuánto stock quiere reponer: "))
                    inventario_tienda[categoria_a_reponer][producto_a_reponer] += cantidad_reposicion
                    print("El inventario se ha actualizado correctamente.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
            else:
                print("El producto no está en el inventario.")
        else: 
            print("La categoría no está en el inventario.")

    elif opcion_elegida == '3':
        print("Su inventario es: ")
        for categoria_actual in inventario_tienda:
            print(categoria_actual, inventario_tienda[categoria_actual])

    else:
        print("Opción no válida. Intenta otra vez.")