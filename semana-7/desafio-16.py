##Enunciado
#Calcular el área de un triángulo
#Escribe una función llamada calcular_area_triangulo que reciba la base y la altura de un triángulo y devuelva su área.
#Prueba la función con diferentes valores de base y altura.
#Puedes incluir manejo de excepciones (opcional).

def calcular_area_triangulo(base, altura):
    try:
        # Verificar que base y altura sean números válidos
        base = float(base)
        altura = float(altura)
        
        if base <= 0 or altura <= 0:
            return "Error: La base y la altura deben ser números positivos."
        
        # Calcular el área
        area = (base * altura) / 2
        return f"El área del triángulo es: {area}"
    
    except ValueError:
        return "Error: La base y la altura deben ser números."

# Probar la función con valores ingresados por el usuario
try:
    base = input("Ingresa la base del triángulo: ")
    altura = input("Ingresa la altura del triángulo: ")
    resultado = calcular_area_triangulo(base, altura)
    print(resultado)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    