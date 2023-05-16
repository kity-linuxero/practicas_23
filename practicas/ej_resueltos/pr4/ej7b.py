"""
Escriba un programa que genere una lista de 100 elementos con números enteros aleatorios entre -1000 y 1000.
Y luego informe la suma y el promedio de todos los elementos de la lista.

Esta es la versión usando la función sum().

"""

import random
lista = []

for l in range(100):
    lista.append(random.randint(-1000,1000))

suma = sum(lista)

print("La suma es:", suma)
print("El promedio es:", suma/1000)
