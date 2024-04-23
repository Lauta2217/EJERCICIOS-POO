import csv
from fechas import *
class Equipos():
  def __init__(self,idd_equipo, nom_equipo,goles_a_favor, goles_en_contra, dif_de_goles,puntos):
    self.__idd_equipo = idd_equipo
    self.__nom_equipo = nom_equipo
    self.__goles_a_favor = goles_a_favor
    self.__goles_en_contra = goles_en_contra
    self.__dif_de_goles = dif_de_goles
    self.__puntos = puntos
  def __str__(self):
    return self.__nom_equipo
  
class gestorequipos():
  def __init__(self,lista = []):
    self.__lista = lista
    
  def cargar_equipos_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS/EJERCICIO 5/equipos2024.csv",newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        equipos = Equipos(*fila)
        self.__lista.append(equipos)
    print("Los equipos fueron cargados correctamente\n")
    
  def mostrar(self):
    for equipos in self.__lista:
      print(equipos)    
  def buscar(self,GF):
    i = 0
    nom = str(input("Ingrese nombre del equipo a buscar\n")).strip().lower()
    for equipos in self.__lista:
      if nom == equipos._Equipos__nom_equipo.strip().lower():
        f = GF.buscar(equipos._Equipos__idd_equipo)
        print(f"Equipo:{nom} \n")
        print(" Fecha         Goles a Favor       Goles en Contra      Diferencia de Goles        Puntos")
        for fecha in f:
          i+=1
          print(f"{fecha:<20}{equipos._Equipos__goles_a_favor:<17} {equipos._Equipos__goles_en_contra:<30} {equipos._Equipos__dif_de_goles:<15} {equipos._Equipos__puntos:<20}")
        print("-----------------------------------------------------------------------------------------------\n")
        print(f"Total:  {(i * int(equipos._Equipos__goles_a_favor)):<17 } {(i * int(equipos._Equipos__goles_en_contra)):<30} {(i * int(equipos._Equipos__dif_de_goles)):<15} {(i * int(equipos._Equipos__puntos)):<20}")
        
  
    

        