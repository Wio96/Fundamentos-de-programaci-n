# Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor "profesion" (esta clave ya existe, pero la actualizamos)
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)  # 'None' evita errores si la clave no existiera

# Imprimir el diccionario resultante
print(informacion_personal)
