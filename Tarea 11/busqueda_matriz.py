matriz = [
    [4, 7, 1],
    [9, 3, 5],
    [2, 8, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no se encontró en la matriz"

# Definir el valor a buscar
valor_a_buscar = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print