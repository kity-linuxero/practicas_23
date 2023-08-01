
def tomar_datos():
    x =''
    while not '@fin' in x.lower():
        y = input()
        x = x + y +'\n'
    x = x.replace('@fin', '')
    return(x)


def comparar(x,h):
    z = 0 #cantidad de palabras que no se encuentran en el diccionario
    for l in x:
        if l not in h:
            z = z+1
            print(l)
    return(z)

print("¡Bienvenido al TP1 del curso de programación!")

dic=''
try:
    d = open('spanish.dic','r',encoding="utf-8")
    dic = d.read()
    d.close()
except FileNotFoundError:
        print(f"No se encuentra el archivo de diccionario")
        exit()
        
h = dic.split() #crea una lista con todas las palabras del diccionario

a = ''
while not ((a=="1") or (a=="2")):
    a = input("Elija una opción:\n1) Modo interactivo\n2) Archivo externo\n")

texto=''

if a == "1":
    texto = tomar_datos().split()
else:
    a=input("Escriba el nombre del archivo:\n")
    try:
        b = open(a, 'r', encoding="utf8")
        c = b.read().lower()
        b.close()
    except FileNotFoundError:
        print(f"No se encuentra el archivo {a}.")
        print("El programa ha finalizado")
        exit()
        
    texto = c.split() #crea una lista con las palabras del texto

print(f"Ha finalizado el ingreso de texto.\nEl texto contiene {comparar(texto,h)} palabras que no están en el diccionario.")

# Desarrollado por Mauro Seimandi