def buscar_elemento_iterativo(array, elemento):
    for i, item in enumerate(array):
        if item == elemento:
            return i
    return -1

# Ejemplo
array = [1, 2, 3, 4, 5]
resultado = buscar_elemento_iterativo(array, 4)
print("Arreglo:", array)
print("Posición del elemento 4:", resultado)
