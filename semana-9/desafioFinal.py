##Enunciado de la Actividad: Filtrado de Información en un Archivo CSV
 
#Objetivo: Crear un programa en Python que permita filtrar datos de personas según un rango de edades. Pueden utilizar el  archivo datos.csv

#Requisitos:
#Leer el archivo CSV:

#Cargar los datos del archivo datos.csv en una estructura que te resulte cómoda (por ejemplo, una lista de diccionarios).
#Pedir datos al usuario:

#Solicitar al usuario que ingrese un rango de edades (edad mínima y edad máxima).
#Filtrar la información:

#Mostrar los datos completos de las personas que se encuentren dentro del rango de edades especificado.
#Opciones adicionales (opcionales):
#Agregar un menú de opciones.
#Agregar más filtros, como búsqueda por nombre o ciudad.
#Usar otro archivo .csv con una estructura diferente, pero implementar algún tipo de filtrado.
#Guardar los resultados filtrados en un nuevo archivo CSV o TXT.

import csv

# Función para cargar los datos del archivo CSV como una lista de diccionarios
def cargar_datos(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                row['Edad'] = int(row['Edad'])  # Convertir la edad a entero
                datos.append(row)
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []

# Función para filtrar datos por rango de edades
def filtrar_por_edad(datos, edad_min, edad_max):
    return [persona for persona in datos if edad_min <= persona['Edad'] <= edad_max]

# Función para guardar resultados en un nuevo archivo CSV
def guardar_datos(nombre_archivo, datos_filtrados):
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            fieldnames = ['Nombre', 'Edad', 'Ciudad']
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datos_filtrados)
        print(f"Los datos filtrados fueron guardados en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Menú de opciones
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Filtrar por rango de edades")
    print("2. Buscar por ciudad")
    print("3. Guardar resultados filtrados en un archivo")
    print("0. Salir")

# Programa principal
def main():
    archivo = 'datos.csv'
    datos = cargar_datos(archivo)

    if not datos:
        return

    resultados = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                edad_min = int(input("Ingresa la edad mínima: "))
                edad_max = int(input("Ingresa la edad máxima: "))
                resultados = filtrar_por_edad(datos, edad_min, edad_max)
                if resultados:
                    print(f"\nPersonas entre {edad_min} y {edad_max} años:")
                    for persona in resultados:
                        print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Ciudad: {persona['Ciudad']}")
                else:
                    print("No se encontraron personas en ese rango de edades.")
            except ValueError:
                print("Por favor ingresa valores numéricos válidos para las edades.")

        elif opcion == '2':
            ciudad = input("Ingresa la ciudad para filtrar: ").strip().lower()
            resultados = [persona for persona in datos if persona['Ciudad'].strip().lower() == ciudad]
            if resultados:
                print(f"\nPersonas en {ciudad.capitalize()}:")
                for persona in resultados:
                    print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Ciudad: {persona['Ciudad']}")
            else:
                print(f"No se encontraron personas en la ciudad de {ciudad.capitalize()}.")

        elif opcion == '3':
            if resultados:
                archivo_salida = input("Ingresa el nombre del archivo para guardar (ejemplo: resultados.csv): ").strip()
                guardar_datos(archivo_salida, resultados)
            else:
                print("No hay resultados para guardar. Realiza un filtrado primero.")

        elif opcion == '0':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()