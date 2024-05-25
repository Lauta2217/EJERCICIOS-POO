from clase_lista import Lista
from parajson import jsoon
if __name__ == '__main__':
	lista = Lista()
	jsooon = jsoon()
	lista.agregar_calefactor(jsooon.cargar_calefactores())
	op = int(input("""Ingrese opcion: 
					1_Insertar en posicion determinada 
					2_Cargar a mano
					3_Mostrar calefactor de determinada posicion
					4_Mostrar datos calefactor mas barato
					5_Buscar y mostrar por marca
					6_Mostrar calefactores en promocion
					7_Almacenar en otro json
					0_Para finalizar
					"""))
	while op!=0:
		if op == 1:
			i = 1
			for cale in lista:
					print(f"{cale} posicion:{i}")
					print("------------------\n")
					i+=1
			lista.insertar_pos(pos = int(input("Ingrese posicion para agregar\n")))
			i = 1
			print("CARGADOOOOOS")
			for cale in lista:
					print(f"{cale} posicion:{i}")
					print("------------------\n")
					i+=1
		elif op == 2:
			tipo = str(input("Ingrese tipo de calefactor: electrico o gas\n"))
			lista.cargar_cale(tipo,lista)
			i = 1
			for cale in lista:
					print(f"{cale} posicion:{i}")
					print("------------------\n")
					i+=1
		elif op == 3:
			lista.informar_pos(pos = int(input("Ingrese posicion para consultar\n")))
		elif op == 4:
			lista.cale_gas_min(lista)
		elif op == 5:
			marca = str(input("Ingrese marca a buscar\n"))
			lista.buscar_marca(marca,lista)
		elif op == 6:
			lista.buscar_promo(lista)
		elif op == 7:
			jsooon.guardar_calefactores(lista)
		else: print("Numero ingresado no corresponde")
		op = int(input("""Ingrese opcion: 
					1_Insertar en posicion determinada 
					2_Cargar a mano
					3_Mostrar calefactor de determinada posicion
					4_Mostrar datos calefactor mas barato
					5_Buscar y mostrar por marca
					6_Mostrar calefactores en promocion
					7_Almacenar en otro json
					0_Para finalizar
					"""))
"""
1
2
2
electrico
caca
caca pro
caca mundo
100000
contado
si
1000
3
1
4
5
samsung
6
7
"""