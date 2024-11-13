# Inicializar el valor del número más grande
numero_mas_grande = -1

# Pedir al usuario que ingrese números enteros positivos
while True:
    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
    
    # Finalizar si el número ingresado es 0
    if numero == 0:
        break
    
    # Verificar si el número ingresado es mayor que el número más grande actual
    if numero > numero_mas_grande:
        numero_mas_grande = numero

# Mostrar el número más grande ingresado
if numero_mas_grande == -1:
    print("No se ingresaron números positivos.")
else:
    print("El número más grande ingresado es:", numero_mas_grande)