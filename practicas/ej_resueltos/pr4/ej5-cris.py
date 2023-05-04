# Este programa es un piedra, papel, tijeras
from random import choice

# Opciones de juego
opciones = ["piedra", "papel", "tijera"]

# Opciones válidas para elegir del usuario
validas = ['1','2','3']

# Como estaba aburrido le puse emojis :D
emojis = ['🪨', '📃', '✂️','🆚']

# Resultados
victorias = derrotas = empates = 0

while (True):
    # Le pido al player que elija una opción
    player = input(f"---------\nElija una opción.\n1) Piedra\n2) Papel\n3) Tijera\n\nSu opción: ")
    
    # Para descartar opciones inválidas
    while not player in validas:   
        player = input("Elija una opción.\n1) Piedra\n2) Papel\n3) Tijera\n\nSu opción: ")

    # Se tiene en formato número para poder elejir un emoji
    pl_n = int(player)-1

    # Se convierte la opción del player a una opción válida en string
    pl = opciones[pl_n] 

    # Elije la computadora
    pc = choice(opciones) # Opción en texto
    pc_n = opciones.index(pc) # En número

    # Acá se imprimen los emojis 😁
    print(f"Resultado: {emojis[pl_n]} {emojis[-1]} {emojis[pc_n]}\n")

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

    seguir = input("¿Querés seguir jugando?\n(n para salir) ")
    if seguir.lower() == 'n':
        break

# Informo resultados
print(f"\n¡Fin del juego!.\nResumen:\n\tVictorias: {victorias}\n\tDerrotas: {derrotas}\n\tEmpates: {empates}\n\tTotal de partidas: {victorias+derrotas+empates}\n-------------\nGracias por jugar.\n")