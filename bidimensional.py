def eliminar_elemento(array, elemento):
    return [item for item in array if item != elemento]

# Ejemplo
array = [1, 2, 3, 4, 5]
resultado = eliminar_elemento(array, 3)
print("Arreglo original:", array)
print("Después de eliminar el 3:", resultado)
