from clase_patinadores import *
from gestorEva import *
import csv
class gestor_patinadores:
  __lista: list
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_patinadores_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/PRACTICO TEMA1/federados.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        patinador = Patinador(*fila)
        self.__lista.append(patinador)
      print("PATINADORES BIEN CARGADOS\n")
      
  def mostrar(self):
    for patinador in self.__lista:
      print(patinador)
  
  def edad(self,DNI):
    for patinador in self.__lista:
      if patinador.getDNI() == DNI:
        return patinador.getEdad()

  def nomyape(self, DNI):
    for patinador in self.__lista:
      if patinador.getDNI() == DNI:
        return f"{patinador.getNom()}  {patinador.getApe()}"
      
  def club(self,DNI):
    i = 0
    while i < len(self.__lista):
      if self.__lista[i].getDNI() == DNI: #ocupo un while para probar nomás, se puede hacer con for(supongo)
        return self.__lista[i].getClub()
      else:
        i+=1