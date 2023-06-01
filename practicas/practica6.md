
# Práctica 6 - Modularidad

## Ejercicio 1

Escriba una función que reciba un nombre de una persona (ingresada por el usuario por teclado) y lo salude desde el módulo (no debe retornar nada). Por ejemplo, si le mandamos "Manuel" el módulo debe imprimir en pantalla: ¡Hola Manuel!. Junto con la función, escribir el programa que invoque a la función.

## Ejercicio 2

Escriba una función que retorne el cuadrado de un número enviado por parámetro. (Se debe multiplicar por si mismo ;)

## Ejercicio 3

Escriba una función que reciba dos números y retorne el mayor de esos dos. Devolverlos con return e imprimirlo desde el programa

## Ejercicio 4

Escriba una función de nombre `esCero(unNumero)` que retorne si un número es igual a 0 o no y úselo en el siguiente programa.

```python
if esCero(unNumero):
    print("Es cero")
else:
    print("No es cero")
```

## Ejercicio 5

Escriba un programa que convierta una temperatura ingresada por el usuario en grados Celsius a grados Fahrenheit y viceversa. Crear dos funciones: una llamada celsius_a_fahrenheit() que tome una temperatura en grados Celsius y devuelva su equivalente en grados Fahrenheit, y otra llamada fahrenheit_a_celsius() que haga lo contrario.

Celsius a Fahrenheit: (x°C * 9/5) + 32 = y°F

Fahrenheit a Celsius: (x°F -32) * 5/9 = y°C

```bash
¡Bienvenido al conversor de temperaturas!
Ingresa una temperatura: 64
64.0 grados Celsius equivalen a 147.2 grados Fahrenheit.
64.0 grados Fahrenheit equivalen a 17.77 grados Celsius.
```

## Ejercicio 6

Crear un programa calculadora. Le debe pedir al usuario dos números y una operación (puede ser suma, resta, multiplicación o división). Posteriormente debe imprimir el resultado.

Escribir una función para cada operación.

```bash
Escriba el op1: 9
Escriba el op2: 2
Elija una operación (+ - * /): +

El resultado es 9+2=11
```

En caso de la división, verificar que op2 NO sea 0. Dado que no puede realizarse una división por 0. En tal caso debe imprimir "No se puede dividir por 0".

```bash
Escriba el op1: 9
Escriba el op2: 0
Elija una operación (+ - * /): /

No se puede dividir por 0

```

## Ejercicio 7

Reescribir el programa hecho en la práctica 4 del juego de piedra, papel y tijera que se puede jugar varias veces utilizando la nueva técnica para separar en módulos.

Una sugerencia de módulos podría ser:

- `realizar_jugada()`: La computadora elige una opción.
- `tomar_jugada()`: Realiza la operación de tomar una jugada al usuario descartando los valores inválidos.
- `gano(user, pc)`: Retorna si la jugada del usuario enviada mediante el parámetro `user` le ganó la jugada de la pc enviada mediante el parámetro `pc`. El valor debe ser `True` o `False`
- `informar_victoria(user, pc)`: Imprime el texto correspondiente cuando un usuario gana.
- `informar_derrota(user, pc)`: Imprime el texto correspondiente cuando un usuario pierde.
- `informar_empate(user,pc)`: Imprime el texto correspondiente cuando hay empate.
- `informar_fin_juego()`: Imprime el texto con las estadísticas de las partidas.

## Ejercicio 8

Modifique el programa de piedra, papel y tijera del ejercicio anterior para que permita a la computadora hacer trampa dándole la oportunidad de tirar otra vez en caso que el usuario haya ganado en el primer intento. El usuario no debe enterarse ;) y la PC podrá elegir solo una vez mas (sino sería muy obvio XD).

## Ejercicio 9

Escriba un programa que permita elegir las parejas para el juego del "amigo invisible".

Se debe tomar los nombres de las personas que van a jugar. La entrada de datos puede terminar cuando se ingrese `fin` o `.` lo que usted considere.

Una vez que se tienen todos los participantes, se debe elegir para cada participante otro participante que será su amigo invisible. Al finalizar la toma de datos, se debe realizar el sorteo e informar por pantalla.

```bash
Ingrese nombre de participante: Carlos
Ingrese nombre de participante: Lucia
Ingrese nombre de participante: Juanjo
Ingrese nombre de participante: Nadia
Ingrese nombre de participante: Pablo
Ingrese nombre de participante: German
Ingrese nombre de participante: .

Se ha finalizado la toma de participantes. Hay en total 6 participantes.
El sorteo ha dado lo siguiente:

Carlos -> Juanjo
Lucia -> German
Juanjo -> Pablo
Nadia -> Carlos
Pablo -> Lucia
German -> Nadia

```

Utilice las estructuras de datos vistas hasta el momento que le pueda ayudar. Separe en módulos para que el programa sea mas legible.

