# Script = PROGRAMA EN PYTHON
# FUNCIONES: bloques de codigo se guardan/encapsulan bajo un nombre. Definimos con def

# Gestionar/manejar archivos: with as

# Leer un archivo (csv), imprimir cada linea/fila

def leer_archivo(nombre_archivo): # --> parámetro
    """ Lee un archivo CSV e imprime cada linea. """
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        for linea in archivo:
            print(linea.strip())

archivo = 'datos.csv'
# tengo que leer
leer_archivo(archivo)

# 1- Buenas prácticas: variables y funciones --> leer_archivo "snake_case"
# 2- Docstring: descripcion de una funcion
# 3- Métodos: funciones que pertenecen a un Objeto