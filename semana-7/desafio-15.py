##Enunciado
#Contar vocales
#Escribe una función llamada contar_vocales que reciba una palabra y devuelva cuántas vocales contiene.

#La función debe ignorar si las letras son mayúsculas o minúsculas.
#Usen la siguiente variable que guarda todas las vocales: vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
#Al final, prueba la función con diferentes palabras.
#(Nota: Asumimos que el usuario ingresará una palabra).

# Definir la función contar_vocales
def contar_vocales(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Probar la función con diferentes palabras
palabra = input("Ingresa una palabra: ")
cantidad_vocales = contar_vocales(palabra)
print(f"La palabra '{palabra}' contiene {cantidad_vocales} vocal(es).")