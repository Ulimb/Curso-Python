# Solicitar los límites del intervalo y el valor entero
limite_inferior = int(input("Ingrese el límite inferior del intervalo: "))
limite_superior = int(input("Ingrese el límite superior del intervalo: "))
valor_entero = int(input("Ingrese un valor entero: "))

# Verificar si el valor entero se encuentra dentro del intervalo
if limite_inferior <= valor_entero <= limite_superior:
    print("El valor entero está dentro del intervalo.")
else:
    print("El valor entero no está dentro del intervalo.")