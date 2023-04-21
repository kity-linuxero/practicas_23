# Escribir un programa que pida al usuario 10 números y calcule la suma y el promedio de todos.
# suma = 0 # Para ir sumando

# print("Ingresá 10 números y te doy la suma y promedio ;)")
# for j in range(10):
#     numero = input("Ingrese número: ")
#     suma += int(numero)

# print(f"La suma es: {suma} y el promedio es: {suma/10}")

numero = 1
suma = 0

while(numero <= 10):
    numero1 = int(input("Ingrese un número: "))
    suma = suma + numero1
    numero = numero + 1

print(f"La suma es: {suma} y el promedio es: {suma/10}")