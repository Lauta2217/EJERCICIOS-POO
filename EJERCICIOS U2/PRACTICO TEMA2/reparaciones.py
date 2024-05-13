import csv
class Reparacion:
  __patente:str
  __reparacion:str
  __repuesto:str
  __precioRepuesto:float
  __precioManoObra:float
  __estado:str

  def __init__(self, patente,reparacion,repuesto,precioRepuesto,precioManoObra,estado):
    self.__patente = patente
    self.__reparacion = reparacion
    self.__repuesto = repuesto
    self.__precioRepuesto = precioRepuesto
    self.__precioManoObra = precioManoObra
    self.__estado = estado
  
  def __str__(self):
    return f"{self.__patente}\n{self.__reparacion}\n{self.__repuesto}\n{self.__precioRepuesto}\n{self.__precioManoObra}\n{self.__estado}\n"
  
  def getrepa(self):
    return self.__reparacion
  
  def getpaten(self):
    return self.__patente
  
  def getpresu(self):
    return self.__precioRepuesto
  
  def getMO(self):
    return self.__precioManoObra
  
  def getSubT(self):
    return float(float(self.__precioRepuesto) + float(self.__precioManoObra))
  
  def getestado(self):
    return self.__patente
  
class gestor_reparaciones:
  __lista = list
  
  def __init__(self,lista = []):
    self.__lista = lista
  
  def cargar_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/PRACTICO TEMA2/reparaciones.csv", newline='', encoding='utf-8') as archivo_csv:
      reader = csv.reader(archivo_csv, delimiter=';')
      for fila in reader:
        repa = Reparacion(*fila)
        self.__lista.append(repa)
      print("Reparaciones cargadas\n")
  
  def mostrar(self):
    for repa in self.__lista:
      print(repa)
  
  def mostrarRepa(self,patente):
    total = 0
    print(f"""
              Reparación                precio repuesto                     mano de obra           subtotal 
          """)
    
    for repa in self.__lista:
      if repa.getpaten() == patente:
        print(f"                {repa.getrepa()}                {repa.getpresu()}                    {repa.getMO()}                 {float(repa.getSubT())}\n")
        total += repa.getSubT()
    print(f"TOTAL:{total}")
    
  def repaterminadas(self,GC):
    patente = input("ingrese patente\n")
    band = True
    total = 0
    for repa in self.__lista:
      if repa.getpaten() == patente:
        if repa.getestado() == 'P':
          band = False
        else:
          total += repa.getSubT() 
    if band:
      GC.cambiarestado(patente,total)
        
        
      
      
      
    
      
        
    
