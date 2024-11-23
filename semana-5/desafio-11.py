##Enunciado
#Verificación de DNI en el sistema.
#1.Descripción:
#	-Crea una lista predefinida de números de DNI, por ejemplo: [12345678, 87654321, 11111111, 22222222].
#	El programa deberá permitir al usuario ingresar un número de DNI y verificar si está registrado en la lista.
#2.Funcionalidades requeridas:
#	-Si el DNI se encuentra en la lista:
#	Mostrar el mensaje: "El DNI xxx se encuentra registrado en nuestro sistema."
#	-Si el DNI no se encuentra:
#	Mostrar el mensaje: "El DNI xxx no está registrado en nuestro sistema."
#	-Si la entrada no es un número:
#	Mostrar el mensaje: "Lo lamento, xxx no es un número."
#	-Si el programa se ejecuta sin errores:
#	Mostrar el mensaje: "¡El programa se ejecutó perfectamente!"
#3.Mensajes adicionales:
#	-Siempre mostrar un mensaje final al salir del programa, como: "Gracias por utilizar nuestro sistema."
#4.Opcional:
#	-Permitir al usuario realizar múltiples búsquedas hasta que decida salir escribiendo "salir".

##Resolución
# Lista predefinida de números de DNI
dnis_registrados = [12345678, 87654321, 11111111, 22222222]

# Ciclo para permitir múltiples búsquedas
while True:
    # Pedimos al usuario que ingrese un DNI o escriba "salir" para terminar
    entrada = input("Ingrese un número de DNI para verificar o escriba 'salir' para finalizar: ")
    
    # Verificamos si el usuario desea salir
    if entrada.lower() == "salir":
        break
    
    try:
        # Intentamos convertir la entrada a un número entero
        dni = int(entrada)
        
        # Verificamos si el DNI está en la lista
        if dni in dnis_registrados:
            print(f"El DNI {dni} se encuentra registrado en nuestro sistema.")
        else:
            print(f"El DNI {dni} no está registrado en nuestro sistema.")
    
    except ValueError:
        # Capturamos el error si la entrada no es un número
        print(f"Lo lamento, '{entrada}' no es un número.")
    
    else:
        # Mensaje si el programa se ejecuta sin errores
        print("¡El programa se ejecutó perfectamente!")

# Mensaje final de despedida
print("Gracias por utilizar nuestro sistema.")


