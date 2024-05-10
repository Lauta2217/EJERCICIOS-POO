from gestor_material import *
from clase_ladrillo import *
from clase_material_refrectario import *
class gestor_ladrillo:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista
    
  def crear_ladrillo(self,GM):
    lista = GM.lista
    print(f"{lista[0].material}")
    op = int(input("ingrese cantidad de ladrillos a pedir o 0 para finalizar\n"))
    while op != 0:
      iden = input("Ingrese identificador de ladrillo\n")
      kgmatpri = input("Ingrese cantidad de KG de material primario\n")
      r = input("Quiere adiccionar material reclicado? S/N\n")
      if r.upper() == 'S':
        mat = input("Ingrese nombre del material\n")
        band = False
        i= 0
        while i < len(lista) and not band:
          if lista[i].material == mat:
            band = True
            ladri = Ladrillo(7,25,15,op,iden,kgmatpri,100,lista[i])
            self.__lista.append(ladri)
          else:
            i+=1
      elif r.upper() == 'N':
        ladri = Ladrillo(7,25,15,op,iden,kgmatpri,100,None)
        self.__lista.append(ladri)
      else:
        print("Material ingresado incorrecto\n")
      op = int(input("ingrese cantidad de ladrillos a pedir o 0 para finalizar\n"))
  
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
      if self.__lista[i].idd == idd:
        band = False
      else:
        i+=1
    if not band:
      if self.__lista[i].material_refrectario == None:
        print(f"No tiene material agregado")
      else:
        print(f"Costo del material: {self.__lista[i].material_refrectario.costo_adicional}\ncaracteristicas del material:{self.__lista[i].material_refrectario.caracteristicas}")
  
  def total(self,GL ):
    i = 0
    while i < len(self.__lista):
      if isinstance(self.__lista[i].material_refrectario,mate_refrec) :
        print(f"Para el ladrillo con id: {self.__lista[i].idd} su costo total de fabricacion más el csoto por material agregado es:{GL.calcular_total(i)}")
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
    
    
  
