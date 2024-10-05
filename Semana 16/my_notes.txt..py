# Escritura de Archivo de Texto

# Crea un nuevo archivo llamado my_notes.txt en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribe al menos tres líneas de notas personales en el archivo
    file.write("Estas son mis notas personales.\n")
    file.write("Hoy aprendí sobre manejo de archivos en Python.\n")
    file.write("Estoy disfrutando el proceso de aprendizaje.\n")

# Lectura de Archivo de Texto

# Abre el archivo my_notes.txt en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra en la consola cada línea leída
        print(line.strip())  # Utiliza strip() para eliminar saltos de línea

# Cierre de Archivos
# No es necesario cerrar el archivo explícitamente cuando se usa 'with', ya que se cierra automáticamente al salir del bloque.