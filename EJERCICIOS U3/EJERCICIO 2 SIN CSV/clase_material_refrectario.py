class mate_refrec:
  __material: str
  __caracteristicas: str
  __cant_utilizada: int
  __costo_adicional:float
  def __init__(self, material,cant_utilizada,costo_adicional,caracteristicas):
    self.__material = material
    self.__caracteristicas = caracteristicas
    self.__cant_utilizada = cant_utilizada
    self.__costo_adicional = costo_adicional
  
  @property
  def material(self):
    return self.__material
  @property
  def caracteristicas(self):
    return self.__caracteristicas
  @property
  def cant_utilizada(self):
    return self.__cant_utilizada
  @property
  def costo_adicional(self):
    return int(self.__costo_adicional)
  def __str__(self):
    return f"{self.__caracteristicas}\n"