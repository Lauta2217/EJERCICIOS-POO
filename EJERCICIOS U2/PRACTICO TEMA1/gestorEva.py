from clase_evaluacion import *
from gestorPati import *
import csv
class gestor_evaluaciones:
  __lista: list
  
  def __init__(self,lista = []):
    self.__lista = lista
    
  def cargar_evaluaciones_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/PRACTICO TEMA1/evaluacion.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        eva = Evaluacion(*fila)
        self.__lista.append(eva)
      print("Evaluaciones cargadas\n")
      
  def mostrar(self):
    for evaluacion in self.__lista:
      print(evaluacion)
  
  def mostrarestilo(self,GP):
    estilo = input("Ingrese estilo a mostrar\n")
    edad = input("Ingrese edad\n")
    DNI = eva.getDNI()
    for eva in self.__lista:
      if eva.getEstilo() == estilo and GP.edad(DNI) == edad:
        print(f"{GP.nomyape(DNI)}\n{DNI}\n")
        
  def mayorpuntaje(self,GP):
    maxi = max(self.__lista)
    DNI = maxi.getDNI()
    print(f"PATINADOR CON EL MAYOR PUNTAJE ES:\nNOMBRE Y APELLIDO:{GP.nomyape(DNI)}ESTILO:{maxi.getEstilo()}\nCLUB:{GP.club(DNI)}\n")
  
  def listartodo(self,GP):
    for eva in self.__lista:
      DNI = eva.getDNI()
      print(f"""
            NOMBRE Y APELLIDO: {GP.nomyape(DNI)}
            DNI: {DNI}
            EDAD: {GP.edad(DNI)}
            CLUB: {GP.club(DNI)}
            ESTILO: {eva.getEstilo()}
            VALORACION 1, VALORACION 2 Y VALORACION 3: {eva.getValoraciones()}
          ----------------------------------------------------------------------
        """)
  def buscar_DE(self):
    DNI = input("ingrese dni a buscar\n")
    e = input("estilo a buscar\n")
    for eva in self.__lista:
      if eva.getDNI() == DNI and eva.getEstilo() == e:
        print(f"VALORACION 1, VALORACION 2 Y VALORACION 3: {eva.getValoraciones()}")
      else:
        print("Alguno de los datos ingresados no coicide\n")