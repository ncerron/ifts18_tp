Estructura de Datos - Parcial

#Informe


Se desarrolla modulo de consulta de la aplicación web, módulo registración y módulo login. Al ingresar a la aplicacion se mostrará una página de bienvenida,  para ingresar al sistema habrá que loguearse, si no se encuentra registrado, tiene la opción de hacerlo a través de la barra de navegación.                                                                                                                  

El sistema posee distinto comportamiento de acuerdo al tipo de usuario:

*usuario común*, al loguearse, el sistema lo redireccionará a una página que le dará la bienvenida, solo tiene acceso a desloguearse.

*usuario admin*, al loguearse, el sistema lo redireccionará a una página que le dará la bienvenida y se visualizará las últimas ventas realizadas, éste usuario también tiene acceso a la página usuarios en la cual se visualizarán los usuarios registrados a través de una tabla,  y tiene acceso a las páginas correspondientes a las distintas consultas, las cuales se visualizarán también a través de tablas .                                                                                  


La información se encuentra en dos archivos csv,   las ventas estan dispuestas en una tabla que contiene 5 columnas y un número variable de filas, y los usuarios registrados contienen 2 columnas  y un número variable de filas.
Una vez iniciada la aplicación las páginas se irán generando a partir de las solicitudes que realiza el usuario desde el navegador. Por ejemplo  cuando el usuario  ingresa usuario y contraseña,  se realizará una consulta en el archivo passws.csv y si está registrado, será redirigido a la página de bienvenida.

La aplicación esta compuesta por los siguientes archivos: archivo.py, formulario.py, principal.py, carpeta template que contiene los distintos archivos .html,  una carpeta archivos_csv, con los archivos archivo.csv (contiene información de las ventas) y passws.csv (contiene la información de los usuarios registrados) y una carpeta static en la cual se encuentra el archivo estilo.css

*archivo.py* contine las distitas funciones que manipulan el archivo archivo.csv, las mismas serán utilizadas en principal.py.

*archivo formulario.py* se creará  las distintas clases de los formularios que se usarán en la aplicación.

*principal.py* es donde se incia la aplicación,  aquí se generan las distintas páginas html según las solicitudes que ingrese el usuario, y dependiendo de estas solicitudes, se realizarán validaciones o manejo de datos a través de las distintas consultas. 
