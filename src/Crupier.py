#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Crupier():

	def __init__(self,jugadores=2):
		self.jugadores=jugadores
		self.baraja=self.generar_baraja()
		self.num_cartas=len(self.baraja)


	def generar_baraja(self):
	   palos = ['C','D','T','P'] # C=Corazón, D=Diamante, T=Trébol, P=Pica

	   valores = ['A'] + [v for v in range(2,11)] + ['J','Q','K'] #A-2-...-10-J-Q-K

	   return [(rank,suit) for suit in palos for rank in valores] #devuelve cartas ordenadas por palo (valor,palo)

	def mezclar_baraja(self):
		baraja=self.baraja
		while len(baraja) > 0:
			carta = random.choice(baraja)
			baraja.remove(carta)
			yield carta
		
	def repartir_cartas(self):
		jugador=[]
		num=0	
		mano=[]
		mano_jugador=[]
		baraja=self.mezclar_baraja()	
		while num < self.jugadores:
			jugador=[num]
			mano=[next(baraja)]+[next(baraja)]
			self.num_cartas=self.num_cartas-len(mano)
			num=num+1
			mano_jugador=mano_jugador+jugador+mano
		"""for i in jugador*ncartas:
			jugador=jugador+[next(baraja)]"""
		return mano_jugador #Guarda id jugador + dos cartas, luego el id se encuentra cada 3 posiciones (posicion:0,3,6,...)
	

	def mostrar_baraja(self,baraja):
		carta=next(baraja)
		if (not type(carta) == tuple):
			raise TypeError( "La baraja tiene que estar compuesta por tuplas (cartas)" )

		return [carta]+[cartas for cartas in baraja]

	def mostrar_mano(self, mano, jugador):
		if (not 0<=jugador<self.jugadores):
			raise IndexError( "El número de jugadores es incorrecto" )
		print("Cartas Jugador "+str(jugador)+": "+str(mano[jugador*3+1])+"-"+str(mano[jugador*3+2]))
		return 0

	def mostrar_manos(self):
		mano_jugador=self.repartir_cartas()
		player=0
		while player < self.jugadores:		
			self.mostrar_mano(mano_jugador,player)
			player=player+1
		return 0

	def cantidad_cartas(self):
		if 0<=self.num_cartas<=52:
			return True
		else: 
			return False

	def cantidad_jugadores(self):
		return self.jugadores


if __name__=='__main__':

	num_jugadores=5
	baraja=Crupier(num_jugadores)
	manos_jugadores=baraja.mostrar_manos()
	print (manos_jugadores)
	baraja_restante=baraja.mezclar_baraja()
	print (baraja.mostrar_baraja(baraja_restante))



