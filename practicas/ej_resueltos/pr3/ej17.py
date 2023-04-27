# Se ingresan palabras y se debe informar la palabra mas corta y mas larga
# len("Hola") o len(zaraza)

corta = larga = palabra = input("Ingrese una palabra: ")

while palabra.upper() != "FIN":
    if len(palabra) < len(corta):
        corta = palabra
    elif len(palabra) > len(larga):
        larga = palabra
    palabra = input("Ingrese una palabra: ")

print(f"La palabra mas corta es {corta}\nLa palabra mas larga es {larga}")