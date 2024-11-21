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