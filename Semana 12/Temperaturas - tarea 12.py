ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4


temperaturas = [
    [  # Ciudad1
        [20, 21, 19, 22, 20, 18, 19],  # Semana 1
        [21, 22, 20, 23, 21, 19, 20],  # Semana 2
        [22, 21, 19, 23, 20, 18, 19],  # Semana 3
        [20, 22, 21, 24, 21, 19, 20]  # Semana 4
    ],
    [  # Ciudad2
        [25, 26, 27, 24, 25, 28, 26],  # Semana 1
        [26, 27, 25, 28, 29, 26, 27],  # Semana 2
        [24, 25, 26, 27, 26, 28, 25],  # Semana 3
        [27, 28, 26, 29, 30, 27, 28]  # Semana 4
    ],
    [  # Ciudad3
        [18, 19, 17, 18, 19, 17, 16],  # Semana 1
        [19, 20, 18, 20, 21, 18, 17],  # Semana 2
        [17, 18, 19, 18, 19, 16, 17],  # Semana 3
        [18, 19, 18, 19, 20, 17, 18]  # Semana 4
    ]
]

# Bucle para calcular los promedios de temperatura por ciudad y semana
for i in range(len(ciudades)):  # Recorremos cada ciudad
    print(f"Promedio de temperaturas para {ciudades[i]}:")
    for j in range(semanas):  # Recorremos cada semana (ahora 4 semanas)
        suma_temperaturas = 0
        for k in range(len(dias_semana)):  # Recorremos los días de la semana
            suma_temperaturas += temperaturas[i][j][k]

        promedio_temperaturas = suma_temperaturas / len(dias_semana)
        print(f"  Semana {j + 1}: {promedio_temperaturas:.2f}°C")