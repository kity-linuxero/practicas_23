"""
Este es un programa de muestra para ver la instrucción continue.

La lista "alumnxs" contiene el nombre de los alumnos que asistieron a clase.

Cada alumno saluda a quien va llegando. Si llega algún alumno se le saluda como ¡Hey!... ¿Como estás?, de lo contrario
con ¡Hola!. Mucho gusto.

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
        print("¡Hola!. Mucho gusto.")
        continue
    print("¡Hey!... ¿Como estás?")