# Ejercicio 11

cant_personas = 0
nombre = "Nadie"

while (nombre.lower() != "juan"):
    nombre = input("Ingrese su nombre: ")

    cant_personas = cant_personas +1

print(f"Llegaron {cant_personas} personas.")