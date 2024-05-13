import csv
from empleados import *
class gestor_empleados:
  __lista: list
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_empleados_desde_csv(self):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 3/empleados.csv",newline='',encoding='utf-8') as archivo_csv: 
        reader = csv.reader(archivo_csv,delimiter=';') 
        next(reader)
        for fila in reader: 
          empleados = Empleados(*fila) 
          self.__lista.append(empleados) 
        print("Empleados cargados correctamente\n")
  
  def ordenar(self):
    self.__lista = sorted(self.__lista)
  
  def buscarempleado(self,idd):
    i = 0
    band = False
    if idd == None:
      return None
    else:
      while i < len(self.__lista) and not band:
        if self.__lista[i].idempleado == idd:
          band = True
        else:
          i+=1
      if band:
        return self.__lista[i]
      
  def mostrar(self):
    for emple in self.__lista:
      print(emple)
  
  def buscar_programas_del_empleado(self,idd):
    i = 0
    j = 0
    band = False
    while i < len(self.__lista) and not band:
      if self.__lista[i].idempleado == idd:
        band = True
      else:
        i+=1
        
    if not band:
      print("No hay empleado registrado con ese id\n")
    else:
      while j < len(self.__lista[i].matricula):
        if self.__lista[i].matricula[j].programacapacitacion != None and self.__lista[i].matricula[j].programacapacitacion.nom != None: #contempla la posibilidad de que si haya usuario, pero que al programa que este matriculado no exista(no se haya ingresado) o que no exista el nombre
          band = False
          print(f"{self.__lista[i].matricula[j].programacapacitacion.nom}\n")
        j+=1
        
      if band:
        print(f"El empleado {self.__lista[i].nomyape} no participa en ningun programa\n")
        
  def informar_empleados(self):
    band = False
    empleados_sin_programa = []
    for emple in self.__lista:
      if emple.matricula == []: #pregunta si la lista de matriculas del empleado está vacia
        band = True
        empleados_sin_programa.append(emple)
    if not band:
      print("Todos los empleados participan en un programa\n")
    else:
      print("Empleados sin programa:\n")
      for emple in empleados_sin_programa:
        print(emple)
         
      
          
          
  