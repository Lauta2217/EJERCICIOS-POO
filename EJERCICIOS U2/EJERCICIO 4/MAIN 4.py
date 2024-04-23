import os
import numpy as np 
from motos import *
from pedidos import *
if __name__ == '__main__':
  op = int(input("Ingrese opcion:\n 1_Cargar Motos\n 2_Cargar pedidos\n 3_Agregar pedido\n 4_Agregar tiempo real a pedido\n 5_Tiempo real por conductor\n 6_Calcular comisiones\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GM = gestorMoto()
      GM.cargar_motos_desde_csv()
    elif op == 2:
      GP = gestorPedido()
      GP.cargar_pedidos_desde_csv()
    elif op == 3:
      GP.asignar_pedido_a_moto(GM)
      GP.mostrar()
      GP.ordenar()
    elif op == 4:
      GP.Mod_Tiempo_Real()
      GP.mostrar()  
    elif op == 5:
      GM.tiempo_real_por_conductor(GP)
    elif op == 6:
      GM.calcular_comisiones(GP)
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Cargar Motos\n 2_Cargar pedidos\n 3_Agregar pedido\n 4_Agregar tiempo real a pedido\n 5_Tiempo real por conductor\n 6_Calcular comisiones\n 0_Para finalizar\n"))