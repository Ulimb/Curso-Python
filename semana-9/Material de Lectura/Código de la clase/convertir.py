# Convertir datos de un archivo csv en una lista de diccionarios

# 1- Leer el archivo
# 2- Crear una lista de diccionarios
# 3- Imprimir la lista

import csv

def leer_datos_como_diccionario(nombre_archivo):
    data = []
    with open(nombre_archivo, mode='r', encoding='utf-8-sig') as archivo:
        reader = csv.DictReader(archivo) # Convierte las filas en diccionarios
        for row in reader:
            row['Edad'] = int(row['Edad']) # Convertimos 'edad' en entero
            data.append(row)
    return data



archivo = 'datos.csv'
# usar mi funcion
datos = leer_datos_como_diccionario(archivo)
for d in datos:
    print(d)