def agregar_elemento(array, elemento):
    array += [elemento]
    return array

# Ejemplo
array = [1, 2, 3, 4, 5]
resultado = agregar_elemento(array, 6)
print("Arreglo original:", [1, 2, 3, 4, 5])
print("Después de agregar el 6:", resultado)
