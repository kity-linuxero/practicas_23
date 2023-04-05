# Práctica 2 - Ejercicios resueltos

> Ejercicios resueltos en clase.

## Ejercicio 5

Escriba un programa que permita recorrer la fila 7 del área realizando la limpieza del piso. Solo hay batería para 20 limpiezas.
Debe informar si las 20 limpiezas disponibles fueron suficientes para limpiar toda la fila o quedaron baldosas sin limpiar.

>Precond: Se sabe que no hay baldosas mojadas.

##### Resolución

```
# En este programa se intenta cubrir los tres casos posibles,
# 1) Que no alcancen la cantidad de limpiezas disponibles
# 2) Que sobren la cantidad de limpiezas
# 3) Que la cantidad de limpiezas alcance justo

programa ej5
# variables
totales = 20 # Limpiezas disponibles
hechas = 0 # Limpiezas hechas

#main
pos(1,7) # Se ubica

mientras NO (hay_pared) Y hechas < totales
	mientras NO (esta_limpio) Y hechas < totales
		limpiar
		limpiezas_hechas = limpiezas_hechas+1
	avanzar
	
# Ultima baldosa
si (hay_pared) Y hechas < totales
	mientras NO (esta_limpio) Y hechas < totales
		limpiar
		limpiezas_hechas = limpiezas_hechas+1

si hechas == totales
	mientras (esta_limpio) Y NO (hay_pared)
		avanzar
	si NO(esta_limpio)
		imprimir("NO alcanzaron")
	sino
		imprimir("Fueron suficientes")
sino
	imprimir("Fueron suficientes")

fin_programa
```

## Ejercicio 6
Escriba un programa que permita al robot recorrer la columna 2 informando a su paso las baldosas mojadas y las sucias.
No debe secar ni limpiar.

Por ejemplo:
```
La baldosa (2,10) está mojada
La baldosa (2,30) está mojada
La baldosa (2,34) está sucia
```

##### Resolución

```
programa pr2_ej6
# variables

# main

pos(2,1)
girar_derecha

repetir (40 veces)
	si (esta_mojado)
		imprimir("La baldosa (posX,posY) está mojada")
	sino 
		si NO (esta_limpio)
			imprimir("La baldosa (posX,posY) está sucia")
	si NO (hay_pared)
		avanzar
fin_programa
```
-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">