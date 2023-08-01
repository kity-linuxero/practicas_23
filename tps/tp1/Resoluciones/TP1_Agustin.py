######falta etapa 2 y 3, tampoco trannforma el texto en minusculas.
add_palabra=[]
print("¡Bienvenido al TP1 del curso de programación. Usted ha ingresado al modo interactivo.")
def read_file():
    r_file=open("spanish.dic","r",encoding="utf-8")
    print(r_file.read)
    r=r_file.read

def write_file():
    w_file=open("spanish.dic","a+",encoding="utf-8")
#######################primer etapa###################################################
###detecta y almacena las palabras ingresadas por el usuario, lo convierte en una lista si esta tiene espacios y luego se añade a la variabele para almacenar estas palabras
def detectar_palabras():
    while True:
        palabra=input("ingrese la palabra que desea añadir: ")
        if palabra == "fin":
            break
            
        else:  
            add_palabra.extend(palabra.split())
    print("las palabras añadidas son: ",add_palabra)
    
def detectar_en_dicconario():
    r_file=open("spanish.dic","r",encoding="utf-8")
    palabra_no_encontrada=int()
    palabra_encontrada=int()
    read=r_file.read().split()
    #####################################################
    # for l in add_palabra:
    #     for a in read:
    #         if l==a  :
    #             palabra_encontrada+=1                                          
    #             break
    #     else:
    #         palabra_no_encontrada+=1

    for l in add_palabra:
        if l in read:
            palabra_encontrada+=1
    palabra_no_encontrada = len(add_palabra) - palabra_encontrada

            
    print("palabras encontradas: ",palabra_encontrada)
    print("palabras no figura: ",palabra_no_encontrada)      
    #print(palabra_no_figura)


detectar_palabras()
detectar_en_dicconario()
######falta etapa 2 y 3, tampoco trannforma el texto en minusculas.


# Desarrollado por Agustin Guigovaz