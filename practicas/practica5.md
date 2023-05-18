
# Práctica 5 - Diccionarios

## Parte I

## Ejercicio 1

Escribir un programa que guarde en una variable el siguiente diccionario `{'Dolar':'US$', 'Euro':'€', 'Yuan':'¥', 'Peso':'AR$'}` y pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. En tal caso se termina el programa.

```bash
Ingrese una divisa para saber el símbolo: Euro
El símbolo es: €
Ingrese una divisa para saber el símbolo: hola
La divisa no existe.
Fin del programa
```

## Ejercicio 2

Realice otro diccionario como anterior pero que contenga el valor de la divisa respecto al peso argentino. Y luego pida al usuario que ingrese un monto en pesos argentinos para calcular el equivalente a una divisa deseada en ambos sentidos.

```bash
Ingrese monto en pesos: 800
Ingrese la divisa para convertir: Euro

800 pesos argentinos es equivalente a: 6,30 €
1€ es igual a 127.07 pesos argentinos

```

Actualice el valor de la divisa respecto al peso argentino. Los símbolos de la divisa no es obligatorio.



## Ejercicio 3
Se tiene el siguiente diccionario anidado:
```python
diccionario = {
    "clase": {
        "estudiante": {
            "nombre": "Marcos",
            "materias": {
                "matematica": 7,
                "geografia": 8
            }
        }
    }
}
```

Desarrolle un programa para que imprima la nota de geografía.

## Ejercicio 4

Desarrolle una programa que dado el diccionario anterior, actualice las notas de matemática y geografía para que sean 8 y 7 respectivamente.

## Ejercicio 5

Desarrolle una programa que dado el diccionario anterior actualice la clave `geografia` por `historia` e imprima el diccionario final.

## Ejercicio 6

Se tienen a los siguientes alumnos `('Ana', 'Alejo', 'Valentina', 'Fausto', 'Clara', 'Manuel')`.

Cree un programa que, pida por cada alumno la nota obtenida en un examen y la guarde en un diccionario donde la clave será el nombre del alumno.

## Ejercicio 7

Dado el siguiente diccionario, convierta sus claves en una lista llamada `claves` y sus valores en otra lista llamada `valores`.

```
{
    'camion' : '23.4',
    'auto' : '7.2',
    'moto' : '3.4',
    'camioneta' : '13.8',
    'colectivo' : '21.9'
}
```

## Ejercicio 8

Desarrolle un programa que, dado el siguiente diccionario, devuelva el día con menor temperatura.

```python

temp = {
    'domingo': 23.3,
    'lunes': 22.6,
    'martes': 18.9,
    'miércoles': 17.2,
    'jueves': 19.4,
    'viernes': 20.0,
    'sabado': 24.1
}

```

[Pista](https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/)

## Ejercicio 9

Contar letras: Crea un programa que reciba por el usuario una palabra y devuelva un diccionario con cada letra como clave y el número de veces que aparece como valor.

Por ejemplo:
```bash
Escriba una palabra: palabra

{'p': 1, 'a': 3, 'l': 1, 'b': 1, 'r': 1}

```


## Ejercicio 10

Se tiene el siguiente diccionario:
`{'Mayonesa':'140,50', 'Cerveza': 130, 'Agua mineral': 110.15, Servilleta: 65.20}`.
Escriba un programa que permita simular una compra donde se van ingresando productos y cantidad. Los valores se van sumando para tener el total para cobrar al finalizar la compra.
La compra termina cuando el usuario ingresa `fin` donde se deberá finalizar la compra e informar el monto total.
También debe ser posible saber el parcial de una compra cuando se ingresa `parcial` donde deberá informar el monto gastado hasta el momento pero sin finalizar la compra:
A continuación se muestra un ejemplo de ejecucición del programa:

```bash
Ingrese producto: Mayonesa
Ingrese cantidad: 3
El precio es: $421.50
----------------------
Ingrese producto: Cerveza
Ingrese cantidad: 2
El precio es: $260
----------------------
Ingrese producto: parcial
Parcial compra: $681.50
----------------------
Ingrese producto: computadora
El producto no existe
----------------------
Ingrese producto: Servilleta
Ingrese cantidad: 1
El precio es: $65.20
----------------------
Ingrese producto: fin
----------------------
El total de su compra es: $ 746.70
```
