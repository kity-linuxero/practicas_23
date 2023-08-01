
def leer_diccionario():
    diccionario = []  #lista vacio
    with open('spanish.dic', 'r', encoding='utf-8') as archivo:
        for palabra in archivo.readlines():
            palabra=palabra.lower()
            diccionario.append(palabra.strip())  #agrega cada palabra a la lista de diccionario interno
    return diccionario

def modo_interactivo():
    carta=""
    entrada=input("Ingrese texto.Termine con @fin:\n")
    while entrada.lower() !="@fin":        
        carta=carta+"\n"+entrada.lower()
        entrada=input()
    print("Finalizo el igreso de texto.")
    return carta
    

def leer_archvio_externo(x):#abre el archivo externo y 
    palabraxpalabra=""
    with open(x, 'r', encoding='utf-8') as archivo_externo: #el archivo es a eleccion por variable input
        for linea in archivo_externo:
            palabraxpalabra+=linea.lower()
        carta=palabraxpalabra#remplaza los simbolos
    # print(carta)
    return carta

def remplazar_simbolos(carta):#quita los simbolos de el texto 
    #palabras=carta.strip('\n','!','¡','¿','?',',','.',';',':')
    palabras=carta.replace(",","").replace(".","").replace("_","").replace("!","").replace("?","").replace("¡","").replace("¿","").replace(";","").replace(":","").split() 
    palabras_no_repetidas = []
    for palabra in palabras:#itera y agrega las palabras que no estan el la lista
        if palabra not in palabras_no_repetidas:
            palabras_no_repetidas.append(palabra)
    carta=palabras_no_repetidas
    return carta

def modo_contador(diccionario,carta):#cuenta las palabras que no estan en el diccionario
    contador=0
    for palabra in carta:
        if palabra not in diccionario:
            # print(palabra)
            contador+=1
    return contador

def guardar_palabras_erroneas(diccionario,carta):#gaurda en una lista las palabras que no estan en el diccionario
    palabras_invalidas=""
    for palabra in carta:
        if palabra not in diccionario:
            palabras_invalidas=palabras_invalidas+"\n"+palabra
    return palabras_invalidas


def arreglo_texto(diccionario,palabras_erroneas):#da las tres opciones a cada palabra que no está en el diccionario
    for palabra in palabras_erroneas.split():
        print(f"La palabra {palabra} no se encuentra en el diccionario.\nQue desea hacer?")
        ingreso=input("1. Agregarla al diccionario\n2. Corregir palabra\n3. Ignorar y seguir\n")
        if ingreso == "1":
            diccionario.append(palabra.strip())
        elif ingreso=="2":
            while True:
                palabra_interna=input("Escriba nuevamente la palabra: ")
                palabra=palabra_interna
                print(f"Desea agregar {palabra} al diccionario?\nSi(1) o No(2).")
                opcion=input()
                if opcion=="1":
                    diccionario.append(palabra.strip())
                    break
                elif opcion=="2":
                    break
                else:
                    print("Opcion invalida.")
        elif ingreso=="3":
            pass
        else:
            print("Opción no valida.")

    return diccionario

def conseguir_archivo():#pide el nombre del archivo a importar
    x=input("Ingrese nombre y extencion de archvio.\n")# X es la variable que contiene el nombre del archivo a abrir
    try:
        with open(x) as f:
            x=x
    except FileNotFoundError:
        print(f"No se encuentra el archivo {x}.")
        exit()
    return x

def eleccion_modo(diccionario):#da la opcion de elegir entre los 2 modos
    modo=input("¡Bienvenido al TP1 del curso de programación!\Elija el modo a usar\n1) Modo interactivo\n2) Archivo externo.")
    print(f"Su opción: {modo}")
    if modo=="1":
        programa_interno(diccionario)
    elif modo=="2":
        programa_externo(diccionario)
    else:
        print("Input no valido.")
        eleccion_modo()
    return
# def nuevas_palabras (diccionario,diccionario_final):
#     palabras_agregadas=[]
#     for palabra in diccionario_final:
#         if palabra not in diccionario:
#             palabras_agregadas.append(palabra)
#     return palabras_agregadas

def programa_interno(diccionario):
    carta=modo_interactivo()
    carta=remplazar_simbolos(carta)
    contador = modo_contador(diccionario,carta)
    palabras_erroneas=guardar_palabras_erroneas(diccionario,carta)
    diccionario_final=arreglo_texto(diccionario,palabras_erroneas)
    print(f"Número de palabras desconocidas: {contador}")
    return

def programa_externo(diccionario):
    x=conseguir_archivo()
    carta=leer_archvio_externo(x)
    carta=remplazar_simbolos(carta)
    contador = modo_contador(diccionario,carta)
    palabras_erroneas=guardar_palabras_erroneas(diccionario,carta)
    diccionario_final=arreglo_texto(diccionario,palabras_erroneas)
    print(f"Número de palabras desconocidas: {contador}")
    return

def principal():
    diccionario = leer_diccionario()
    eleccion_modo(diccionario)
        
principal()

# Desarrollado por Marcos Servin