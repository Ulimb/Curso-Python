print("Hola mundo")

# Variables y Tipos de datos

#Crear Variables y darles un valor
x = 1
y = 2

#Existen varios tipos de datos:
# String, cadena de caracteres
# Integer, entero (son para los numeros: -1, 0, 20, etc)
# Boolean, logico (solo guardan True o False)
# Existen otros tipos de datos mas: ver en el material de lectura.

nombre = "Juan"
apellido = "Díaz"
edad = 30
esMayor = True
resto = 20 % 2 # aca estoy obteniendo el resto de una división

# guardar en una variable nombre y apellido junto
nombre_completo = nombre + " " + apellido
# mostrar los datos en pantalla
print(nombre)
print(nombre)
print(nombre_completo)

# imprimir en pantalla el nombre y apellido (avanzado) f-String (verlo en la teoría)
print(f'Nombre completo: {nombre} {apellido}')


# ingresar datos desde teclado y mostrarlo

#obtengo un dato con el input (además muestro un mensaje)
# y al mismo tiempo guardo eso que ingresa en una variable llamada entrada
# Al final muestro el dato en pantalla
entrada = input("Ingrese el valor que quiera guardar en la variable: ")
print("Usted acaba de ingresar: " + entrada)


# Recordar: hay varias maneras para mostrar datos con el print: + , f-String
# el print sirve para mostrar datos
# el input sirve para pedir datos por teclado, además se puede colocar un mensaje.