alu = ('Ana', 'Alejo', 'Valentina', 'Fausto', 'Clara', 'Manuel')

notas = {}

for a in alu:
    while (True):
        x = float(input(f"Ingrese la nota de {a}: "))
        if 0 <= x <= 10:
            notas[a]=float(x)
            break
        else:
            continue
# Terminó el for

for c,v in notas.items():
    print(f"La nota de {c} fue {v}")
    print("APROBÓ") if v > 4 else print("DESAPROBÓ")