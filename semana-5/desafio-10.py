##Enunciado
#Realizar un programa en el cual:
#Se ingrese por teclado 2 números y haga una división, mostrando su resultado en pantalla.
#Si los datos ingresado por teclado NO son numeros, mostrar algún mensaje al usuario informado el error.
#Si la división es sobre cero, capturar el error y mostrar al usuario un mensaje indicando ese error.

##Resolución
# Bloque principal con manejo de excepciones
try:
    # Pedimos los dos números al usuario
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    # Intentamos realizar la división
    resultado = numero1 / numero2
except ValueError:
    # Capturamos el error si el valor ingresado no es un número
    print("Error: ¡Ingrese solo números válidos!")
except ZeroDivisionError:
    # Capturamos el error si se intenta dividir por cero
    print("Error: No se puede dividir por cero.")
else:
    # Si no hubo errores, mostramos el resultado
    print(f"El resultado de la división es: {resultado}")
finally:
    # Este bloque se ejecuta siempre al final, haya habido errores o no
    print("Gracias por utilizar nuestro sistema.")