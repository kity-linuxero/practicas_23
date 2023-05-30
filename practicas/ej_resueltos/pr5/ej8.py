# Desarrolle un programa que, dado el siguiente diccionario,
# devuelva el día con menor temperatura.

temp = {
    'domingo': 23.3,
    'lunes': 22.6,
    'martes': 18.9,
    'miércoles': 17.2,
    'jueves': 19.4,
    'viernes': 20.0,
    'sabado': 24.1
}


def max_min():
    """ 
    Opción usando máximos y mínimos
    """
    min_temp = 99 # No habrá una temperatura mayor.
    min_dia = ''

    for d,t in temp.items():
        if t < min_temp:
            min_temp = t
            min_dia = d
    
    print (f"El día con menor temperatura fue el {min_dia} con {min_temp}ºC")
    

def otra_alternativa():

    # Los convierto a listas.
    keys = temp.keys()
    values = temp.values()

    min_temp = min(values)
    min_dia = keys[]

