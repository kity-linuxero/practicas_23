
# Práctica 4 - Listas y función random

## Función random

En los lenguajes de programación, por lo general contamos con una herramientas para generar datos aleatorios.
El Python se usa la función `random`.

#### Importación de módulos

Para complementar las funciones _built-in_ (las que vienen incorporadas) a veces es necesario de hacer uso de librerías o módulos de terceros o bien desarrolladas por el equipo de desarrollo propio del lenguaje, pero que por defecto no las trae habilitadas.

Para importar módulos se usa la instrucción `import`. Es un tema que veremos en mas detalles adelante pero para hacer un resumen, una vez que importamos el módulo podemos hacer uso de sus funciones.

Si queremos usar todas las funciones que brinda _random_ en Python la instrucción es la siguiente:

```python
import random
```

Por lo general, las importaciones se hacen al principio del archivo de código para que estén listas para usar en cualquier momento.

### Generar números enteros de forma aleatoria

Para generar números enteros aleatorios se usa la función `randint()` que se incluye en random. En dicha función se le envían dos parámetros, el número de donde empieza y donde termina. Por lo que la función `randint()` generará un número aleatorio entre esos dos. Es importante aclarar que esos números SÍ están incluídos en la generación de los números.

```python
import random

num = random.randint(0, 99) # Desde 0 hasta 99 inclusives
print (num)
```