Una sugerencia de módulos puede ser:
- `tomar_participantes()`: Toma los participantes. Devuelve una lista con los participantes.
- `sortear(lista_participantes)`: Realiza el sorteo.

# Ejercicio 10

Escriba un programa que reciba la apuesta de n jugadores. A los jugadores se les pregunta el nombre y el número al cual apuestan. Las apuestas son números entre 0 y 99 y puede ser que varios jugadores apuesten al mismo número. Una vez que todos los jugadores hayan realizado su apuesta, el programa sortea un número entre 0 y 99. Puede ser que no haya ganadores, o haya mas de uno. Debe informar si hay ganadores o no y debe decir el nombre de los ganadores.

```bash
Ingrese nombre de la/el apostador: Martín
Ingrese su apuesta: 89

Ingrese nombre de la/el apostador: Agustin
Ingrese su apuesta: 19

Ingrese nombre de la/el apostador: Rebeca
Ingrese su apuesta: 76

Ingrese nombre de la/el apostador: Patricio
Ingrese su apuesta: 0

Ingrese nombre de la/el apostador: Fernanda
Ingrese su apuesta: 99

Ingrese nombre de la/el apostador: . # Termina de tomar apuestas

Salió sorteado el número 86. No hay ganadores

```

Trate de pensar la resolución "en módulos" es decir, en partes mas pequeñas para luego ir integrando esas partes mas pequeñas para resolver todo el programa. Por ejemplo, una parte es la de toma de apostadores con su apuesta, otra puede ser en qué estructura se guarda, otro realizar el sorteo y otra parte es la búsqueda de ganadores.

## Ejercicio 11

### Ejercicio para super sayayins de la programación XD


>Este ejercicio tiene una dificultad alta. Necesitará pensar cada parte del programa. Modularice cada parte del programa de manera que pueda reutilizar el código que se utilizará en cada turno. ¡Éxitos!

Escriba un programa que permita jugar _una especie_ de __"7 y medio"__ que se juega con mazos de cartas españolas. Las cartas españolas tiene cuatro palos: espada, basto, copa y oro y cada palo tiene cartas numeradas del 1-12. A efectos del ejercicio eliminaremos las cartas 8 y 9 de cada palo, quedando 10 cartas por palo y en total 40 cartas.

Al principio del programa, se le preguntará la cantidad de jugadores que deseen jugar. Siendo el mínimo 2 jugadores (la pc no jugará).

Para este juego, no importa el palo de la carta, pero sí el valor numérico. Las cartas del 1 al 7 valen del 1 al 7 respectivamente. Los 10,11 y 12 valen 1/2.

El juego consiste en que el jugador pide cartas a la computadora y luego de pedir una carta elegir si se "planta" o quiere otra carta mas. Gana el jugador que llegue mas cerca de sacar 7 y 1/2. Pero pierde automáticamente cuando se pasa.

A tener en cuenta. Al principio de la partida debe _barajarse_ las cartas quedando mezcladas. A medida que un jugador pida una carta, la carta es quitada del mazo.

Ejemplo de juego:

```bash
¡Bienvenidx al juego de cartas 7 y medio del curso de programación del CFP!

Elija la cantidad de jugadores (mínimo 2): 3

Turno jugador 1-
Su carta en este turno es: 5
En total lleva 5 puntos.
¿Desea sacar otra carta? (S/n): s
Su carta en este turno es: 10
En total lleva 5,5 puntos.
¿Desea sacar otra carta? (S/n): s
Su carta en este turno es: 1
En total lleva 6,5 puntos.
¿Desea sacar otra carta? (S/n): n
El jugador 1 terminó su partida con 6,5.
--------------
Turno jugador 2
Su carta es: 2
En total lleva 2 puntos.
¿Desea sacar otra carta? (S/n): s
Salió una carta 7.
¡Perdiste!
El jugador 2 terminó su partida con 9.
--------------
Turno jugador 3
Su carta es: 7
En total lleva 7 puntos.
¿Desea sacar otra carta? (S/n): n
El jugador 3 terminó su partida con 7.
--------------
¡Ganó jugador 3!
```

Sugerencias (Son opcionales pero le puede ayudar a resolver el ejercicio)
- Escriba un módulo que, dada una carta le devuelva el valor de la misma.
- Escriba un módulo que le permita saber si un jugador se pasó del puntaje o no. Lo que indicaría si perdió o no.
- Escriba un módulo para crear el mazo.
- Escriba un módulo para barajar las cartas (mezclarlas)
- El mazo de cartas puede ser una lista. Como no importa el palo podrá resolverlo con una lista de 40 elementos numéricos. Debe haber 4 elementos de cada número 1,2,3,4,5,6,7,10,11 y 12.
- Vaya probando cada módulo a medida que los vaya escribiendo. Por ejemplo. Cuando haga el módulo para crear el mazo, imprima con `print()`el mazo creado para verificar que funciona. Una vez creado el mazo pruebe con `print()`si al mezclarlo, el mismo se hace correctamente.