##Enunciado:
#Un profesor debe cargar un conjunto de notas de exámenes.
#Debemos realizar un programa que nos permita CARGAR un conjunto de notas de exámenes utilizando una LISTA.
#Luego MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.
#PD.: Usted define si el programa le solicita al usuario la cantidad de notas a cargar o que ingrese el valor 0 para finalizar la carga, por ejemplo.

##Solución:
# Programa para cargar un conjunto de notas de exámenes

# Pedimos al usuario la cantidad de notas que desea ingresar
cantidad_notas = int(input("Ingrese la cantidad de notas a cargar: "))

# Creamos una lista vacía para almacenar las notas
notas = []

# Utilizamos un bucle para cargar las notas en la lista
for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)  # Agregamos cada nota a la lista

# Mostramos el contenido de la lista de notas
print("\nNotas ingresadas:")
for nota in notas:
    print(nota)