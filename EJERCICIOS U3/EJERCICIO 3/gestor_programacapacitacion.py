import csv
from programacapacitacion import *
class gestor_programacapacitacion:
  __lista: list
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_programas_desde_csv(self):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 3/programacapacitacion.csv",newline='',encoding='utf-8') as archivo_csv: 
        reader = csv.reader(archivo_csv,delimiter=';') 
        next(reader)
        for fila in reader: 
          pc = Programacapacitacion(*fila) 
          self.__lista.append(pc) 
        print("Programas de capacitacion cargados correctamente\n")
  
  def ordenar(self):
    self.__lista = sorted(self.__lista)
  
  def buscarprograma(self,cod):
    i = 0
    band = False
    if cod == None:
      return None
    else:
      while i < len(self.__lista) and not band:
        if self.__lista[i].cod == cod:
          band = True
        else:
          i+=1
      if band:
        return self.__lista[i]
      
  def mostrar(self):
    for programa in self.__lista:
      print(programa)
      
  def buscar_empleados_en_programa(self,programa):
    i = 0
    j = 0
    band = False
    while i < len(self.__lista) and not band:
      if self.__lista[i].nom.lower() == programa.lower():
        band = True
      else:
        i+=1
    if not band:
      print("No existe el programa ingresado\n")
    else:
      for matri in self.__lista[i].matricula:
        if matri.empleado.idempleado != None and matri.empleado != None:  #contempla la posibilidad de que si haya programa, pero que no esté ningun empleado en ese programa o que no exista el empleado
          print(f"{matri.empleado.nomyape}")
          band = False
      if band:
        print("El programa no tiene empleados\n")
  
        
        
        
        
      """for matri in self.__lista[i].matricula:
        if matri.empleado != None:
          band = True
          print(f"{matri.empleado.nomyape}\n")"""
          
        
        
       