# Dealer (Proyecto_IV)

[![Build Status](https://travis-ci.com/MarcelKemp/Proyecto_IV-Dealer.svg?branch=master)](https://travis-ci.com/MarcelKemp/Proyecto_IV-Dealer)

## Descripción del proyecto

Este proyecto consistirá en la realización de un micro-servicio encargado de repartir cartas, principalmente para poder integrarse en un servicio de Poker hold'em.

Estará basado en el número de usuarios (con limitación, por la capacidad en las mesas), la posición de los usuarios, el turno de reparto, el historial de manos, y si es posible, las estadísticas de victoria de cada mano.

---
## Herramientas
- **Python** será el lenguaje de programación usado.
- **Hug**, como el framework que usaremos.
- **MariaDB** será la base de datos utilizada.
- **LogStash** para la administración de logs.

---
## Descripción de la clase
Se ha creado una clase en */src/Crupier.py*, la cual crea una instancia con *n* jugadores (*n*=5, en este caso), donde muestra las dos cartas de cada jugador, y además una lista que contiene las cartas restantes en la baraja usada.  

---
## Instalando lo necesario
    pip install -r requirements.txt

## Para ejecutar clase
  	python3 src/Crupier.py

## Para ejecutar los tests
Para realizar los tests en nuestro proyecto, haremos uso del framework  **pytest**. Y para ejecutarlo usaremos el siguiente comando:

    pytest

Además el repositorio está configurado para que los tests pasen por **Travis CI** (servicio de integración continua). Comprobación: [![Build Status](https://travis-ci.com/MarcelKemp/Proyecto_IV-Dealer.svg?branch=master)](https://travis-ci.com/MarcelKemp/Proyecto_IV-Dealer)

---
#### Autor: Marcel Kemp Muñoz
