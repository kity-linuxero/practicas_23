
# Práctica 3 - Introducción a Python

Para esta práctica puede usar algún intérprete Python Online o bien hacerlas en algún IDE como Visual Studio Code, Pycharm, etc.

Algunos intérprete online:
- <a href="https://www.programiz.com/python-programming/online-compiler/" target="_blank">Programiz</a>
- <a href="https://www.mycompiler.io/es/new/python" target="_blank">My compiler</a>
- <a href="https://www.online-python.com/" target="_blank">Python Online</a>



## Ejercicio 1

Escriba un programa en Python que imprima por pantalla `¡Hola mundo!`.

## Ejercicio 2

Escriba un programa que le solicite su nombre e imprima por pantalla un `¡Hola <NOMBRE>! Bienvenido al curso de programación.`.

Ejemplo de programa:

```
Escriba su nombre: Cristian
¡Hola Cristian! Bienvenido al curso de programación.
```

## Ejercicio 3

Escriba un programa que pida los datos nombre, apellido y correo electrónico y luego imprima los datos por pantalla.

```
Bienvenidx. A continuación escriba sus datos.

Nombre: Juan
Apellido: Gómez
email: juan.gomez@argentina.com

Sus datos ingresados son
Nombre: Juan
Apellido: Gómez
Mail: juan.gomez@argentina.com
```

Trate de respetar los espacios para que quede ordenado y sea legible.

## Ejercicio 4

Escriba un programa que ingrese dos números y devuelva la suma de ellos.

```
Ingrese los valores
Primero: 78
Segundo: 2

Resultado de la suma 80
```

## Ejercicio 5

Escriba un programa que solicite al usuario que ingrese dos números e imprima el mayor de ellos.

```
Escriba el primer número: 6
Escriba el segundo número: 76

El número ingresado 76 es mayor que 6.
```



## Ejercicio 6

Escribir un programa que pida al usuario un número entero e imprima por pantalla su doble y su triple.

```
Ingrese un número: 20
Su doble es: 40
Su triple es: 60
```

## Ejercicio 7

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.

```
Ingrese un número: 20
El número es positivo
```

```
Ingrese un número: -20
El número es negativo
```

```
Ingrese un número: 0
El número es cero
```

## Ejercicio 8

Escribir un programa que pida al usuario dos números y muestre por pantalla el resultado de sumar, restar, multiplicar y dividir ambos números como muestra el siguiente ejemplo.

```
Ingrese un número: 2
Ingrese otro número: 5

La suma es (2+5)= 7
La resta es (2-5)= -3
El producto es (2*5)= 10
La división es (2/5)= 0.4 

```

## Ejercicio 9
Escriba un programa que pregunte cuántas horas trabajó y el coste por hora. Después debe mostrar por pantalla la paga que corresponde.

```
Horas trabajadas: 8
Coste por hora: 500
La paga correspondiente es: 4000
```

## Ejercicio 10

Escriba un programa que, ingresado un número diga si es par o impar.

Pistas:
- El módulo del número y 2 debe ser 0.
- <a href="https://programacion.concristian.com.ar/clase2.html#/numericos_aritmetica" target="_blank">Operaciones sobre números</a>

## Ejercicio 11

Escriba un programa que lea por teclado nombres de personas hasta que llega "Juan". En el momento que llega "Juan" el programa debe informar la cantidad de personas que llegaron.

Ejemplo:
```bash
Ingrese el nombre:
Marcos
Ingrese el nombre:
Franco
Ingrese el nombre:
Celeste
Ingrese el nombre:
Juan
Llegaron 4 personas
```


## Ejercicio 12

Escribir un programa que pida al usuario 10 números y calcule la suma y el promedio de todos.

## Ejercicio 13

Escribir un programa que pida al usuario una serie de números y muestre por pantalla el número más grande y el número más pequeño de la lista.

La lista de números termina cuando se ingresa el número `0`.

```
Ingrese un número: 2
Ingrese un número: 20
Ingrese un número: 99
Ingrese un número: 32
Ingrese un número: 0

El número mayor de los ingresados es: 99
El número menor de los ingresados es: 2
```
## Ejercicio 14

