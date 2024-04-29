class Patinador:
  __ape: str
  __nom: str 
  __DNI: int
  __edad: int 
  __club: str
  def __init__(self,ape,nom,DNI,edad,club):
    self.__ape = ape
    self.__nom = nom
    self.__DNI = DNI
    self.__edad = edad
    self.__club = club
    
  def __str__(self):
    return f"APELLIDO:{self.__ape}\nNOMBRE:{self.__nom}\nDNI:{self.__DNI}\nEDAD:{self.__edad}\nCLUN:{self.__club}\n"
  
  def getDNI(self):
    return self.__DNI
  
  def getEdad(self):
    return self.__edad
  
  def getNom(self):
    return self.__nom
  
  def getApe(self):
    return self.__ape

  def getClub(self):
    return self.__club
