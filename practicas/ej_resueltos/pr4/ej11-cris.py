dias = ['domingo', 'lunes','martes','miércoles','jueves','viernes','sábado']

temps = []

for d in dias:
    t = input(f"Ingrese la temperatura para el día {d}: ")
    temps.append(float(t))


max_temp = max(temps)
max_dia = dias[temps.index(max_temp)]

min_temp = min(temps)
min_dia = dias[temps.index(min_temp)]
prom = sum(temps)/len(temps)

print(f"La temperatura máxima se dió el día {max_dia} con {max_temp}")
print(f"La temperatura mínima se dió el día {min_dia} con {min_temp}")
print(f"La temperatura promedio de la semana fue: {round(prom,2)}")

