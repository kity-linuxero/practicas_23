
# Práctica 2 - Algoritmos y pseudocódigo - Parte II

En esta práctica, seguiremos programando al robot que limpia de la primera práctica. El área a limpiar compuesto por *filas* (horizontales) y *columnas* (verticales). A cada cuadrante llamaremos *baldosas*.

Las instrucciones que entiende el robot son las siguientes:

##### Las instrucciones que entiende el robot son las siguientes:

- `avanzar`: Avanza un lugar hacia adelante.
- `girar_a_derecha:` Gira 90º hacia su derecha.
- `girar_a_izquierda:` Gira 90º hacia su izquierda.
- `limpiar`: Limpia el lugar donde se encuentra posicionado.
- `hay_pared_delante`: El robot consulta a su sensor si hay una pared delante. (`verdadero`/`falso`).
- `imprimir("Mensaje")`: Informará un mensaje cualquiera.
- `esta_limpio`: El robot consulta a su sensor si el lugar donde se encuentra ubicado está limpio (`verdadero`/`falso`)
- `bateria_baja`: El robot consulta a su sensor si queda poca energía. (`verdadero`/`falso`).
- `pos(X,Y)`: Posiciona al robot en una ubicación señalada por `X` (columna) e `Y` (fila). X e Y son números del 1 al 40.


##### Además, se incluyeron las siguientes instrucciones

- `esta_mojado`: El robot consulta a su sensor si el lugar donde está parado está *mojado*.
- `secar`: Seca el lugar donde se encuentra parado.
- `posX`: Nos dirá el número de **columna** donde se encuentra ubicado. Es un número del 1 al 40.
- `posY`: Nos dirá el número de **fila** donde se encuentra ubicado. Es un número del 1 al 40.
- Puede usar todas las <a href="https://programacion.concristian.com.ar/clase2.html#/numericos_aritmetica" target="_blank">operaciones aritméticas</a> vistas en las clases que considere necesarias.
- Puede usar todos los <a href="https://programacion.concristian.com.ar/clase2.html#/numericos_comparacion" target="_blank">operadores de comparación</a> vistas en las clases que considere necesarias.


### A tener en cuenta

- Utilizar comentarios cuando lo vea necesario
- Utilice las variables que considere necesarias.
- Cada vez que se pida informar una baldosa por favor indicar las coordenadas x e y.
- Realice de ser posible los ejercicios en computadora dejando una tabulación (con la tecla tab) para indicar un bloque de código. Si los ejercicios se realizan en papel, por favor tenga muy en cuenta la tabulación para indicar los diferentes bloques de código.
- Los nombres de las variables que sean auto explicativas. Es preferible un nombre de variable su nombre sea explicativo por sí mismo a que sea un nombre corto para ahorrar espacio.
- Especifique el tipo de datos que contendrá cada variable que utilice:
    - Numéricas:
        - `int`: Para números enteros
        - `float`: Para números con parte fraccionarias
    - Lógicas (booleanas): `bool`
    - String: `str`
- Si una baldosa esta mojada **NO** será posible limpiarla hasta que esté seca. El proceso de secado alcanza con solo una instrucción `secar`. Luego de secar una baldosa es probable que quede sucia y sea necesario realizar una limpieza para que quede completamente limpia.


## Ejercicio 1

Escribir un programa que informe la cantidad de veces que fueron necesarias limpiar para que la baldosa `(1,39)` quede completamente limpia.

A continuación se presenta una posible solución, se espera que utilicen la siguiente sintáxis:

```bash
programa pr2_ej1
# variables
int veces=0

# main
pos(1,39)

# Arranca la limpieza
mientras NO (esta_limpio)
    limpiar
    veces = veces +1

imprimir("Fue necesario realizar",veces,"limpiezas")
```

## Ejercicio 2

Escriba un programa que permita al robot que informe _la cantidad_ de baldosas mojadas que encuentre en toda la fila 32.

## Ejercicio 3

Escriba un programa que recorra la columna 23 e informe la cantidad de baldosas que luego de secarlas no fueron necesario limpiar.

>Precond: Existe al menos una baldosa mojada.

## Ejercicio 4

