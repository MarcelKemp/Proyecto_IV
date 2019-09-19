# -*- coding: utf-8 -*-
import pytest
from Crupier import Crupier

def test_comprobar_valores():
    jugadores=5
    crupier = Crupier(jugadores)
    assert crupier.cantidad_cartas() is True, "El número de cartas no está en el intervalo [0-52], por lo que es incorrecto"
    assert crupier.cantidad_jugadores() is jugadores, "El número de jugadores es incorrecto"

def test_mostrar_mano_OK_y_error():
    jugadores=5
    crupier = Crupier(jugadores)
    mano=crupier.repartir_cartas_jugadores() 
    assert crupier.mostrar_mano(mano,1)==0
    try:
        prueba = crupier.mostrar_mano(mano,-1)
    except Exception as fallo:
        assert type(fallo) is IndexError

    try:
        prueba = crupier.mostrar_mano(mano,5)
    except Exception as fallo:
        assert type(fallo) is IndexError

def test_mostrar_baraja_OK_y_error():
    jugadores=5
    crupier = Crupier(jugadores)
    baraja=crupier.mezclar_baraja()
    assert type(crupier.mostrar_baraja(baraja)) == list
    try:
	baraja=['A',58,47]
        prueba = crupier.mostrar_baraja(baraja)
    except Exception as fallo:
        assert type(fallo) is TypeError
