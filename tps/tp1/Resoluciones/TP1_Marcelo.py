

def Presentacion():  # Presentacion del programa
    print("¡Bienvenido al TP1 del curso de programación!\nUsted ha ingresado al modo interactivo.")
    print("Seleccione una opcion")
    return input("1) Modo interactivo \n2) Archivo externo ")

############################## comienza modulos modo interactivo##################################


def pres_interactivo():  # Presentacion del modo interactivo
    print("Usted ha ingresado al modo interactivo.")
    print("ingrese el texto deseado\nfinalice ingresando @fin")


def ingreso_texto():  # Ingresamos el texto deseado y lo guardamos en un archivo
    with open("texto_tp1", "w", encoding="utf-8") as texto:

        while True:
            tex = input()  # Ingresa el texto y lo guarda en una variable
            if tex == "@fin":  # En caso de ingresar @fin se detiene el ingreso de texto
                print("Ha finalizado el ingreso de texto.")
                break
            else:
                texto.write(tex+"\n")  # Guarda el texto en un archivo


def l_texto():  # convertimos el archivo en una lista y retornamos la lista
    with open("texto_tp1", "r", encoding="utf-8") as archivo:
        texto = archivo.readline()
        tx = []
        while texto != "":
            tx = tx + texto.split()
            texto = archivo.readline()

        return (tx)
################################## Comienza modulo compartidos##################################


def add_dic(palabra, diccionario):
    with open("spanish.dic", "a", encoding="utf-8") as archivo:
        # agregamos la palabra al archivo/diccionario.
        archivo.write(palabra+"\n")
        # agregamos la palabra a la lista del diccionario para que si aparace nuevamente no la vuelva agregar.
        diccionario.append(palabra)
        print(f"se agrego al diccionario la palabra {palabra}")


# Comparamos en con el diccionario que la palabra corregida este en el diccionario
def revision2(texto, diccionario):
    with open("spanish.dic", "r", encoding="utf-8") as archivo:
        arch = archivo.readlines()
        palabra = texto.lower()
        for ar in arch:
            if palabra == ar.strip('\n'):
                print("esta en el archivo")
                break
        else:
            opciones(palabra, diccionario)


# solicitamos la correccion de la palabra mal ingresada
def correct_tex(palabra, diccionario):
    correccion = input(f"Escriba nuevamente la palabra {palabra}  ")
    revision2(correccion, diccionario)


def opciones(palabra, diccionario):
    op = input(
        f"La palabra \"{palabra}\" no se encuentra en el diccionario.\n¿Qué desea hacer?\n1. Agregarla al diccionario\n2. Corregir palabra\n3. Ignorar y seguir ")
    if op == '1':  # esta opcion agrega la palabra al diccionario
        print("Elegiste opcion 1 ")
        add_dic(palabra, diccionario)
    elif op == '2':  # esta opcion vuelve a solicitar que ingrese la palabra
        print("Elegiste opcion 2 ")
        correct_tex(palabra, diccionario)
    elif op == '3':  # pasa la palabra
        print("Elegiste opcion 3 ")
        pass


# limpiador de parlabras de caracteres y la hago todas las palabras minusculas
def limpia_palabra(palabra):
    palabra = palabra.lower()
    palabra = palabra.strip('\n'',''.'':''?''¿''¡''!''"')
    return palabra


def revision(texto):  # Comparamos en con el diccionario.
    with open("spanish.dic", "r", encoding="utf-8") as archivo:
        # Convierto el alrchivo (diccionario) en una lista
        diccionario = archivo.readlines()
        for palabra in texto:
            # limpio la palabra de caracteres y espacios par luego buscarlo en el diccionario
            palabra = limpia_palabra(palabra)
            for pal_dic in diccionario:
                # realizo un strip en la palabra del diccionario para borrar los espacios tanto delante o detras de la palabra
                if palabra == pal_dic.strip('\n'):
                    break
            else:
                opciones(palabra, diccionario)


def comparamos_in_diccionario(texto):  # compara con el diccionario
    revision(texto)


def mod_interactivo():
    pres_interactivo()  # presentacion del modo interactivo
    ingreso_texto()  # ingreso de texto
    texto = l_texto()  # El texto ingresado lo convertimos en una lista
    comparamos_in_diccionario(texto)  # comparamos el texto con el diccionario

################################## AQUI COMIENZA LOS MODULOS DLE MODO EXTERNO##############################################################


def pres_externo():  # Ingresa el nombre del archivo
    print("Usted ha ingresado al modo externo.")
    print("ingrese el nombre del archivo deseado junto con la extencion por ejemplo \"archivo.txt\" ")
    dir_arch = input()  # ingresael nombre del archivo para abrir
    return dir_arch


def abrir_archivo(tex):  # abre el archivo

    try:
        with open(tex, "r", encoding="utf-8") as archivo:
            texto = archivo.readline()  # convierto la linea en un string
            tx = []  # creo una lista la cual va a contener el diccionario
            while texto != "":
                tx = tx + texto.split()  # hago split a la linea y la agrego a la lista del diccionario
                texto = archivo.readline()  # convierto la linea en un string
    except FileNotFoundError:
        print(f"No se encuentra el archivo {tex}.")
        exit()
    return tx


def mod_externo():
    texto = pres_externo()  # Ingresa el nombre del archivo
    abrir_archivo(texto)  # abre el archivo
    revision(abrir_archivo(texto))  # compara con el diccionario


# main
seleccion = Presentacion()  # selecciona el modo
if int(seleccion) == 1:  # si eleje 1 entra al modo interactivo
    mod_interactivo()
else:
    if int(seleccion) == 2:  # si eleje 2 entra al modo externo
        mod_externo()


# Desarrollado por Marcelo Ayala