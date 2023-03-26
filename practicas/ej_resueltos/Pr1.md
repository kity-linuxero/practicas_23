# Práctica 1 - Ejercicios resueltos

> Ejercicios resueltos en clase.



## Ejercicio 2 

Escribir un algoritmo que solo limpie la segunda fila y vuelva a la posición original.

![](../img/pr1/aspiradora_2da_fila.png)

```
programa ej_2
  imprimir ("Iniciar programa")
  girar_a_la_derecha
  avanzar
  girar_a_la_izquierda
  
  repetir (2 veces)
	limpiar
	avanzar
  
  limpiar
  imprimir ("Iniciando la vuelta")
  girar_a_izquierda
  avanzar
  girar_a_izquierda

  repetir (2 veces)
    avanzar
  
  imprimir ("Finalizo")
  repetir (2 veces)
    girar_a_izquierda
```

## Ejercicio 4


Escribir un algoritmo que permita al robot realizar la limpieza con el siguiente recorrido.

![](../img/pr1/aspiradora_ej3.png)


```
programa ej_4
  imprimir ("Comienza recorrido")
  girar_derecha
  repetir (2 veces)
    limpiar
    avanzar
  girar_a_izquierda
  limpiar
  avanzar
  girar_a_izquierda
  repetir (2 veces)
    limpiar
    avanzar
  girar_a_derecha
  limpiar
  avanzar
  girar_a_derecha
  repetir (2 veces)
    limpiar
    avanzar
  limpiar
  imprimir ("FInalizó la limpieza")
fin programa
```

## Ejercicio 7

Escriba un algoritmo que permita al robot limpiar un área de `40x40`, pero solamente limpie los lugares que es necesario, consultando a su sensor con la instrucción `esta_limpio`. Si el la posición donde se encuentra está limpia debe avanzar a la siguiente sin realizar la limpieza.

- :bulb: Puede ser útil utilizar <a href="https://programacion.concristian.com.ar/clase1.html#/condicionales_negativas" target="_blank">condiciones negativas</a>

![](../img/pr1/aspiradora_random.png)

```
programa ej_7
   imprimir("Iniciar limpieza")
   girar_a_derecha
   repetir (20 veces)
	repetir (39 veces)
		si NO (esta_limpio)
			limpiar
		avanzar
	si NO (esta_limpio)
		limpiar
	girar_a_izquierda
	avanzar
	girar_a_izquierda
	repetir (39 veces)
		si NO (esta_limpio)
			limpiar	
		avanzar
	girar_a_derecha
	
	si NO (esta_limpio)
		limpiar
	si NO (hay_pared)
		avanzar
		girar_a_derecha
	
   imprimir ("FIN!")
```

## Ejercicio 8

Escriba un algoritmo que permita recorrer las primeras 5 filas limpiando completamente todas las baldosas de las filas. El área es de `40x40`.

```
programa  ejercicio8
   imprimir("Se inicia la limpieza")
   
   repetir (2 veces)
     repetir (39 veces)
         mientras NO (esta_limpio)
            limpiar
         avanzar
      mientras NO (esta_limpio)
         limpiar
      girar_a_derecha
      avanzar
      girar_a_derecha
      
     repetir (39 veces)
        mientras NO (esta_limpio)
           limpiar
         avanzar
      mientras NO (esta_limpio)
         limpiar
       
      girar_a_izquierda
      avanzar
      girar_a_izquierda

   repetir (39 veces)
      mientras NO (esta_limpio)
         limpiar
      avanzar
   mientras NO (esta_limpio)
      limpiar   
   
   imprimir ("termino")
fin_programa	
```

## Ejercicio 9

Escriba un algoritmo que permita recorrer al robot la fila 17 limpiando completamente solo las baldosas de columnas impares. Como se desconoce el área a limpiar, el recorrido termina cuando tenga enfrente una pared.

```
programa pr1_ej_9
	imprimir("Los impares de la 17")
	girar_a_derecha
	repetir (16 veces)
		avanzar
	girar_a_izquierda
	
	mientras NO (hay_pared_delante)
		mientras NO (esta_limpio)
			limpiar
		repetir (2 veces)
			si NO (hay_pared_delante)
				avanzar
	mientras NO (esta_limpio)
		limpiar
```

## Ejercicio 11

Escriba un algoritmo que permita al robot recorrer el perímetro del área de la que se desconoce el tamaño realizando la limpieza completamente.

![](../img/pr1/aspiradora_perimetro.png)

```
programa ej_11
		
	repetir (4 veces)
		mientras NO (hay_pared_delante)
			mientras NO (esta_limpio)
				limpiar
			avanzar
		girar_a_derecha
		
	# Por si es de 1x1.
	mientras NO (esta_limpio)
		limpiar
```

## Ejercicio 12

Escriba un programa que permita al robot limpiar la ubicación `(4,38)`. Si la ubicación requería limpieza debe informar _"Se realizó la limpieza"_. Si no requería limpieza, debe informar _"No fue necesaria la limpieza."_

```
programa ej_12
	pos(4,38)
	si (esta_limpio)
		imprimir ("No fue necesaria la limpieza")
	sino
		mientras NO (esta_limpio)
			limpiar
		imprimir ("Se realizó la limpieza)
```
#### Otra versión
```
programa ej_12_v2
	pos(4,39)
	si NO (esta_limpio)
		mientras NO (esta_limpio)
			limpiar
		imprimir ("Se realizó la limpieza")
		
	sino
		imprimir ("No fue necesaria la limpieza")
```

## Ejercicio 13
Escriba un programa que permita al robot recorrer limpiando las baldosas en fila `30` desde la columna `8` hasta la columna `23`.
Para ahorrar energía, no limpia si la baldosa se encuentra limpia.

```
programa ej_13
	pos(30,8)
	repetir(15 veces)
		mientras NO (está_limpio)
			limpiar
		avanzar
```

## Ejercicio 14

Escriba un programa que permita al robot recorrer la columna `23` limpiando las baldosas a su paso hasta que queden limpias. Si en algún momento se queda con poca batería, debe seguir recorriendo la columna pero sin limpiar.

```
programa ej_14
	pos(1,23)
	girar_a_derecha
	mientras NO (hay_pared)
		si (bateria_baja)
			avanzar
		sino
			mientras NO (esta_limpia)
				limpiar
			avanzar
	si NO (bateria_baja)
		mientras NO (esta_limpia)
			limpiar
```

### Otra versión

```
programa ej_14_v2
	pos(1,23)
	girar_a_derecha
	repetir (40 veces)
	  mientras NO (bateria_baja) y NO (esta_limpio)
	  	limpiar
	  si NO (pared_delante)
	     avanzar
```