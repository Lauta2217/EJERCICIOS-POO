from clase_movimiento import *
import numpy as np
import csv
class gestor_movimiento:
  __lista: list
  
  def __init__(self):
    self.__lista = np.array([],dtype='object')
    
  def cargar_movimiento_desde_csv(self):
    with open("MovimientosAbril2024.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter=';')
      next(reader)
      for fila in reader:
        movi = Movimiento(*fila)
        self.__lista = np.append(self.__lista,movi)
      print("\nMOVIMIENTOS CARGADOS\n")
      
  def mostrar(self):
    for movi in self.__lista:
      print(movi)   
      print("------------------------------------\n") 
      
  def mostrar_movi(self,num_t,saldo):
    saldo_n = 0
    print("          Fecha Descripción             Importe                   Tipo de movimiento")
    for movi in self.__lista:
      if movi.getnum_T() == num_t:
        if movi.gettipo_M() == 'P':
          saldo_n-=movi.getimporte()
        elif movi.gettipo_M() == 'C':
          saldo_n+=movi.getimporte()
        print(f"""
              {movi.getfecha()}                  {movi.getimporte()}                         {movi.gettipo_M()}
              """)
    return float(saldo) + float(saldo_n)
  
  def obtener_movi(self,num_t):
    i = 0
    band = False
    while i < len(self.__lista) and not band:
      if self.__lista[i].getnum_T() == num_t:
        band = True
      else:
        i+=1
    return band
  
  def ordenar(self):
    self.__lista = np.sort(self.__lista)
    print("MOVIMIENTOS ORDENADOS:\n")
