def eliminar_caracteres(palabra):
    special_chars=[",",".",":","¿","?","¡","!","(",")"]
    limpiar_palabra=palabra
    for i in special_chars:
        limpiar_palabra=limpiar_palabra.replace(i,"")
    return limpiar_palabra


def contiene_palabra(palabra):
    with open('spanish.dic','r',encoding='UTF-8')as archivo:
        archivo_completo=archivo.readlines()
        archivo_limpio = [i.replace('\n', '') for i in archivo_completo]
    return palabra in archivo_limpio
    
def tomar_cadena():
    ingresado=""
    lista_cadena=[]
    print("Usted ha ingresado al modo interactivo.\n")
    while ingresado!="@fin":
        ingresado=input(">")
        lista_cadena.append(ingresado)
    lista_cadena.pop()
    return lista_cadena

def chequear_palabra(lista_cadenas):
    for i in lista_cadenas:
        palabra_extraida=i.split()
        for i in palabra_extraida:
            sin_chars=eliminar_caracteres(i)
            while not contiene_palabra(sin_chars):
                print(f'La palabra {sin_chars} no se encuentra en el diccionario\n¿Qué desea hacer?')
                accion=palabra_invalida()
                if accion=='1':
                    agregar_dic(sin_chars)
                elif accion=='2':
                    sin_chars=corregir_palabra(sin_chars,opcion,filename)
                elif accion=='3':
                    break

def tomar_archivo(filename):
    try:
        with open(filename) as f:
            completo=f.readlines()
    except FileNotFoundError:
        print(f"No se encuentra el archivo {filename}.")
        exit()
    return completo

def palabra_invalida():
    print('1. Agregarla al diccionario\n2. Corregir palabra\n3. Ignorar y seguir')
    opcion=input('Su opción: ')
    return opcion

def agregar_dic(palabra):
    with open('spanish.dic','a',encoding='UTF-8')as f:
        f.write(palabra+'\n')
    print('La palabra fue ingresada al diccionario con éxito.')

def corregir_palabra(palabra_vieja,opcion,archivo):
    corregida=input('Escriba nuevamente la palabra: ')
    if opcion=='2':
        with open(archivo,'r',encoding='UTF-8')as file:
            filedata = file.read()
            filedata = filedata.replace(palabra_vieja,corregida)
        with open(archivo, 'w', encoding='UTF-8') as file:
            file.write(filedata)
    return corregida



print('¡Bienvenido al TP1 del curso de programación!')
print('1) Modo interactivo\n2) Archivo externo')
opcion=input('Su opción: ')
filename=''
if opcion=='1':
    texto=tomar_cadena()
elif opcion=='2':
    filename=input('Escriba el nombre del archivo: ')
    texto=tomar_archivo(filename)
print('Ha finalizado el ingreso de texto.')
chequear_palabra(texto)
print('El texto no contiene palabras que no están en el diccionario.')


# Desarrollado por Agata Rumi