Escriba un programa que recorra la columna 10 hasta encontrar _al menos 2_ baldosas sucias. Pueden no haberlas.
Si encuentra 2 baldosas sucias debe interrumpir el recorrido e informar la posición.

## Ejercicio 5

Escriba un programa que permita recorrer la fila 7 del área realizando la limpieza del piso. Solo hay batería para 20 limpiezas.
Debe informar si las 20 limpiezas disponibles fueron suficientes para limpiar toda la fila o quedaron baldosas sin limpiar.

>Precond: Se sabe que no hay baldosas mojadas.

## Ejercicio 6
Escriba un programa que permita al robot recorrer la columna 2 informando a su paso las baldosas mojadas y las sucias.
No debe secar ni limpiar.

Por ejemplo:
```
La baldosa (2,10) está mojada
La baldosa (2,30) está mojada
La baldosa (2,34) está sucia
```

## Ejercicio 7
Modifique el ejercicio anterior para tener en cuenta el nivel de batería. En caso que se quede con poca batería debe informar `"Se cancela el recorrido por poca batería"`.

## Ejercicio 8
Escriba un programa que permita recorrer el área hasta llegar a una baldosa sucia o mojada. En ese momento debe interrumpir el recorrido e informar donde se quedó ubicado.

>Precond: Seguro existe alguna baldosa sucia o mojada.

## Ejercicio 9
Escriba un programa que permita recorrer el área hasta llegar a una baldosa sucia o mojada. En ese momento debe interrumpir el recorrido e informar donde se quedó ubicado. 

>Precond: Puede no haber una baldosa que esté mojada o sucia.


## Ejercicio 10
Escriba un programa que permita al robot limpiar completamente la fila 34. Al finalizar debe informar la cantidad de baldosas fueron necesarias realizar exactamente 6 limpiezas.

>Precond: NO hay baldosas mojadas en la fila 34.

## Ejercicio 11
Escriba un programa que permita recorrer toda el área contabilizando la cantidad de baldosas sucias que hay.
El recorrido debe hacerlo **sin realizar giros** (ni a derecha ni izquierda).

# Ejercicio 12
Escriba un programa que permita recorrer toda el área de `40x40` informando el estado de cada baldosa. No se debe realizar limpieza, solo informar.

```
La baldosa (1,1) se encuentra limpia
La baldosa (1,2) se encuentra limpia
La baldosa (1,3) se encuentra sucia
La baldosa (1,4) se encuentra limpia
La baldosa (1,5) se encuentra mojada
....
La baldosa (40,40) se encuentra mojada
```
Elija el modo de recorrido que mejor le parezca.


## Ejercicio 13
Escriba un programa que permita al robot recorrer el área buscando baldosas sucias e informe el porcentaje de baldosas que están sucias respecto al total de baldosas. El área es de `40x40`.

Formula porcentaje: $$ x = { \ Sucias \over Total Baldosas} * 100 $$ 


>Precond: NO hay baldosas mojadas en el área.

## Ejercicio 14

Escriba un programa que recorra la fila 29 buscando _exactamente_ 2 baldosas sucias y 3 mojadas que seguro existen. Deben informar a qué columna pertenece la última baldosa sucia o mojada encontrada.

## Ejercicio 15
Escriba un programa que permita recorrer la fila 17 buscando una baldosa sucia que va a llevar exactamente 2 limpiezas seguida por una baldoza mojada. Se sabe que existe dicha baldosa mojada y se debe informar donde está.
El objetivo del programa es buscar esa baldosa mojada en particular y no realizar la limpieza de la fila.


## Ejercicio 16
Escriba un programa que permita realizar una limpieza completa de área de `40x40` y a la vez informar los siguientes datos sobre la limpieza:
- Cantidad total de baldosas sucias
- Cantidad total de baldosas mojadas
- Cantidad total de limpiezas necesarias

>Precond: La batería alcanza para la limpieza total


## Ejercicio 17 (EXTRA)
Modifique el programa anterior para además informar lo siguiente:

- La baldosa que mas costó limpiar (la que llevó mayor cantidad de limpiezas).

Pista:
- Imaginar un mecanismo para llevar la cantidad mayor de limpiezas y que se compare cuando se realice una nueva limpieza y actualizar el valor si es necesario.



-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">


