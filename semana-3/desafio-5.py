##Enunciado
#Repaso de la clase 2: Estructuras condicionales
#Realizar un programa en el cual se ingrese
#1.El límite inferior de un intervalo
#2.El límite superior del mismo intervalo
#3.Un valor entero
#Indicar si el valor entero ingresado en el punto 3 se encuentra dentro del intervalo definido por los valores del punto (1) y del punto (2).

##Resolución
# Solicitar los límites del intervalo y el valor entero
limite_inferior = int(input("Ingrese el límite inferior del intervalo: "))
limite_superior = int(input("Ingrese el límite superior del intervalo: "))
valor_entero = int(input("Ingrese un valor entero: "))

# Verificar si el valor entero se encuentra dentro del intervalo
if limite_inferior <= valor_entero <= limite_superior:
    print("El valor entero está dentro del intervalo.")
else:
    print("El valor entero no está dentro del intervalo.")