Escribir un programa que pida al usuario un número entero y muestre por pantalla su tabla de multiplicar hasta 10.
Por ejemplo:

```
Ingrese un número: 7
7x1 = 7
7x2 = 14
7x3 = 21
...
7x10 = 70
```

## Ejercicio 15

Escriba un programa que espere un número ingresado `n` por el usuario e imprima en pantalla la suma de los primeros `n números` naturales.
Por ejemplo, si se ingresa el número 5, el programa debe imprimir en pantalla la suma de : `1+2+3+4+5`.

```bash
Ingrese un número: 5

La suma es de los primeros 5 números naturales es 15
```

Realizar dos versiones para este programa:

- Hacerlo con iteraciones y teniendo un contador.

- Mejorar el programa y realizar la suma de los primeros n números naturales con la fórmula matemática:

$$x={n(n+1) \over 2}$$ 

Pista: Las operaciones entre números soportan paréntesis para dividir términos.

## Ejercicio 16

Escribir un programa que pida al usuario una cadena de caracteres (una palabra o una frase) y muestre por pantalla la longitud de la cadena.

```
Ingrese frase o cadena de caracteres: Realizando la práctica de programación

La longitud es de 38 caracteres.
```

Pista: la instrucción `len()` nos provee la siguiente información:

```py
> len("Hola")
4
```

## Ejercicio 17

Escribir un programa que pida al usuario una lista de palabras e imprima por pantalla la palabra más larga y la palabra más corta.

El ingreso de palabras termina cuando se ingresa la palabra `fin`.


## Ejercicio 18

Escribir un programa que calcule el área de un triángulo dados su base y altura.

## Ejercicio 19
Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla cuántas vocales hay en la cadena.

Pista:
La instrucción count() nos provee la siguiente información:
```py
> "Hola".count('a')
1
```

## Ejercicio 20

Escriba un programa que calcule si un alumno o alumna puede promocionar una materia.
Una materia consta de 3 exámenes y el promedio para promocionar debe ser >= 8 pero si en algún examen hay una nota < 6 la o el alumno no podrá promocionar por mas que el promedio sea >= 8.
Las notas son de 1 a 10.

Ejemplo que no promociona:
```
Ingrese la nota en el primer examen: 6
Ingrese la nota en el segundo examen: 8
Ingrese la nota en el tercer examen: 8
Resultado:NO se promocionó la materia :(

# Da como promedio < 8

```

Ejemplo que tampoco promociona:
```
Ingrese la nota en el primer examen: 10
Ingrese la nota en el segundo examen: 10
Ingrese la nota en el tercer examen: 5
Resultado: NO se promocionó la materia :(

# Da como promedio > 8 pero tuvo una nota < 6

```

Ejemplo que sí promociona:
```
Ingrese la nota en el primer exámen: 8
Ingrese la nota en el segundo exámen: 10
Ingrese la nota en el tercer exámen: 8
Resultado: ¡Se promocionó la materia! :D

# Da como promedio >= 8

```


## Ejercicio 21

Escribir un programa que simule ser un cajero automático donde se extrae dinero de la cuenta. El programa debe consultar al usuario la cantidad que desea extraer. Si el dinero que desea extraer es menor al saldo total, la extracción será exitosa y deberá informar el monto extraído y el saldo restante.

Si se solicita un monto que excede el monto, el programa deberá decir saldo insuficiente. Supongamos que se tiene en cuenta 1000.

```
Ingrese el monto a extraer:
200

Ha extraído:
200

Le queda en cuenta 800
```

En caso que quiera extraerse mas que el saldo disponible:

```
Ingrese el monto a extraer:
1200

No hay suficiente saldo para completar la operación
```

El monto en la cuenta está previamente cargado (no se ingresa por teclado).

### Ejercicios resueltos en clase

En [este link](https://github.com/kity-linuxero/practicas_23/tree/main/practicas/ej_resueltos/pr3) podemos ver los ejercicios hechos en clase.

-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 90%">
