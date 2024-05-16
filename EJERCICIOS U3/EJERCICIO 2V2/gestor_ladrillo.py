from gestor_material import *
from clase_ladrillo import *
from clase_material_refrectario import *
class gestor_ladrillo:
  __lista = list
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_ladrillo_desde_csv(self,GM):
    with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 2V2/ladrillos.csv",newline='',encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter=';')
      next(reader)
      for fila in reader:
        ladri = Ladrillo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
        materiales = fila[7].split(',')
        for material in materiales:
          mate = GM.crearobjeto(material)
          if mate!= None:
            ladri.material_refrectario.append(mate)
        self.__lista.append(ladri) 
      print("Ladrillos creados correctamente\n")
  
  def mostrar(self):
    for ladrillo in self.__lista:
      print(ladrillo)
      
  def calcular_total(self,i):
    total = 0
    for mate in self.__lista[i].material_refrectario:
      if isinstance(mate,mate_refrec):
        total += mate.costo_adicional
    if total == 0:
      return self.__lista[i].costo * self.__lista[i].cant
    else:
      return (total + self.__lista[i].costo) * self.__lista[i].cant
    
  def buscar(self,idd):
    i = 0
    band = True
    while i < len(self.__lista) and band:
      if self.__lista[i].idd == int(idd):
        band = False
      else:
        i+=1
    if not band:
      j = 0
      while j < len(self.__lista[i].material_refrectario):
        if isinstance(self.__lista[i].material_refrectario[j],mate_refrec):
          print(f"Costo del material: {self.__lista[i].material_refrectario[j].costo_adicional}\ncaracteristicas del material:{self.__lista[i].material_refrectario[j].caracteristicas}")
        j+=1
    else:
      print(f"No existe el ladrillo")
  def calcular_total_parameteriales(self,i):
    total = 0
    for materiales in self.__lista[i].material_refrectario:
      if isinstance(materiales,mate_refrec):
        total+= materiales.costo_adicional
    return (total + self.__lista[i].costo)* self.__lista[i].cant
  def total(self,GL):
    i = 0
    j = 0
    while i < len(self.__lista):
      band = True
      while j < len(self.__lista[i].material_refrectario):
        if isinstance(self.__lista[i].material_refrectario[j],mate_refrec):
          band = False
        j+=1
      if band:
        print(f"Para el ladrillo con id: {self.__lista[i].idd} su costo total de fabricacion es: {GL.calcular_total(i)}")
      else:
        print(f"Para el ladrillo con id: {self.__lista[i].idd} su costo total de fabricacion más el costo por material agregado es:{GL.calcular_total_parameteriales(i)}")
      i+=1
      j=0
  
  def mostrar_todo(self,GL):
    i = 0
    print(""" N° identificador         Material        Costo asociado 
          """)
    while i < len(self.__lista):
      if len(self.__lista[i].material_refrectario) > 0:
        print(f"{self.__lista[i].idd}                                                          {GL.calcular_total_parameteriales(i)}")
        for mate in self.__lista[i].material_refrectario:
            print(f"                   {mate.material}             ")
      else:
        print(f"\n{self.__lista[i].idd}                  Material no reciclado         {self.__lista[i].costo * self.__lista[i].cant}")
      i+=1