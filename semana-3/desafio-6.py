# Inicializar la suma de los números
suma = 0

# Pedir al usuario que ingrese 5 números y sumarlos
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero

# Calcular el promedio
promedio = suma / 5

# Mostrar el promedio
print("El promedio de los números ingresados es:", promedio)