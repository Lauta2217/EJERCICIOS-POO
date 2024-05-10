from clase_departamento import *
from clase_edificio import *
import csv
class gestor_edificios:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista

  def cargar_edificios_desde_csv(self):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 1/EdificioNorte.csv", newline='',encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter=';')
      edificio_actual = None
      for fila in reader:
        if len(fila) == 6: #es edificio
          edificio_actual = Edificio(*fila)
          self.__lista.append(edificio_actual)
        elif len(fila) == 7: #es departamento 
          departamento = Departamentos(*fila)
          edificio_actual.agregar_departamento(departamento)
      print("EDIFICIOS CARGADOS\n")
      
  def mostrar(self):
    for edif in self.__lista:
      print(edif)
      for depa in edif.departamentos:
        print(depa)
        
  def mostrar_propietarios(self,nom_E):
    i = 0
    band = True
    while i < len(self.__lista) and band:
      if self.__lista[i].nom.lower() == nom_E.lower():
        band = False
      else:
        i+=1
    if not band:
      for depa in self.__lista[i].departamentos:
        print(depa)
          
  def superficie(self,nom_E):
    i = 0
    sup = 0
    band = True
    while i < len(self.__lista) and band:
      if self.__lista[i].nom.lower() == nom_E.lower():
        band = False
      else:
        i+=1
    if not band:
      for depa in self.__lista[i].departamentos:
        sup+= float(depa.superficie_cubierta)
    return sup
    
  def buscarnomE(self,idd):
    i = 0
    band = False
    while i < len(self.__lista) and band:
      if self.__lista[i].idd == idd:
        band = False
      else:
        i+=1
      
    if not band:
      return self.__lista[i].nom
    
  def suppropie(self,nom_P,GE):
    i = 0
    sup = 0
    band = True
    while i < len(self.__lista) and band:
      idd = self.__lista[i].idd
      for depa in self.__lista[i].departamentos:
        if depa.nomyape.lower() == nom_P.lower():
          band = False
          sup += depa.superficie_cubierta
      i+=1
    if sup!=0:
      print(f"id del edificio: {idd}")
      porcentaje = 100 * (sup / GE.superficie(GE.buscarnomE(idd)))
      return porcentaje
    else:
      print("No hay papu con ese nombre\n")
  
  def contar(self,num):
    for edi in self.__lista:
      cont = 0
      print(f"Para el {edi.nom}")
      for depa in edi.departamentos:
        if depa.num_piso == num:
          if depa.cant_dormi == 3 and depa.cant_baños > 1:
              cont+=1
      print(f"Numero de departamentos con 3 dormitorios y más de un baño  en el piso {num} es: {cont}\n")
      
    
      
    
    
    
        
    