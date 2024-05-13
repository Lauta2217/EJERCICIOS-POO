import csv
from reparaciones import *

class Clientes:
  __dni:str
  __apellido:str
  __nombre:str
  __tel:str
  __patente:str
  __vehiculo:str
  __estado:str
  
  def __init__(self,dni,apellido,nombre,tel,patente,vehiculo,estado):
    self.__dni = dni
    self.__ape = apellido
    self.__nom = nombre
    self.__tel = tel
    self.__patente = patente
    self.__vehiculo = vehiculo
    self.__estado = estado
  
  def __str__(self):
    return f"{self.__dni}\n{self.__ape}\n{self.__nom}\n{self.__tel}\n{self.__patente}\n{self.__vehiculo}\n{self.__estado}\n"
  
  def getDNI(self):
    return self.__dni

  def getnom(self):
    return self.__nom
  
  def getape(self):
    return self.__ape
  
  def getpaten(self):
    return self.__patente
  
  def getvehiculo(self):
    return self.__vehiculo
  
  def gettelefono(self):
    return self.__tel
  
  def getestado(self):
    return self.__estado
  
  def setestado(self):
    self.__estado = 'T'
    return
  
  def __eq__(self,other):
    if ((self.__dni == other.__dni) and (self.__nom == other.__nom) and (self.__ape == other.__ape) and (self.__tel == other.__tel)):
      return self.__dni == other.__dni
    else:
      return self.__dni != other.__dni
    
class gestor_clientes:
  __lista = list
  
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/PRACTICO TEMA2/clientes.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv, delimiter=';')
      for fila in reader:
        clientes = Clientes(*fila)
        self.__lista.append(clientes)
      print("Clientes cargados\n")
  
  def mostrar(self):
    for cliente in self.__lista:
      print(cliente)
      
  def mostrarrepa(self,GR):
    DNI = input("Ingrese DNI\n")
    i = 0
    band = True
    while i < len(self.__lista) and band:
      if self.__lista[i].getDNI() == DNI:
        band = False
      else:
        i += 1
    if band == False:
      print(f"""
                DNI: {self.__lista[i].getDNI()}                                  Apellido y nombre: {self.__lista[i].getnom()}{self.__lista[i].getape()} 
                Patente: {self.__lista[i].getpaten()} 
                Vehículo: {self.__lista[i].getvehiculo()} 
              """)
      patente = self.__lista[i].getpaten()
      GR.mostrarRepa(patente)
      
  def cambiarestado(self,patente,total):
    band = True
    i = 0
    while i < len(self.__lista) and band:
      if self.__lista[i].getpaten() == patente:
        self.__lista[i].setestado()
        j = i
        band = False
      i +=1
      
    if not band:
      print(f"""
            Nombre: {self.__lista[j].getnom()}
            Apellido: {self.__lista[j].getape()}
            Telefono: {self.__lista[j].gettelefono()}
            Vehiculo: {self.__lista[j].getvehiculo()}
            Total a pagar: {total}
            """)
  def repanoterminadas(self,GR):
    for cliente in self.__lista:
      if cliente.getestado() == 'P':
        print(f"""
              Apellido y nombre: {cliente.getnom()}  {cliente.getape()}  
              Teléfono:{cliente.gettelefono()}
              Patente: {cliente.getpaten()} 
              Vehículo: {cliente.getvehiculo()} 
            \n""")
        patente = cliente.getpaten()
        GR.mostrarRepa(patente)
  
  def masdeunauto(self):
    apariciones = []
    for i, cliente in enumerate(self.__lista):
        # Si el cliente ya está en la lista, aumentamos su contador
        if cliente in self.__lista[:i]:
            apariciones[self.__lista.index(cliente)][1] += 1
        # Si no está en la lista, lo añadimos con un contador inicial de 1
        else:
            apariciones.append([cliente, 1])

    # Mostramos el resultado
    for cliente, cantidad in apariciones:
      print(f"""
            Nombre: {cliente.getnom()}
            Apellido: {cliente.getape()}
            Telefono: {cliente.gettelefono()}
            Patente: {cliente.getpaten()}
            Vehiculo: {cliente.getvehiculo()}
            \n""")