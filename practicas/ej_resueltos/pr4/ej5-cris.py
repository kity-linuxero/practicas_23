# Este programa es un piedra, papel, tijeras correspondiente al ejercicio 5 de la práctica 4.

# Se importa librería random
from random import choice

# Opciones de juego
opciones = ["piedra", "papel", "tijera"]

# Opciones válidas para elegir del usuario
validas = ['1','2','3','n']

# Resultados arrancan en 0
victorias = derrotas = empates = 0


# Esto es una variable doc-string. Se hace con triple comilla (pueden ser dobles o simples).
# Esto permite hacer strings de mas de una línea.
# Por lo general, este tipo de string se usan para documentar una función. Se verá mas adelante.
texto = '''Elija una opción.
1) Piedra
2) Papel
3) Tijera
n) Salir
    
    Su opción: '''

while (True):
    # Le pido al player que elija una opción.
    player = input(texto)
    
    # Para descartar opciones inválidas
    if not player in validas:   
        print("¡Opción inválida!")
        continue # Vuelve a reiniciar el loop

    # El usuario elige salir del juego
    if player.lower() == 'n':
        break # Rompe el loop

    # Se convierte la opción del player a una opción válida en string
    pl = opciones[int(player)-1] 

    # Elije la computadora
    pc = choice(opciones) # Opción en texto

    # Determinar si el player ganó. Estos son los casos en el que el usuario gana.
    # Observar el uso de and y or.
    gano = (pl == 'piedra' and pc == 'tijera') or (pl == 'papel' and pc == 'piedra') or (pl == 'tijera' and pc == 'papel')

    if gano: # Gana el player
        print (f"¡Ganaste! Yo elegí {pc}\n")
        victorias+=1 # Se suma una victoria
    elif pl == pc: # Empate. Las opciones de juego son iguales. 
        print (f"¡Empatamos! Yo también elegí {pc}\n")
        empates+=1 # Se suma un empate
    else: # Gana PC
        print (f"¡Perdiste! Yo elegí {pc}\n")
        derrotas+=1 # Se suma una derrota

    # Vuelve al loop




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