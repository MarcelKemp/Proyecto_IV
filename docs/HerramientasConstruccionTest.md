# Construcción y tests

## Herramientas de contrucción:

  He encontrado varias herramientas que se pueden usar para automatizar la construcción del proyecto, estas son: PyBuilder, Fabric, PyInvoke o Buildout. *El problema es que no se cuál es la más conveniente para el proyecto, por ello no hay ninguna implementada, y espero que pueda implementar alguna lo antes posible. (Comentario temporal)*

  Para la "construcción del proyecto", usamos el programa *pip* para ejecutar el archivo *requirements.txt*, que es el que contiene todo lo necesario para el funcionamiento del propio microservicio.

  Como en principio solo necesitamos ejecutar *pytest* para poder ejecutar el microservicio, es la única línea que contiene, ya que es lo único que necesita instalar.

## Tests:

  Para ejecutar los tests, hacemos uso de *pytest*, con el cual, comprobamos nuestro test *test_Crupier.py*.

  En este archivo, nos encontramos con varias funciones fundamentales para que nuestro microservicio funcione correctamente:

  ```
def test_comprobar_valores():
  ```

  Con esta función, dado un número de jugadores (5), y un crupier asignado a los jugadores, estamos comprobando el número de cartas en la baraja para que sea correcto [0-52], y el número de jugadores.

  ```
def test_mostrar_mano_OK_y_error():
  ```

  La siguiente función, dado un número de jugadores (5), y un crupier asignado a los jugadores, el crupier reparte las cartas, y nos muestra una mano. A partir de aquí, metemos datos incorrectos para hacer pruebas a nuestro test.

  ```
def test_mostrar_baraja_OK_y_error:
  ```

  Al igual que la función anterior, comprobamos que nuestro test funcione correctamente, introduciéndole datos erróneos, pero esta vez al mostrar la baraja completa.
