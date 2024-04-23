import csv
from equipos import *
class Fechas():
  def __init__(self,fecha_partido, idd_de_Elocal, idd_de_Evisitante, cant_G_Elocal,cant_G_Evisitante):
    self.__fecha_partido = fecha_partido
    self.__idd_de_Elocal = idd_de_Elocal
    self.__idd_de_Evisitante = idd_de_Evisitante
    self.__cant_G_Elocal = cant_G_Elocal
    self.__cant_G_Evisitante = cant_G_Evisitante
  
  def __str__(self): #cuando yo coloque print(fechas) muestra por pantalla lo que retorna la funcion
    return self.__idd_de_Elocal
  
class gestorfechas():
  def __init__(self, lista = []):
    self.__lista = lista
  
  def cargar_fechas_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/EJERCICIO 5/fechasFutbol.csv",newline='') as archivo_csv: #sirve para abrir un archivo y le da un nombre "archivo_csv"
      reader = csv.reader(archivo_csv) #almacena los datos del archivo en una variable
      for fila in reader: #itera los datos del archivo que fueron pasados a la variable por fila
        fechas = Fechas(*fila) #a una variable le asigna los atributos que tiene el archivo y que deben ser iguales a los que tiene la clase
        self.__lista.append(fechas) #agrega los atributos a la lista
    print("Fechas cargadas correctamente\n")
    
  def mostrar(self):
    for fechas in self.__lista:
      print(fechas)#usa el operador str 
            
  def buscarfechas(self,idd): #Esta funcion la llamo desde el gestor equipos
    f = []
    for fechas in self.__lista: #me muevo por las fechas de la lista
      if idd == fechas._Fechas__idd_de_Elocal or idd == fechas._Fechas__idd_de_Evisitante: #Verifica si el id del equipo que estoy buscando ha jugado en tal fecha como local o visitante
        f.append(fechas._Fechas__fecha_partido) #si ha jugado entonces lo guardo en una lista
    return f
  def buscarequipo(self,idd):
    for fechas in self.__lista:
      if fechas._Fechas__idd_de_Elocal == idd or fechas._Fechas__idd_de_Evisitante == idd: #verifico si el equipo que estoy buscando ha jugado
        return True
  def obtener_goles_favor(self, idd): #obtengo los goles que el equipo hizo como local o vistante en cada fecha
    suma = 0
    for fechas in self.__lista:
        if fechas._Fechas__idd_de_Elocal == idd: #si el equipo jugo como local tomo los goles del local
            suma += int(fechas._Fechas__cant_G_Elocal)
        elif fechas._Fechas__idd_de_Evisitante == idd: #si el equipo jugo como visitante tomo los goles del visitante
            suma += int(fechas._Fechas__cant_G_Evisitante)
    return suma

  def obtener_goles_contra(self,idd):#obtengo los goles que le hicieron al equipo como local o vistante en cada fecha
    suma = 0
    for fechas in self.__lista:
      if fechas._Fechas__idd_de_Elocal == idd:  #si el equipo jugo como local tomo los goles del visitante
        suma+= int(fechas._Fechas__cant_G_Evisitante)
      elif fechas._Fechas__idd_de_Evisitante == idd:  #si el equipo jugo como visitante tomo los goles del local
        suma+= int(fechas._Fechas__cant_G_Elocal)
    return suma
  
        
      
        