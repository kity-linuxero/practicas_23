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

## Ejercicio 10

Escriba un programa que permita al robot limpiar completamente la fila 34. Al finalizar debe informar la cantidad de baldosas fueron necesarias realizar exactamente 6 limpiezas.

>Precond: NO hay baldosas mojadas en la fila 34.

```
programa ej10
# variables
int cont = 0 # Lleva la cuenta de limpiezas
int limp = 0 # Lleva la cuenta de las baldosas

# Main
pos(1,34)

repetir (40 veces)
	mientras NO (esta_limpio)
		limpiar
		cont = cont + 1
		
	si (cont == 6)
		limp = limp +1
		
	si NO (hay_pared)
		avanzar
	cont = 0

imprimir("La cantidad de baldosas que llevaron 6 son ",cont)


```
### Otra versión
```
## Versión con mientras

programa ej10
# variables
int cont = 0 # Lleva la cuenta de limpiezas
int limp = 0 # Lleva la cuenta de las baldosas

# Main
pos(1,34)

mientras NO (hay_pared)
	mientras NO (esta_limpio)
		limpiar
		cont = cont + 1
		
	si (cont == 6)
		limp = limp +1
		
	avanzar
	cont = 0

mientras NO (esta_limpio)
		limpiar
		cont = cont + 1
		
	si (cont == 6)
		limp = limp +1
```

## Ejercicio 11

Escriba un programa que permita recorrer toda el área contabilizando la cantidad de baldosas sucias que hay.
El recorrido debe hacerlo **sin realizar giros** (ni a derecha ni izquierda).

```
programa ej11

# Variables
int bald_sucias = 0

# MAIN

repetir (40 veces)
	repetir (39 veces)
		si NO (esta_limpio)
			bald_sucias+=1
		avanzar
		
	si NO (esta_limpio)
		bald_sucias+=1
		
	pos(1,posY+1) 
	# Va a la primer columna de la próxima fila
			
```

## Ejercicio 13

Escriba un programa que permita al robot recorrer el área buscando baldosas sucias e informe el porcentaje de baldosas que están sucias respecto al total de baldosas. El área es de `40x40`.

Formula porcentaje: $$x={Sucias \over TotalBaldosas}*100$$ 


>Precond: NO hay baldosas mojadas en el área.

```
programa ej13
# variables
int x = 0 # Cant baldosas sucias

# main

repetir (20 veces)
	repetir (40 veces)
		si NO (esta_limpio)
			x = x+1
		
		si NO (hay_pared)
			avanzar
		
	si NO (esta_limpio)
		x = x+1
	
	girar_derecha
	avanzar
	girar_derecha
	
	repetir (40 veces)
		si NO (esta_limpio)
			x = x+1
		
		si NO (hay_pared)
			avanzar
		
	si NO (esta_limpio)
		x = x+1
	
	girar_izquierda

	si NO (hay_pared)
		avanzar
		girar_izquierda
		
y = (x/1600)*100

imprimir ("El",y,"% de baldosas están sucias")
print (f"El {y}% de baldosas están sucias")

```

#### Otra versión

```
programa ej13_v2

# Variables
int bald_sucias = 0

# MAIN

repetir (40 veces)
	repetir (39 veces)
		si NO (esta_limpio)
			bald_sucias+=1
		avanzar
		
	si NO (esta_limpio)
		bald_sucias+=1
		
	pos(1,posY+1) 
	# Va a la primer columna de la próxima fila
	
y = (bald_sucias/1600)*100
imprimir (f"El {y}% de baldosas están sucias") 
```

## Ejercicio 16

Escriba un programa que permita realizar una limpieza completa de área de `40x40` y a la vez informar los siguientes datos sobre la limpieza:
- Cantidad total de baldosas sucias
- Cantidad total de baldosas mojadas
- Cantidad total de limpiezas necesarias

>Precond: La batería alcanza para la limpieza total
programa ej16

# Variables
int cant_moj = 0
int cant_suc = 0
int cant_limpiezas = 0

# MAIN

repetir (40 veces)
	repetir (40 veces)
		si (esta_mojado)
			cant_moj +=1
			secar
			
		si NO (esta_limpio)
			cant_suc +=1
			
			mientras NO (esta_limpio)
				limpiar
				cant_limpiezas+=1
		si NO (hay_pared)
			avanzar
			
	pos(1,posY+1) 
	# Va a la primer columna de la próxima fila
	
imprimir (blabla)
-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">