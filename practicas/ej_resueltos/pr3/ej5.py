# Escriba un programa que solicite al usuario que ingrese 
# dos números e imprima el mayor de ellos.

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número:  "))

if (x>y):
    print(f"El mayor es {x}")
elif (x==y): # Son iguales
    print("Son iguales")
else:
    print(f"El mayor es {y}")