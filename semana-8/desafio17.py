##Enunciado
#Realizar un programa que escriba los datos de un diccionario en un archivo.
#Los datos a guardar son: nombre, apellido, edad, email.
#El diccionario puede estar creado previamente o pueden generarlo desde el teclado.

#Pueden elegir:
#Un diccionario con datos de una sola persona.
#Un diccionario que contiene datos de varias personas (usando diccionarios o listas)

##Solución:
# Función para guardar los datos de un diccionario en un archivo
def guardar_diccionario_en_archivo(diccionario, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            for clave, valor in diccionario.items():
                archivo.write(f"{clave}: {valor}\n")
        print(f"Datos guardados exitosamente en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Opción 1: Diccionario con datos de una sola persona
def diccionario_persona_unica():
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    edad = input("Ingresa la edad: ")
    email = input("Ingresa el email: ")

    return {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Email": email
    }

# Opción 2: Diccionario con datos de varias personas
def diccionario_varias_personas():
    personas = []
    cantidad = int(input("¿Cuántas personas deseas agregar? "))
    for i in range(cantidad):
        print(f"\nDatos de la persona {i + 1}:")
        nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        edad = input("Ingresa la edad: ")
        email = input("Ingresa el email: ")

        personas.append({
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Email": email
        })
    return personas

# Guardar datos en un archivo
def guardar_varias_personas_en_archivo(lista_diccionarios, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            for i, persona in enumerate(lista_diccionarios, start=1):
                archivo.write(f"Persona {i}:\n")
                for clave, valor in persona.items():
                    archivo.write(f"  {clave}: {valor}\n")
                archivo.write("\n")
        print(f"Datos guardados exitosamente en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Menú principal
print("Elige una opción:")
print("1. Guardar datos de una persona")
print("2. Guardar datos de varias personas")

opcion = input("Ingresa tu opción (1 o 2): ")

if opcion == "1":
    diccionario = diccionario_persona_unica()
    guardar_diccionario_en_archivo(diccionario, "persona_unica.txt")
elif opcion == "2":
    lista_diccionarios = diccionario_varias_personas()
    guardar_varias_personas_en_archivo(lista_diccionarios, "varias_personas.txt")
else:
    print("Opción no válida.")