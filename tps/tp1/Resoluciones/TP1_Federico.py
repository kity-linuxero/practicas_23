def cargar_diccionario(nombre_archivo):
    diccionario = []
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            palabra = linea.strip()
            diccionario.append(palabra)
    return diccionario

def contar_palabras_desconocidas(diccionario, texto):
    palabras_desconocidas = []
    for palabra in texto.split():
        if palabra not in diccionario:
            palabras_desconocidas.append(palabra)
    return palabras_desconocidas

def agregar_palabra_al_diccionario(diccionario, palabra):
    diccionario.append(palabra)

def corregir_palabra(palabras_desconocidas, palabra, nueva_palabra):
    palabras_desconocidas.remove(palabra)
    palabras_desconocidas.append(nueva_palabra)

def mostrar_opciones(palabra_desconocida):
    print("Palabra desconocida:", palabra_desconocida)
    print("Opciones:")
    print("1. Agregarla al diccionario")
    print("2. Corregir palabra")
    print("3. Ignorar y seguir")

def ingresar_texto_interactivo():
    texto = ""
    print("Ingresa el texto línea por línea (escribe '@fin' en una línea para terminar):")
    while True:
        linea = input()
        if linea == "@fin":
            break
        texto += linea + "\n"
    return texto

def cargar_texto_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        texto = archivo.read()
    return texto

nombre_archivo_diccionario = "spanish.dic"  

print("¡Bienvenido al TP1 del curso de programación!")
print("Selecciona una opción:")
print("1. Modo interactivo")
print("2. Archivo externo")

opcion = input("Ingresa la opción: ")

if opcion == "1":
    texto = ingresar_texto_interactivo()
elif opcion == "2":
    nombre_archivo_texto = input("Ingresa el nombre del archivo de texto: ")
    texto = cargar_texto_desde_archivo(nombre_archivo_texto)
else:
    print("Opción inválida. El programa se cerrará.")
    exit()

diccionario = cargar_diccionario(nombre_archivo_diccionario)
palabras_desconocidas = contar_palabras_desconocidas(diccionario, texto)

print("La cantidad de palabras desconocidas es:", len(palabras_desconocidas))

for palabra_desconocida in palabras_desconocidas:
    mostrar_opciones(palabra_desconocida)
    opcion = input("Ingresa la opción para la palabra desconocida: ")
    if opcion == "1":
        agregar_palabra_al_diccionario(diccionario, palabra_desconocida)
    elif opcion == "2":
        nueva_palabra = input("Ingresa la palabra corregida: ")
        corregir_palabra(palabras_desconocidas, palabra_desconocida, nueva_palabra)
    elif opcion == "3":
        continue
    else:
        print("Opción inválida. La palabra será ignorada y se seguirá con el programa.")

print("El diccionario actualizado es:", diccionario)


# Desarrollado por Federico Gigena