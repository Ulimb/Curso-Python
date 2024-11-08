# Pedimos al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificamos si el primer número es múltiplo del segundo
if numero2 != 0 and numero1 % numero2 == 0:
    print("El primer número es múltiplo del segundo.")
else:
    print("El primer número no es múltiplo del segundo.")