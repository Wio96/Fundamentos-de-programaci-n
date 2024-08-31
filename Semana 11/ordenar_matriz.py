matriz = [
    [4, 7, 1],
    [9, 3, 5],
    [2, 8, 6]
]


def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz


print("Matriz original:")
for fila in matriz:
    print(fila)


fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)


print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
