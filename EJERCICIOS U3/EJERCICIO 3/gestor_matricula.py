import csv
from gestor_empleados import *
from gestor_programacapacitacion import *
from matricula import *
class gestor_matricula:
  __lista: list
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_matriculas_desde_csv(self,GE,GP):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 3/matricula.csv",newline='',encoding='utf-8') as archivo_csv: 
        reader = csv.reader(archivo_csv,delimiter=';') 
        next(reader)
        for fila in reader: 
          matricula = Matricula(fila[0],GE.buscarempleado(fila[1]),GP.buscarprograma(fila[2])) #las funciones de los 2 gestores van a corroborar que los datos ingresados coiciden así pueden devolver el objeto y en caso de que no se haya ingresado algo o que no exista devulve None
          self.__lista.append(matricula) 
        print("Matriculas cargadas correctamente\n")
        
  def mostrar(self):
    for matri in self.__lista:
      print(matri)
      
  
        
      
      
        
    
      
        
  