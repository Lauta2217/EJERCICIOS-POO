from clase_material_refrectario import *
import csv
class gestor_material:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_material_desde_csv(self):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 2 SIN CSV/decoracionezzz.csv",newline='',encoding='utf-8') as archivo_csv: 
        reader = csv.reader(archivo_csv,delimiter=';') 
        next(reader)
        for fila in reader: 
          material = mate_refrec(*fila) 
          self.__lista.append(material) 
        print("Material cargados correctamente\n")
  
  def mostrar(self):
    for mate in self.__lista:
      print(mate)
  @property
  def lista (self):
    return self.__lista