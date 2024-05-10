from gestor_edificios import *
class Edificio:
  __idd = int
  __nom = str
  __direccion = str
  __nom_empresa = str
  __cant_pisos = int
  __cant_depa = int
  __departamentos = list
  def __init__(self,idd,nom,direccion,nom_empresa,cant_pisos,cant_depa):
    self.__idd = idd
    self.__nom = nom
    self.__direccion = direccion
    self.__nom_empresa = nom_empresa
    self.__cant_pisos = cant_pisos
    self.__cant_depa = cant_depa
    self.__departamentos = []
    
  def agregar_departamento(self,depa):
    return self.__departamentos.append(depa)
    
  def __str__(self):
    return f"{self.__nom}:"
  
  @property
  def departamentos(self):
    return self.__departamentos
  
  @property
  def nom(self):
    return self.__nom
  
  @property
  def idd(self):
    return self.__idd
  