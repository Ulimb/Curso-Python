##Enunciado
#Realizar un programa en el cual se ingresen dos numeros e informe si el primero es múltiplo del segundo.
#En caso contrario deberá generar un mensaje adecuado.

##Resolución
# Pedimos al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificamos si el primer número es múltiplo del segundo
if numero2 != 0 and numero1 % numero2 == 0:
    print("El primer número es múltiplo del segundo.")
else:
    print("El primer número no es múltiplo del segundo.")