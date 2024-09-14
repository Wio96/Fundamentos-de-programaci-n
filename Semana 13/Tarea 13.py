def calcular_promedio_temperaturas(temperaturas):
    promedios_ciudades = []

    for ciudad in temperaturas:
        total_temperaturas = 0
        total_dias = 0

        # Recorre cada semana de la ciudad
        for semana in ciudad:
            total_temperaturas += sum(semana)  # Suma todas las temperaturas de la semana
            total_dias += len(semana)  # Cuenta los días de la semana

        # Calcula el promedio de la ciudad
        promedio_ciudad = total_temperaturas / total_dias
        promedios_ciudades.append(promedio_ciudad)

    return promedios_ciudades


# Datos de las temperaturas
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

# Llamar a la función
promedios = calcular_promedio_temperaturas(temperaturas)

# Imprimir el promedio de cada ciudad
for i, promedio in enumerate(promedios, 1):
    print(f"El promedio de temperatura de la Ciudad {i} es: {promedio:.2f}°C")