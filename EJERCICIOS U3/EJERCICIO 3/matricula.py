class Matricula:
  __fecha: str
  __empleado:None
  __programacapacitacion:None
  def __init__(self,fecha,empleado,programacapacitacion):
    self.__fecha = fecha
    self.__empleado = empleado
    self.__programacapacitacion = programacapacitacion
    if empleado != None:
      self.__empleado.addmatricula(self)
    if programacapacitacion != None:
      self.__programacapacitacion.addmatricula(self)
  
  @property
  def fecha(self):
    return self.__fecha
  @property
  def empleado(self):
    return self.__empleado
  @property
  def programacapacitacion(self):
    return self.__programacapacitacion
  
  def __str__(self):
    if self.__programacapacitacion != None and self.__empleado != None:
      return f"{self.__fecha} {self.__empleado.nomyape} {self.__programacapacitacion.nom}\n"
    elif self.__empleado != None:
      return f"{self.__fecha} {self.__empleado.nomyape}\n"
    else:
      return f"{self.__fecha}"
  
    