def crear_matriz(m, n, valor):
    return [[valor for _ in range(n)] for _ in range(m)]

# Ejemplo
m = 3
n = 4
valor = 0
matriz = crear_matriz(m, n, valor)
print(f"Matriz de {m}x{n} inicializada con {valor}:")
for fila in matriz:
    print(fila)
