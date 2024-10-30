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
