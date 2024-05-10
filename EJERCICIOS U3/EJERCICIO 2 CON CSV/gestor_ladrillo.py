from gestor_material import *
from clase_ladrillo import *
from clase_material_refrectario import *
class gestor_ladrillo:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_ladrillo_desde_csv(self,GM):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 2 CON CSV/ladrillos.csv",newline='',encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter=';')
      next(reader)
      for fila in reader:
        ladri = Ladrillo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],GM.crearobjeto(str(fila[7])))
        self.__lista.append(ladri)
      print("Ladrillos creados correctamente\n")
  
  def mostrar(self):
    for ladrillo in self.__lista:
      print(ladrillo)
      
  def calcular_total(self,i):
    if self.__lista[i].material_refrectario == None:
      return self.__lista[i].costo * self.__lista[i].cant
    else:
      return (self.__lista[i].costo + self.__lista[i].material_refrectario.costo_adicional) * self.__lista[i].cant
    
  def buscar(self,idd):
    i = 0
    band = True
    while i < len(self.__lista) and band:
      if self.__lista[i].idd == int(idd):
        band = False
      else:
        i+=1
    if not band:
      if isinstance(self.__lista[i].material_refrectario,mate_refrec):
        print(f"Costo del material: {self.__lista[i].material_refrectario.costo_adicional}\ncaracteristicas del material:{self.__lista[i].material_refrectario.caracteristicas}")
      else:
        print(f"No tiene material agregado")
        
  def total(self,GL ):
    i = 0
    while i < len(self.__lista):
      if isinstance(self.__lista[i].material_refrectario,mate_refrec):
        print(f"Para el ladrillo con id: {self.__lista[i].idd} su costo total de fabricacion más el costo por material agregado es:{GL.calcular_total(i)}")
      else:
        print(f"Para el ladrillo con id: {self.__lista[i].idd} su costo total de fabricacion es: {GL.calcular_total(i)}")
      i+=1
  def mostrar_todo(self,GL):
    i = 0
    print(""" N° identificador         Material        Costo asociado 
          """)
    while i < len(self.__lista):
      if isinstance(self.__lista[i].material_refrectario,mate_refrec):
        print(f"{self.__lista[i].idd}                  {self.__lista[i].material_refrectario.material}           {GL.calcular_total(i)}")
      else:
        print(f"{self.__lista[i].idd}                  Material no reciclado         {GL.calcular_total(i)}")
      i+=1