##Enunciado:
#Hola! luego de revisar el material "Entrada y salida de datos", sabremos que podemos solicitar datos con input y con el print podemos armar mensajes:
#- usando el operador +,
#- anteponiendo f al texto, y tambien
#- podemos usar la coma ( , ). Ejemplo: print("Nombre:", nombre)
#Les dejo este desafío para que se animen a completarlo:
#Desarrollar un programa que muestre un mensaje de presentación de los datos de una persona.
#Para eso, deben solicitar por teclado los datos de una persona: nombre, apellido, edad, correo, y luego mostrar un mensaje final con ellos.


##Solución:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo: ")

# 1. Usando el operador +
print("¡Hola! Mi nombre es " + nombre + " " + apellido + ", tengo " + edad + " años y mi correo es " + correo + ".")

# 2. Anteponiendo 'f' al texto
print(f"¡Hola! Mi nombre es {nombre} {apellido}, tengo {edad} años y mi correo es {correo}.")

# 3. Usando la coma ( , )
print("¡Hola! Mi nombre es", nombre, apellido, ", tengo", edad, "años y mi correo es", correo + ".")
