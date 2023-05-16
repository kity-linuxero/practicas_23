"""
Este es un programa de muestra para ver la instrucción pass.

Cada alumno saluda a quien va llegando. Si llega algún alumno se le saluda como ¡Hey!... ¿Como estás?, de lo contrario
con ¡Hola!. Mucho gusto.

En caso que llegue cristian, el programa hará algo especial, pero aún no está implementado. Por eso se hace con la instrucción pass.
Para dejar mas adelante su implementación.

"""
from random import shuffle


alumnxs = ['mariela','mauro','mina','henry','marcelo','agustin','marcos']

# Se usa shuffle para cambiar el orden (:
shuffle(alumnxs)

nom = ''

for a in alumnxs:
    nom = input(f"¡Hola, soy {a.capitalize()}!. ¿Cuál es tu nombre?\n").lower()

    # Si la persona que llega no es un alumno, vuelve a pedir el nombre.
    if not nom in alumnxs:
        if nom == 'cristian':
            # Pensar algo especial si llega el instructor
            pass # Todavía no implementada
        else:
            print("¡Hola!. Mucho gusto.")
            continue
    print("¡Hey!... ¿Como estás?")