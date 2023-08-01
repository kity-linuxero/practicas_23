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
    

print("¡Bienvenido al TP1 del curso de programación!\nUsted ha ingresado al modo interactivo.")

d = open('spanish.dic','r',encoding="utf-8")
dic = d.read()
d.close()
h = dic.split() #crea una lista con todas las palabras del diccionario

texto = tomar_datos().split()
print("Finalozó la toma de datos")

print(f"Ha finalizado el ingreso de texto.\nEl texto contiene {comparar(texto,h)} palabras que no están en el diccionario.")

# Desarrollado por Mauro Seimandi