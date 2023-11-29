# Trabajo práctico N°4

Con el TP4, se busca que se puedan volcar todos los conocimientos vistos en el curso y dar un cierre al mismo.


## Presentación de proyecto

Para la aprobación del TP4 se le solicita que piense en un proyecto que puede ser propio o un derivado de otro proyecto que encuentre por internet. Puede ser un programa propio con interface gráfica de usuario, por ejemplo desarrollado con Tkinter o QT, un juego en 2D desarrollado con pygame, arcade, etc. O bien puede ser algún proyecto software libre que le parezca interesante participar.

Si se opta por un proyecto propio, se requieren los siguientes puntos:

>Piense un proyecto simple y realizable en base al tiempo disponible y a las exigencias del TP.


- Presentar la idea al instructor
- Crear un repositorio Git (Github, GitLab) con acceso al instructor o público para su seguimiento.
    - Agregar el archivo [README.md](https://docs.github.com/es/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) con la descripción del programa y como hacerlo funcionar. Utilice la sintaxis [Markdown](https://markdown.es/sintaxis-markdown/) para organizar la documentación y el readme.
    - Agregue el archivo `.gitignore` para Python.

- Puede usar los siguientes branchs para tener una guía:
    - `main`: rama principal por defecto. Recuerde mantener "limpio" el branch y que lo que haya en el main sea código funcional.
    - `develop`: Rama de desarrollo. Es la que debe usar por lo general cuando está desarrollando el programa.
    - `feature/branch`: Parten y se fusionan con la rama `develop`. `feature` se refiere a una característica que tiene el programa. Por ejemplo si estamos desarrollando un juego y en algún momento quisiéramos desarrollar un escenario un branch puede ser `feature/escenario_selva`.
    > Tales branchs son siguiendo (parcialmente) la forma de trabajo de [Gitflow](https://www.google.com/search?channel=sn&q=giflow).

- Implementar el manejo de excepciones de manera de hacer robusto su programa.
- Debe estar bien definidos los módulos y separados según corresponda.
- No es obligatorio que el programa sea orientado a objetos, pero piense si el hacerlo orientado a objetos puede hacer su programa mas fácil de implementar y de entender.
- Realizar tests de unidad (deseable)
- De lo posible registrar en archivos datos del programa. Por ejemplo, si es un juego puede ser el puntaje máximo o algún dato que sea útil guardar. ¿De qué forma guardarlo?. Investigue la notación [json](https://www.json.org/json-es.html) y [yaml](https://es.wikipedia.org/wiki/YAML). En Python tenemos formas de manejar archivos [json](https://docs.python.org/es/3/library/json.html) como [yaml](https://python.land/data-processing/python-yaml).



Let's code!

-----

<img src="../practicas/img/foot_logos.png" alt="Descripción de la imagen" style="width:100%; filter: grayscale(100%); opacity: 40%">


