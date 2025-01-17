##Enunciado
#Crear un programa que permita ingresar varios números enteros positivos.
#El programa debe mostrar el número más grande de los que se ingresaron.
#Instrucciones:
#1.El programa pedirá números enteros positivos uno por uno.
#2.Cuando se ingrese el número 0, el programa debe finalizar.
#3.El programa mostrará el número más grande que se haya ingresado (excepto el 0).
#Nota: El programa comienza con un valor inicial de -1 para el número más grande. Este valor no afecta el resultado, ya que siempre se actualiza con el primer número que sea mayor a -1.

##Resolución
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