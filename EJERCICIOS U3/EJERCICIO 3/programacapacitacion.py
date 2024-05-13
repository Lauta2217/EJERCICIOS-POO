class Programacapacitacion:
  __nom: str
  __cod: str
  __duracion: str
  __matricula: []
  def __init__(self,nom,cod,duracion):
    self.__nom = nom
    self.__cod = cod
    self.__duracion = duracion
    self.__matricula = []
  
  @property
  def nom(self):
    return str(self.__nom)
  @property
  def cod(self):
    return str(self.__cod)
  @property
  def duracion(self):
    return self.__duracion
  @property
  def matricula(self):
    return self.__matricula
  
  def __str__(self):
    return f"{self.__cod}\n"
    
  def __lt__(self,otro):
    if self.__cod < otro.__cod:
      return self.__cod < otro.__cod
    
  def addmatricula(self,matricula):
    self.__matricula.append(matricula)