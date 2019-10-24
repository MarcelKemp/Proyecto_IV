# Integración continua

## Travis CI:

  Se trata de un sistema de integración continua que se integra sin problemas en GitHub, comprobando y testeando aplicaciones de distintos lenguajes de programación (Ruby, Java, C#, Python...) con cada push o pull request.


  Para hacer uso de esta herramienta, he seguido el tutorial de la página oficial: [Travis-CI](https://docs.travis-ci.com/user/tutorial/)

  El archivo *.travis.yml.* que he creado, contiene el siguiente código:

```
language: python
python:
  - "2.7"
install:
  - pip install -r requirements.txt
script:
  - pytest
  - python src/Crupier.py
```

  En las primeras líneas, le indicamos el lenguaje de programación usado, que en este caso es python, junto con la versión que va a utilizar para realizar las pruebas (2.7). A continuación, se añade una línea que ejecute la instalación de los componentes necesarios para la ejecución del servicio, que al ser python, hacemos que instale los requirements. Y por último, le indicamos los scripts que queremos que se ejecuten, que en este caso, son los tests junto con el servicio.
