##Enunciado:
#Retomar el ejercicio del desafío anterior pero solo CARGAR en la LISTA aquellas notas que estén entre 6 y 10 (inclusive)
#MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.

##Solución:
# Programa para cargar un conjunto de notas de exámenes entre 6 y 10

# Pedimos al usuario la cantidad de notas que desea ingresar
cantidad_notas = int(input("Ingrese la cantidad de notas a cargar: "))

# Creamos una lista vacía para almacenar las notas válidas
notas = []

# Utilizamos un bucle para cargar las notas en la lista solo si están entre 6 y 10
for i in range(cantidad_notas):
    while True:
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        
        # Verificamos si la nota está en el rango de 6 a 10
        if 6 <= nota <= 10:
            notas.append(nota)  # Agregamos la nota válida a la lista
            break  # Salimos del bucle cuando la nota es válida
        else:
            print("Nota fuera de rango. Solo se permiten notas entre 6 y 10. Intente nuevamente.")

# Mostramos el contenido de la lista de notas válidas
print("\nNotas ingresadas en el rango de 6 a 10:")
for nota in notas:
    print(nota)