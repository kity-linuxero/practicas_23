"""
Escriba un programa que tome por teclado la temperatura media de cada día de la semana.
Una vez tomados los datos que deben ser ingresados por teclado, debe informar la temperatura máxima y la mínima 
y qué día ocurrió cada una y el promedio de temperatura de la semana.

Versión realizada por el instructor
"""

dias = ['domingo', 'lunes','martes','miércoles','jueves','viernes','sábado']

temperaturas = []

for d in dias:
    t = input(f"Ingrese la temperatura para el día {d}: ")
    temps.append(float(t))


max_temp = max(temperaturas)
max_dia = dias[temperaturas.index(max_temp)]

min_temp = min(temperaturas)
min_dia = dias[temperaturas.index(min_temp)]
promedio = sum(temperaturas)/len(temperaturas)

print(f"La temperatura máxima se dió el día {max_dia} con {max_temp}")
print(f"La temperatura mínima se dió el día {min_dia} con {min_temp}")

# Se usa la función round para redondear. El segundo parámetro indica cuantos decimales lleva. En este caso 2.
print(f"La temperatura promedio de la semana fue: {round(promedio,2)}")

