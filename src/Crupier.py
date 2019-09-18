#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json

class Crupier():

	def __init__(self,jugadores=2):
		self.jugadores=jugadores
		self.baraja=self.generar_baraja()
		self.num_cartas=len(self.baraja)
		self.cartas_descartadas=[]
		self.mano=self.repartir_cartas_jugadores()


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

	def repartir_cartas_jugadores(self):
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

	def repartir_cartas_mesa(self):
		num=0
		mesa=[]
		mano_jugador=[]
		baraja=self.mezclar_baraja()
		while num < 5:
			if(num<3):
				self.cartas_descartadas=self.cartas_descartadas+[next(baraja)]
				mesa=mesa+[next(baraja)]+[next(baraja)]+[next(baraja)]
				num=num+3
			elif(num<5):
				self.cartas_descartadas=self.cartas_descartadas+[next(baraja)]
				mesa=mesa+[next(baraja)]
				num=num+1

			self.num_cartas=self.num_cartas-len(mesa)

		return mesa

	def mano_player(self, mano, jugador):
		if (not 0<=jugador<self.jugadores):
			raise IndexError( "El número de jugadores es incorrecto" )
		#print("Cartas Jugador "+str(jugador)+": "+str(mano[jugador*3+1])+"-"+str(mano[jugador*3+2]))
		return [jugador,mano[jugador*3+1],mano[jugador*3+2]]

	def mostrar_baraja(self,baraja):
		carta=next(baraja)
		if (not type(carta) == tuple):
			raise TypeError( "La baraja tiene que estar compuesta por tuplas (cartas)" )

		return [carta]+[cartas for cartas in baraja]

	def mostrar_cartas_descartadas(self):
		return [cartas for cartas in self.cartas_descartadas]

	def mostrar_mano(self, mano, jugador):
		if (not 0<=jugador<self.jugadores):
			raise IndexError( "El número de jugadores es incorrecto" )
		print("Cartas Jugador "+str(jugador)+": "+str(mano[jugador*3+1])+"-"+str(mano[jugador*3+2]))
		return 0

	def mostrar_manos(self):
		player=0
		manos=[]
		while player < self.jugadores:
			self.mostrar_mano(self.mano,player)
			player=player+1
		return 0

	def mostrar_mesa(self):
		mesa=self.repartir_cartas_mesa()
		if (0>=len(mesa)>5):
			raise IndexError( "La mesa no contiene ninguna carta repartida" )
		#print("Cartas comunes (mesa): "+str(mesa[0])+"-"+str(mesa[1])+"-"+str(mesa[2])+"-"+str(mesa[3])+"-"+str(mesa[4]))
		return mesa

	def cantidad_cartas(self):
		if 0<=self.num_cartas<=52:
			return True
		else:
			return False

	def cantidad_jugadores(self):
		return self.jugadores

	def get_JSON(self):
		with open('data.json', 'r') as read_file:
			data = json.load(read_file)
		return data


if __name__=='__main__':
	jugador=0
	num_jugadores=5
	baraja=Crupier(num_jugadores)
	manos_jugadores=baraja.mano
	mesa=baraja.mostrar_mesa()
	cartas_descartadas=baraja.mostrar_cartas_descartadas()
	baraja_restante=baraja.mostrar_baraja(baraja.mezclar_baraja())

	baraja.mostrar_manos()
	print("Cartas comunes (mesa): "+str(mesa[0])+"-"+str(mesa[1])+"-"+str(mesa[2])+"-"+str(mesa[3])+"-"+str(mesa[4]))
	print("\nLo siguiente es una prueba para ver que funcionan correctamente las funciones:")
	print("\n\t - Las cartas que se han descartado al barajar son:\n\n"+"\t"+str(cartas_descartadas))
	print ("\n\t - Las cartas restantes de la baraja son:\n\n"+"\t"+str(baraja_restante))

	data = {
		"Cartas": {
			"jugadores": manos_jugadores,
			"jugador_"+str(baraja.mano[0]): [baraja.mano[1]]+[baraja.mano[2]],
			"mesa": mesa,
			"descartes":cartas_descartadas,
			"baraja":baraja_restante
		}
	}

	#json_str = json.dumps(data)
	#print('Datos en formato JSON:', json_str)

#Datos juego actual
with open('data.json', 'w') as write_file:
	json.dump(data, write_file)

test=baraja.get_JSON()
partida=test['Cartas']
manos=partida['jugadores']
mesa=partida['mesa']
baraja=partida['baraja']
descartes=partida['descartes']

print (partida['jugador_0'])



# Este segundo json, corresponderá al historial de cada jugada
# with open('history.json', 'a') as history_file:
# 	history={'PartidaX': data}
# 	json.dump(history, history_file)
