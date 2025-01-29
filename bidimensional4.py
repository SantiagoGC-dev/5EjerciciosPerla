def buscar_y_agregar(array, elemento):
    for i, item in enumerate(array):
        if item == elemento:
            return i
    array += [elemento]
    return -1  # No se encontro, se agrego al final

# Ejemplo
array = [1, 2, 3, 4, 5]
resultado = buscar_y_agregar(array, 7)
print("Arreglo original:", [1, 2, 3, 4, 5])
print("Posicion del 7 (o agregado):", resultado)
print("Arreglo despues de buscar/agregar:", array)
