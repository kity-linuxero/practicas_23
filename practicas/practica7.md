# Práctica 7

Para esta práctica, para abrir archivos, utilice la instrucción `open` o `with open` pero agregando el `enconding utf8` para tener mayor compatibilidad con los caracteres. Por ejemplo:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
```


### Archivos

## Ejercicio 1
Escriba una función que permita leer el contenido entero de un archivo de texto y lo imprima en pantalla. Para esto cree un archivo llamado `datos.txt` desde el bloc de notas guardelo en la misma carpeta que el archivo .py de su programa.

## Ejercicio 2
Escriba un programa que lea las primeras `n` filas del archivo `datos.txt`. El número `n` debe ser enviado por el usuario.

## Ejercicio 3
Escriba una función que lea el archivo `mf1.dat` y cuente la cantidad de líneas que arrancan con la letra `M` e imprima la cantidad en pantalla.

Descargar archivo <a href="https://programacion.concristian.com.ar/img/clase7/mf1.dat" download>
mf1.dat
</a>

## Ejercicio 4
Escriba otra función que permita contar la cantidad de palabras que contiene el archivo del ejercicio anterior.

Pista: Ver uso de [split()](https://www.w3schools.com/python/ref_string_split.asp)

## Ejercicio 5
Escriba una función que permita contar la cantidad de veces que aparece una palabra enviada por el usuario. Por ejemplo:

```bash
Escriba la palabra que desea buscar: Yo
La palabra "Yo" aparece 9 veces
```

## Ejercicio 6
Escriba la función `palabras_cortas()` que lea el archivo `mf1.dat` e imprima las palabras que contienen menos de 4 caracteres.

## Ejercicio 7
Escriba una función que cuente la cantidad de letras mayúsculas que aparece en el archivo `mf1.dat`.

## Ejercicio 8
Escriba una función que permita buscar una palabra dentro del archivo `mf1.dat` y que pueda reemplazarse por otra palabra enviada por el usuario. Se debe guardar en un nuevo archivo llamado `mf1-a.dat`. Utilice las funciones hechas en otros ejercicios, como puede ser el ejercicio 5.

```bash
Escriba la palabra que desea buscar: Yo
La palabra "Yo" aparece 9 veces
Escriba la palabra que desee reemplazar por "Yo": Me
Fue reemplazada la palabra 'Yo' por 'Me' 9 veces.
El resultado se guardó en el archivo 'mf1-a.dat'
```

## Ejercicio 9
Escriba un programa que permita ir agregando contenido a un archivo interactivamente hasta que el usuario escriba `'fin'`.

```bash
Ingrese el texto hasta que llegue una línea con 'fin':

Los hermanos sean unidos porque ésa es la ley primera,
tengan unión verdadera,
en cualquier tiempo que sea,
porque si entre ellos se pelean los devoran los de afuera.
fin

Finalizó la toma de líneas.
```
Ver que el contenido del archivo coincida con lo que ha ingresado por teclado.

## Ejercicio 10
Escriba una función que modifique el contenido del archivo `mf1.dat` para que cada línea empiece con la letra en mayúscula.
Una vez terminado, ejecute nuevamente el ejercicio n y vea como cambia el resultado.

-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 40%">