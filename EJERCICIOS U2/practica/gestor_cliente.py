from clase_cliente import *
import csv

class gestor_cliente:
  __lista: list
  
  def __init__(self,lista = []):
    self.__lista = lista
    
  def cargar_cliente_desde_csv(self):
    with open("ClientesAbril2024.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter = ';')
      for fila in reader:
        cliente = Cliente(*fila)
        self.__lista.append(cliente)
      print("\nCLIENTES CARGADOS\n")
      
  def mostrar(self):
    for cliente in self.__lista:
      print(cliente)
      print("--------------------\n") 
      
  def actualizar_saldo(self,GM):
    DNI = input("Ingrese DNI\n")
    i = 0
    band = False
    while i < len(self.__lista) and not band:
     if self.__lista[i].getDNI() == DNI:
       band = True
     else:
       i+=1
       
    if band:
      print(f"""
            Cliente: {self.__lista[i].getNom()} {self.__lista[i].getApe()}        Numero de tarjeta: {self.__lista[i].getnum_T()}
            Saldo anterior: {self.__lista[i].getsaldo_A()}
            """)
      saldo_N = GM.mostrar_movi(self.__lista[i].getnum_T(),self.__lista[i].getsaldo_A())
      self.__lista[i].setsaldo(saldo_N)
      print(f"Saldo actualizado: {self.__lista[i].getsaldo_A()}\n")
    else:
      print("DNI INCORRECTO\n")  
  
  def movi_abril(self,GM):
    num_t = input("Ingrese numero de tarjeta\n")
    i = 0
    cont = 0
    band = False
    while i < len(self.__lista) and not band:
      if self.__lista[i].getnum_T() == num_t:
        band = True
      else:
        i+=1
        
    if band:
      if not GM.obtener_movi(num_t):
        print(f"El cliente: {self.__lista[i].getApe()} {self.__lista[i].getNom()} no tuvo movimientos en abril")
    else:
      print("Numero de tarjeta incorrecto\n")    