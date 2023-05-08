# Este programa es un piedra, papel, tijeras
from random import choice

# Opciones de juego
opciones = ["piedra", "papel", "tijera"]

# Opciones válidas para elegir del usuario
validas = ['1','2','3','n']

# Resultados
victorias = derrotas = empates = 0

while (True):
    # Le pido al player que elija una opción
    player = input(f"""Elija una opción.
1) Piedra
2) Papel
3) Tijera
n) Salir
    
    Su opción: """).lower()
    
    # Para descartar opciones inválidas
    if not player in validas:   
        print("¡Opción inválida!")
        continue

    # El usuario elige salir del juego
    if player == 'n':
        break

    # Se convierte la opción del player a una opción válida en string
    pl = opciones[int(player)-1] 

    # Elije la computadora
    pc = choice(opciones) # Opción en texto

    # Determinar si el player ganó
    gano = (pl == 'piedra' and pc == 'tijera') or (pl == 'papel' and pc == 'piedra') or (pl == 'tijera' and pc == 'papel')

    if pl == pc: # Empate
        empates+=1
        print (f"¡Empatamos! Yo también elegí {pc}\n")
    elif gano: # Gana el player
        print (f"¡Ganaste! Yo elegí {pc}\n")
        victorias+=1
    else: # Gana PC
        print (f"¡Perdiste! Yo elegí {pc}\n")
        derrotas+=1

# Informo resultados
print(f"""
----------------
¡Fin del juego!.
Resumen:
\tVictorias: {victorias}
\tDerrotas: {derrotas}
\tEmpates: {empates}
\tTotal de partidas: {victorias+derrotas+empates}

Gracias por jugar.
----------------
""")