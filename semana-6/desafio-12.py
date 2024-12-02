##Enunciado:
# A partir del desafío 9, modificar el programa para que pueda cargar el nombre y la nota de cada alumno, pero usando DICCIONARIOS.
# Luego debo informar el nombre y la nota tanto de los aprobados como de los desaprobados.

##Solución:
# Programa para cargar el nombre y la nota de cada alumno, almacenarlos en un diccionario
# y mostrar tanto aprobados como desaprobados.

# Pedimos al usuario la cantidad de alumnos que desea ingresar
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos a cargar: "))

# Creamos un diccionario vacío para almacenar los alumnos y sus notas
alumnos = {}

# Utilizamos un bucle para cargar los nombres y las notas en el diccionario
for i in range(cantidad_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    while True:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        if 0 <= nota <= 10:
            alumnos[nombre] = nota  # Agregamos el nombre y la nota al diccionario
            break
        else:
            print("Nota fuera de rango. Solo se permiten notas entre 0 y 10. Intente nuevamente.")

# Separar y mostrar alumnos aprobados y desaprobados
print("\nAlumnos aprobados (nota entre 6 y 10):")
for nombre, nota in alumnos.items():
    if nota >= 6:
        print(f"{nombre}: {nota}")

print("\nAlumnos desaprobados (nota menor a 6):")
for nombre, nota in alumnos.items():
    if nota < 6:
        print(f"{nombre}: {nota}")