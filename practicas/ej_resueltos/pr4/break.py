"""
Escriba un programa que tome por teclado la temperatura media de cada día de la semana.

Este programa se da como ejemplo la instrucción break que rompe el loop donde se encuentra.
Si hace menos de 0 grados el programa termina de contar los días.
"""

semana = ['domingo','lunes','martes','miércoles','jueves','viernes','sábado']
temperaturas = []

for dia in semana:
    d = float(input(f"Ingrese la temperatura del día {dia}: "))
    temperaturas.append(d)

    if d < 0:
        print("¡Que frío!")
        break # Rompe el for
else:
    # Solo se ejecuta si no se ha ejecutado la instrucción break
    print("Se terminó la semana")

print(temperaturas)


