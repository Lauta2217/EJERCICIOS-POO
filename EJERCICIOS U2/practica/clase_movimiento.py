class Movimiento:
  __num_t: int
  __fecha: str 
  __descripcion: str
  __tipo_M: str
  __importe: float
  
  def __init__(self,num_t,fecha,descripcion,tipo_M,importe):
    self.__num_t = num_t
    self.__fecha = fecha
    self.__descripcion = descripcion
    self.__tipo_M = tipo_M
    self.__importe = float(importe)
    
  def __str__(self):
    return f"Numero de tarjeta:  {self.__num_t}\nDescripcion:  {self.__descripcion}\nImporte:  {self.__importe}\n"
  
  def getnum_T(self):
    return self.__num_t
  
  def getfecha(self):
    return self.__fecha
  
  def getdescripcion(self):
    return self.__descripcion
  
  def gettipo_M(self):
    return self.__tipo_M

  def getimporte(self):
    return self.__importe
  
  def __lt__(self,other):
    return self.__num_t < other.__num_t
