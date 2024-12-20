##Enunciado
#Retomar el desafío anterior e indicar cuantos y que DNI superan el valor de 40 millones.

##Solución:
# 1. Creamos un diccionario vacío para almacenar los datos de las personas
personas = {}

# 2. Pedimos al usuario que ingrese los datos para 3 personas
for i in range(3):
    print(f"Ingrese los datos de la persona {i + 1}:")
    
    # 2.1 Input del nombre
    nombre = input("Nombre: ")
    
    # 2.2 Input del apellido
    apellido = input("Apellido: ")
    
    # 2.3 Input del DNI
    dni = input("DNI: ")
    
    # 2.4 Creamos un nuevo diccionario con los datos ingresados
    persona = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }
    
    # 2.5 Agregamos el diccionario de la persona al diccionario general de personas
    personas[i + 1] = persona

# 3. Mostramos los datos ingresados para cada persona
print("\nDatos de las personas ingresadas:")
for clave, persona in personas.items():
    print(f"\nPersona #{clave}:")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"DNI: {persona['dni']}")

# 4. Verificar cuántos y qué DNIs superan los 40 millones
dnis_superan_40_millones = []  # Lista para almacenar los DNIs que superan los 40 millones

for persona in personas.values():
    dni = persona['dni']
    if dni.isdigit() and int(dni) > 40000000:  # Verificamos si el DNI es un número y mayor a 40 millones
        dnis_superan_40_millones.append(dni)

# 5. Mostrar cuántos y qué DNIs superan los 40 millones
print("\nDNI que superan los 40 millones:")
if dnis_superan_40_millones:
    print(f"Cantidad de DNIs que superan los 40 millones: {len(dnis_superan_40_millones)}")
    print("DNIs:", ', '.join(dnis_superan_40_millones))
else:
    print("Ningún DNI supera los 40 millones.")