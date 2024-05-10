class Ladrillo:
  __alto: int
  __largo: int
  __cant: int
  __idd: int
  __kg_Mat_prim_uti: float
  __costo: float
  __material_refrectario: object
  def __init__(self,alto, largo, ancho,cant,idd,kg_Mat_prim_uti,costo,material):
    self.__alto = alto
    self.__largo = largo
    self.__ancho = ancho
    self.__cant = cant
    self.__idd = idd
    self.__kg_Mat_prim_uti = kg_Mat_prim_uti
    self.__costo = costo
    self.__material_refrectario = material #agregacion
  def __str__(self):
    return f"{self.__idd} {self.__material_refrectario}"
  @property
  def idd(self):
    return int(self.__idd)
  @property
  def material_refrectario(self):
    return self.__material_refrectario
  @property
  def costo(self):
    return int(self.__costo)
  @property
  def cant(self):
    return int(self.__cant)