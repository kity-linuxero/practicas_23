# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.

num = int(input("Ingrese un número: "))

if (num < 0):
    print("El número es negativo.")
elif (num > 0):
    print("El número es positivo")
else:
    print("El número es cero")