# Práctica 8
> Esta es una práctica de repaso e integración. Por lo que no solamente se le da libertad para usar todo lo que hemos aprendido hasta el momento y también complementarlo con búsquedas en internet.


## Ejercicio 1
### Generador de contraseñas

Por nuestra seguridad es muy recomendable utilizar contraseñas fuertes para segurizar nuestras aplicaciones, datos personales y redes sociales. Hoy en día, hasta los navegadores web sugieren contraseñas fuertes y seguras en el momento de registrarnos en alguna plataforma web y el mismo navegador se encarga de guardarla después.
En este ejercicio vamos a desarrollar un generador de contraseñas para ofrecerle al usuario que use nuestro programa contraseñas seguras.

Las contraseñas se componen por caracteres aleatorios que incluyen: caracteres minúsculas, mayúsculas, caracteres especiales y números.

También es necesario preguntarle al usuario la longitud de contraseña que quiere utilizar como también la cantidad de contraseñas a mostrar en pantalla (elija un máximo para no estar generando aleatoriamente infinitas contraseñas).

A continuación se muestra un ejemplo de ejecución:

```
Bienvenido al generador de contraseñas desarrollado por <Su nombre aquí ;)>

Elija la cantidad de caracteres para su contraseña: 10
Elija la cantidad de contraseñas a generar: 5

Contraseñas generadas con los criterios especificados:

!jFtdQ7yhG
7f4Y[!',8X
ST%o6]gxpX
8Gk7XPk05^
daonM,u6zJ
```
Realice un programa que permita generar contraseñas como las listadas arriba. Tenga en cuenta que el programa debe generar contraseñas con caracteres minúsculas, mayúsculas, caracteres especiales y dígitos numéricos.

>Pista: Google lo sabe todo, menos la combinación de la caja fuerte.

## Ejercicio 2
### Diccionario de contraseñas

> __Importante:__ cuando hablamos de diccionarios en este ejercicio no nos referimos a las estructuras de datos diccionarios vistas en el curso. Sino, simplemente a una lista de palabras o números.

Un reconocido ISP (proveedor de internet) de Argentina, durante mucho tiempo tuvo como contraseña de WiFi para sus routers, de forma predeterminada un patrón de números seguido del DNI del titular.
Una técnica muy conocida para atacar redes WPA/WPA2 (a día de hoy es el estándar para proteger redes mas utilizado para redes WiFi) es obtener la PSK (la clave) cifrada, que, mediante un __diccionario de datos__  y un algoritmo se pueden ir probando una a una hasta llegar a la clave WiFi en texto plano.

En este ejercicio trataremos de generar el _diccionario de datos_ con los patrones seguidos de números de DNI.

Los patrones que se utilizaban eran: `004`, `011` o `044` seguido por un DNI. Por lo que, si arrancamos a generar nuestro diccionario de datos con el prefijo `004` desde el DNI 20.000.000 hasta el 30.000.000 el archivo de salida generado debe ser de la siguiente forma:

```
00420000000
00420000001
00420000002
00420000003
.
.
.
00429999999
00430000000
```

Como puede ver, simplemente son números generados consecutivamente.

#### El programa a desarrollar
Desarrolle un programa que permita generar un _diccionario de datos_ que dé al usuario la opción de elegir el prefijo a usar y luego pregunte desde que número empezar a generar y hasta qué número. Si el usuario no especifica el número se debe empezar por el DNI 00.000.000. Se deberá guardar en un archivo `dic.txt`.

Se muestra a continuación un ejemplo de ejecución:

```bash
Bienvenido al generador de diccionario del curso.
Elija el prefijo del diccionario:
1- 004
2- 011
3- 044
Su opción: 1

Elija el número para empezar a generar: 
Elija el número donde termina de generar:
Escriba el nombre del archivo donde se volcará el resultado: dic.txt

Procesando... (esto puede llevar tiempo)

¡Diccionario generado correctamente!

Consulte el archivo dic.txt
```

En dicho caso no se especificó nada, por lo que empezará de la siguiente manera `dic.txt`:
```
00400000000
00400000001
00400000002
.
.
.
00499999998
00499999999
```
 
Observe que cada línea debe tener 11 caracteres (3 del prefijo y 8 del número de DNI) se deben completar con 0 si es necesario, en caso que el dni sea de 7 dígitos. Quedando de la forma: `00405123456`.

__Importante:__ Como se generan muchos datos, tenga en cuenta que el proceso puede consumir muchos recursos, en este caso RAM, almacenamiento. Para limitar los datos generados, pongamos como límite una generación máxima de 2 millones de registros para que no consuma muchos recursos.

> __Nota:__ Genere los valores directamente en el archivo. Si intenta grabarlos en una variable primero la PC puede llegar a colapsar por falta de RAM.

-----

<img src="img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 40%">
