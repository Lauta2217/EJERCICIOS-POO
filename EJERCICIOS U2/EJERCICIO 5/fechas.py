import csv
from equipos import *
class Fechas():
  def __init__(self,fecha_partido, idd_de_Elocal, idd_de_Evisitante, cant_G_Elocal,cant_G_Evisitante):
    self.__fecha_partido = fecha_partido
    self.__idd_de_Elocal = idd_de_Elocal
    self.__idd_de_Evisitante = idd_de_Evisitante
    self.__cant_G_Elocal = cant_G_Elocal
    self.__cant_G_Evisitante = cant_G_Evisitante
  def __str__(self):
    return self.__fecha_partido

class gestorfechas():
  def __init__(self, lista = []):
    self.__lista = lista
  
  def cargar_fechas_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS/EJERCICIO 5/fechasFutbol.csv",newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        fechas = Fechas(*fila)
        self.__lista.append(fechas)
    print("Fechas cargadas correctamente\n")
  def mostrar(self):
    for fechas in self.__lista:
      print(fechas)      
  def buscar(self,idd):
    f = []
    for fechas in self.__lista:
      if idd == fechas._Fechas__idd_de_Elocal or idd == fechas._Fechas__idd_de_Evisitante:
        f.append(fechas._Fechas__fecha_partido)
    return f