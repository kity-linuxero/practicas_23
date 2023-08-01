#llegue hasta elija una opción de correción
r=""
def introduccion():
    return input(f"¡Bienvenido al TP1 del curso de programación! 1) Modo interactivo 2) Archivo externo ")
#escritorio recibe el texto del usuario(modo intereactivo)
def escritorio():
    total=""
    esc=input("  ")
    while not (esc=="@fin"):
        total= total+esc+"\n"
        esc=input("  ")
    return total
#convierte el archivo spanish en una lista
def diccionario(d):
    return d.split()
#corrector ofrece opciones de corrección
def corrector(text,d):
    for l in text:
        if l.lower() not in d:
            r=input(f"La palabra {l.lower()} no está en el diccionario. Qué desea hacer? 1. Agregarla al diccionario 2. Corregir palabra 3. Ignorar y seguir ")
    return r
#archivo externo
def archivo_externo():
    return input(f"Ingrese el nombre del texto que desea corregir ")


#main
dic1=""
#diccionario
with open ("spanish.dic", "r", encoding="utf-8") as archivo:   
    dic=archivo.read()
    dic1= diccionario(dic)
op= introduccion()
#opción modo interactivo
if op == "1":
    print("Eligió el modo interactivo. Al finalizar la escritura ingrese @fin")
    #modo interactivo
    escrit=escritorio()
    print("Ha finalizado el ingreso de texto.")
    escrit1=escrit.split()
#opción archivo externo
elif op=="2":
    escrit= archivo_externo()
    try:
        with open(escrit) as f:
            escrit1= f.read().split()
#respuesta si no se encuentra el archivo externo
        pass
    except FileNotFoundError:
            print(f"No se encuentra el archivo {escrit}.")
            exit() # Se cierra el programa
#con las palabras del texto que no están en el diccionario ofrece 3 opciones de corrección
corrector(escrit1, dic1)


# Desarrollado por Mariela Montesinos