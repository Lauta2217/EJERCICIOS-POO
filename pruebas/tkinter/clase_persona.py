class Persona:
  __nom: str
  __edad: int
  def __init__(self,nom,edad):
    self.__nom = nom
    self.__edad = edad
  def __str__(self):
    return f"{self.__nom} {self.__edad}\n"

      