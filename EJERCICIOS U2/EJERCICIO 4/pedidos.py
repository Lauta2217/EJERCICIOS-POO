import csv
import os
class Pedido():
  def __init__(self,patente,identificador,comida,tiempo_Estimado,tiempo_Real,precio):
    self.__patente = patente
    self.__identificador = identificador
    self.__comida = comida
    self.__tiempo_Estimado = tiempo_Estimado
    self.__tiempo_Real = tiempo_Real
    self.__precio = precio
  def __str__(self):
    return f"Patente: {self.__patente}\nID: {self.__identificador}\nComida: {self.__comida}\nTiempo Estimado: {self.__tiempo_Estimado}\nTiempo Real: {self.__tiempo_Real}\nPrecio: {self.__precio}\n"
  def __lt__(self, other):
        return self.__patente > other._Pedido__patente
  def __lt__(self, other):
        return self.__patente < other._Pedido__patente
class gestorPedido():
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_pedidos_desde_csv(self):
    os.system("cls")
    with open("UNIDAD 2/EJERCICIOS/EJERCICIO 4/datosPedidos.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        pedido = Pedido(*fila)
        self.__lista.append(pedido)
    print("pedidos cargados correctamente")
  def mostrar(self):
    os.system("cls")
    for pedido in self.__lista:
      print("\t-------------------------------------------------------\n")
      print(pedido)
  
  def asignar_pedido_a_moto(self,GM):
    os.system("cls")
    patente = GM.verificarpatente()
    identificador = input("Ingrese identificador\n")
    comida = input("Ingrese comida\n")
    tiempo_Estimado = input("Ingrese tiempo estimado\n")
    tiempo_Real = 0
    precio = input("Ingrese precio\n")
    
    pedido = Pedido(patente.upper(),identificador,comida,tiempo_Estimado,tiempo_Real,precio)
    
    self.__lista.append(pedido)
    
  def Mod_Tiempo_Real(self):
    os.system("cls")
    iden = input("Ingrese id del pedido\n").strip().lower()
    patente = input("Ingrese patente del pedido\n").strip().lower()
    for pedido in self.__lista:
      if(pedido._Pedido__identificador == iden) and (pedido._Pedido__patente == patente):
        pedido._Pedido__tiempo_Real = input("Ingrese tiempo real de entrega\n")
        break
  def calcular_pedido(self,patente):
    i = 0
    suma = 0
    for pedido in self.__lista:
      print(f"{pedido._Pedido__patente}")
      if pedido._Pedido__patente.strip().lower() == patente.strip().lower():
        i += 1
        suma += int(pedido._Pedido__tiempo_Real)
    return suma/i
      
  def Comisiones(self,patente):
      os.system("cls")
      suma = 0
      print("Identificador de pedido          Tiempo estimado           Tiempo real           Precio")
      for pedido in self.__lista:
          if pedido._Pedido__patente == patente:
            print(f"{pedido._Pedido__identificador:<35} {pedido._Pedido__tiempo_Estimado:<27} {pedido._Pedido__tiempo_Real:<17} {pedido._Pedido__precio:<20}" ) 
            suma += float(pedido._Pedido__precio)
      print(f"total: {suma}\n")
      print(f"Comision: {suma * 0.20}\n")
  def ordenar(self):
      os.system("cls")
      self.__lista = sorted(self.__lista)
      print("Lista de pedidos ordenados:")
      for pedido in self.__lista:
        print(pedido)