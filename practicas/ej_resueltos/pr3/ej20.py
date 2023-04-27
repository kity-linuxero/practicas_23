# Ejercicio de los promedios

# tres notas todas >= 6 para promocionar
nota1=float(input("Ingrese nota primer examen: "))
nota2=float(input("Ingrese nota segundo examen: "))
nota3=float(input("Ingrese nota tercer examen: "))

# >= 8 promoción
promedio = (nota1+nota2+nota3)/3 >= 8
notas = nota1 >= 6 and nota2 >= 6 and nota3 >=6

if promedio and notas:
    print("¡SE PROMOCIONÓ!")
else:
    print("NO se promocionó")





