from clase_material_refrectario import *
import csv
class gestor_material:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_material_desde_csv(self):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 2V2/materiales.csv",newline='',encoding='utf-8') as archivo_csv: 
        reader = csv.reader(archivo_csv,delimiter=';') 
        next(reader)
        for fila in reader: 
          material = mate_refrec(*fila) 
          self.__lista.append(material) 
        print("Material cargados correctamente\n")
        
  def crearobjeto(self,idd):
    i = 0
    print(f"id:{idd}")
    band = False
    while i < len(self.__lista) and not band:
      if self.__lista[i].idd == idd:
        band = True
      else:
        i+=1
    if band:
      return self.__lista[i]
    else:
      return None
  def mostrar(self):
    for mate in self.__lista:
      print(mate)