La segunda línea del código, usará la función `randint` de `random` para generar aleatoriamente números tipo int. La función random puede generar varios tipos de datos. Puede ver una lista de funciones que posee el módulo random [aquí](https://www.w3schools.com/python/module_random.asp).

También es posible invocar solo la función que vamos a usar, por ejemplo si solo vamos a usar para generar números enteros random podemos simplificar la importación de la siguiente manera:

```python

from random import randint

num = randint(0, 99)
print (num)
```
El código es exactamente lo mismo que arriba, pero se simplificará cada vez que tengamos que llamar a la función random porque directamente escribimos `randint()` y no tenemos que invocar toda la función del módulo `random.randint()`.


### Random para listas

Hay opciones random para usar en listas, por ejemplo que nos dé un elemento aleatorio de una lista o el orden se cambie de forma aleatoria.

#### Obtener un elemento aleatorio

```python
import random

lista = ["auto", "casa", "moto"]

elem = random.choice(lista) 

print("El elemento elegido es",elem) 

```

Si corremos el programa varias veces veremos que el elemento elegido cambia.

#### Cambiar el orden en una lista

```python
import random

lista = ["auto", "casa", "moto"]

random.shuffle(lista) 

print("La lista quedó así",lista) 
```

Al correr el programa varias veces veremos que el orden cambia. A tener en cuenta, el método `suffle()` desordena la lista y ya no es posible recuperarla en el orden anterior.

Más métodos random [aquí](https://www.w3schools.com/python/module_random.asp)

## Parte práctica

## Ejercicio 1

Escriba un programa que genere números aleatorios entre 1 y 10 e imprima el resultado.

## Ejercicio 2

Escriba un programa que le pida al usuario que ingrese un número del 1 al 6 y simule la función que se lanza un dado usando la función random. El programa debe seguir hasta que el usuario acierte el número.

```
Elija un número del 1 al 6: 3
Se lanza el dado...
Salió el número 4

Elija un número del 1 al 6: 1
Se lanza el dado...
Salió el número 6

Elija un número del 1 al 6: 5
Se lanza el dado...
Salió el número 5, ¡Felicitaciones!
```

## Ejercicio 3

Modifique el ejercicio anterior con las siguientes mejoras:

- Compruebe que lo que envía el usuario sea realmente un número.
- Compruebe que los números sean del 1 al 6. Sino, debe pedirle nuevamente que elija.

Pistas:

- El método [`isnumeric()`](https://www.w3schools.com/python/ref_string_isnumeric.asp) de los [String methods](https://www.w3schools.com/python/python_ref_string.asp) puede ayudarle.

Ejemplo:

```
Elija un número del 1 al 6: P
Elija un número del 1 al 6: 90
Elija un número del 1 al 6: 4
Se lanza el dado...
...
```

## Ejercicio 4

Siguiendo los ejemplos anteriores escriba un juego para jugar piedra, papel o tijeras.

Ejemplos:

```
Elija una opción:
1) Piedra
2) Papel
3) Tijera.

Su opción: 3

¡Perdiste! Yo elegí piedra XD
```

```
Elija una opción:
1) Piedra
2) Papel
3) Tijera.

Su opción: 3

¡Ganaste! Yo elegí papel :(
```

Imagine la mejor manera de realizar el juego utilizando todas vistas hasta el momento en el curso.

## Ejercicio 5

Modificar el programa anterior de piedra, papel y tijera de manera que se juegue varias veces (hasta que el usuario decida no jugar mas) y una vez terminado cuente la cantidad de victorias y derrotas que tuvo con respecto a la computadora.


# Listas

## Ejercicio 6
Escriba un programa que genere una lista con números consecutivos del 1 al 1000 y luego la imprima por pantalla.

```
[1,2,3,4 ... 1000]
```

## Ejercicio 7

Escriba un programa que genere una lista de 100 elementos con números enteros aleatorios entre -1000 y 1000. Y luego informe la suma y el promedio de todos los elementos de la lista.

Realice el programa con dos variantes:

- Realizando la suma de todos los números de la lista y realizando la división.
- Usando las funciones `sum()`.*

*Pista en este [link](https://www.mycompiler.io/view/HeOQCUJ51Pu)

## Ejercicio 8
Hacer un programa que, luego de crearse la lista de los 100 elementos del ejercicio anterior, informe el mayor y el menor de la lista.

Realice el programa con dos variantes:

- Recorriendo la lista usando máximos y mínimos como vimos hasta ahora.
- Usando la función `max()` y `min()` *

*Pista en este [link](https://www.mycompiler.io/view/FKobivFxFtP)

## Ejercicio 9
Realizar un programa que realice una lista de longitud 10 con números aleatorios e imprima la lista por pantalla. Luego la imprima ordenada de menor a mayor y luego la imprima de mayor a menor.

Pista en este [link](https://programacion.concristian.com.ar/clase4.html#/4/6)

## Ejercicio 10

Realizar un programa que, dada la lista del ejercicio 7, genere una nueva lista con solo números impares y debe imprimir por pantalla la nueva lista.

Los números no deben generarse nuevamente.

## Ejercicio 11
Escriba un programa que tome por teclado la temperatura media de cada día de la semana. Una vez tomados los datos que deben ser ingresados por teclado, debe informar la temperatura máxima y la mínima y qué día ocurrió cada una y el promedio de temperatura de la semana.

```
Ingrese temperatura media en el día domingo: 23.4
Ingrese temperatura media en el día lunes: 21.0
Ingrese temperatura media en el día martes: 18.3
Ingrese temperatura media en el día miércoles: 16.4
Ingrese temperatura media en el día jueves: 17.9
Ingrese temperatura media en el día viernes: 15.6
Ingrese temperatura media en el día sábado: 15.4

La máxima se dió el día domingo, con 23.4 ºC
La mínima se dió el día sábado, con 15.4 ºC
La temperatura promedio de la semana fue: 18.28 ºC
```

Pista: Haga una lista con los días de la semana e itere sobre esa lista. ;)

## Ejercicio 12

Escriba un programa que permita escribir una lista de n palabras. Al inicio del programa se le preguntará al usuario la cantidad de palabras que va a ingresar y luego se ingresarán ese número de palabras por teclado.

Al final debe imprimir la lista de palabras en orden alfabético.

```
Ingrese el número de palabras que desea procesar: 6
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Barcos
Ingrese palabra 5: Aviones
Ingrese palabra 6: Peaones

La lista es: ['Aviones', 'Barcos', 'Camiones', 'Peatones', 'Tractores', 'Trenes']

```

## Ejercicio 13

Modifique el programa anterior agregando la opción de cuenta palabras. Al finalizar el programa y luego de imprimir la lista pregunte qué palabra le gustaría buscar en la lista. Luego debe contar la cantidad de veces que aparece dicha palabra.

```
Ingrese el número de palabras que desea procesar: 7
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Barcos
Ingrese palabra 5: Aviones
Ingrese palabra 6: Peatones
Ingrese palabra 7: Barcos

La lista es: ['Aviones', 'Barcos', 'Barcos', 'Camiones', 'Peatones', 'Tractores', 'Trenes']

Ingrese la palabra que desea buscar: Barcos

La palabra Barcos aparece 2 veces
```

## Ejercicio 14

Modifique el programa anterior para que el programa contenga una lista _predefinida_ por el programador de palabras _no válidas_ o _prohibidas_ para ingresar.

```
Ingrese el número de palabras que desea procesar: 7
Ingrese palabra 1: Trenes
Ingrese palabra 2: Camiones
Ingrese palabra 3: Tractores
Ingrese palabra 4: Gatos
La palabra "Gatos" está en la lista de palabras prohibidas. Por favor elija otra.
Ingrese palabra 4: Barcos
Ingrese palabra 5: Aviones
Ingrese palabra 7: Peatones

La lista es: ['Trenes', 'Camiones', 'Tractores', 'Barcos', 'Aviones', 'Peatones']
.......

```
-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">
