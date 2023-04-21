n = int(input("Ingrese un número: "))
suma = 0

for i in range(n):
    suma = suma + (i+1)
    
print(f"La suma de los primeros n números naturales es: {suma}")

# Con la fórmula

suma = (n*(n+1))/2
print(f"La suma con la formula da: {int(suma)}")

