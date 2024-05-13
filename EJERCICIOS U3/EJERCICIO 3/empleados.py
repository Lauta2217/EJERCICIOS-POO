class Empleados:
  __nomyape: str
  __idempleado : str
  __puesto: str
  __matricula: list
  def __init__(self,nomyape,idempleado,puesto):
    self.__nomyape = nomyape
    self.__idempleado = idempleado
    self.__puesto = puesto
    self.__matricula = [] #composicion
    
  @property #decorador para no usar gets
  def nomyape(self):
    return str(self.__nomyape)
  @property
  def idempleado(self):
    return str(self.__idempleado)
  @property
  def puesto(self):
    return str(self.__puesto)
  @property
  def matricula(self):
    return self.__matricula
  
  def __str__(self): #sobrecarga de operadores para mostrar
    return f"{self.__nomyape}\n"
  def __lt__(self,otro): #sobrecarga de operadores para ordenar                         
    if self.__idempleado < otro.__idempleado:
      return self.__idempleado < otro.__idempleado
  
  def addmatricula(self,matricula): #quitar
    self.__matricula.append(matricula)