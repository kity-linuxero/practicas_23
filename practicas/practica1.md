
# Práctica 1 - Algoritmos y pseudocódigo - Parte I

> Esta práctica tiene como objetivo guiar al alumnx en los conceptos teóricos de algoritmos.

Para la realización de esta práctica, imaginemos que estamos escribiendo el software de un robot-aspiradora que debe limpiar un área.

##### Las instrucciones que entiende el robot son las siguientes:

- `avanzar`: Avanza un lugar hacia adelante.
- `girar_a_derecha:` Gira 90º hacia su derecha.
- `girar_a_izquierda:` Gira 90º hacia su izquierda.
- `limpiar`: Limpia el lugar donde se encuentra posicionado.
- `hay_pared_delante`: El robot consulta a su sensor si hay una pared delante. (`verdadero`/`falso`).
- `imprimir("Mensaje")`: Informará un mensaje cualquiera.
- `esta_limpio`: El robot consulta a su sensor si el lugar donde se encuentra ubicado está limpio (`verdadero`/`falso`)


#### Convenciones a utilizar:

- El área a limpiar (a menos que se indique lo contrario) será de `3x3`, como lo muestra la siguiente imágen.

![Aspiradora 3x3](img/pr1/aspiradora_3x3.png)

- Un programa comienza con `programa <nombre_programa>` y finaliza con `fin programa`.

- Una **condición** debe poder evaluarse como `verdadera/falsa`.

- Para la estructura de control de [**selección**](https://programacion.concristian.com.ar/clase1.html#/est_control_seleccion) se usarán las palabras claves `si(condicion)` y `sino`.

- Para la estructura de control de [**repetición**](https://programacion.concristian.com.ar/clase1.html#/est_control_repeticion) se usará la palabra clave `repetir(X veces)`. `X` es la cantidad de veces que se repetirá. Por ejemplo: `repetir (3 veces)`.

- Para la estructura de control de [**iteración**](https://programacion.concristian.com.ar/clase1.html#/est_control_iteracion) se usará la palabra clave `mientras(condicion)`.

- Para informar algo, usaremos la palabra clave `imprimir` y entre paréntesis y comillas el mensaje que queramos informar, por ejemplo `imprimir("Mensaje a informar")`.
- El robot siempre se encuentra posicionado en la primer ubicación mirando hacia la derecha.

## Ejercicio 1

Escriba un algoritmo que permita limpiar toda la primer fila. 

```
programa ejercicio_1

    imprimir("Se iniciará la limpieza de la primer fila")

    repetir (2 veces)
        limpiar
        avanzar
    limpiar

    imprimir("Finalizó la limpieza requerida.")

fin programa
```

Al finalizar el programa, el estado debería ser el siguiente:

![](img/pr1/aspiradora_fila.png)

## Ejercicio 2 

Escribir un algoritmo que solo limpie la segunda fila y vuelva a la posición original.

![](img/pr1/aspiradora_2da_fila.png)

## Ejercicio 3

Escribir un algoritmo que permita al robot realizar la limpieza con el siguiente recorrido.

![](img/pr1/aspiradora_ej2.png)

## Ejercicio 4

Escribir un algoritmo que permita al robot realizar la limpieza con el siguiente recorrido.

![](img/pr1/aspiradora_ej3.png)

## Ejercicio 5

Escribir un algoritmo que permita al robot limpiar toda un área del que se desconoce el tamaño. Usando el recorrido del ejercicio 3.

![](img/pr1/aspiradora_big.png)

## Ejercicio 6

Escribir un algoritmo que permita al robot limpiar toda un área del que se desconoce el tamaño. Usando el recorrido del ejercicio 4.

## Ejercicio 7

Escriba un algoritmo que permita al robot limpiar un área del que se desconoce el tamaño, pero solamente limpie los lugares que es necesario, consultando a su sensor con la instrucción `esta_limpio`. Si el la posición donde se encuentra está limpia debe avanzar a la siguiente sin realizar la limpieza.

![](img/pr1/aspiradora_random.png)


##### Programación 2023 - Centro de Formación Profesional 410 La Plata - Compañero Omar Núñez


-----

![](img/foot_logos.png)

