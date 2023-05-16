"""
Escriba un programa que genere una lista de 100 elementos con números enteros aleatorios entre -1000 y 1000.
Y luego informe la suma y el promedio de todos los elementos de la lista.

Esta es la versión realizando la suma de todos los números de la lista y realizando la división.

"""

import random
lista = []

for l in range(100):
    lista.append(random.randint(-1000,1000))

suma = 0
for i in lista:
    suma = suma + i

print("La suma es:", suma)
print("El promedio es:", suma/1000)
