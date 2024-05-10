class Departamentos():
  __idd = int
  __nomyape = str
  __num_piso = int
  __num_depa = int
  __cant_dormi = int
  __cant_baños = int
  __superficie_cubierta = float
  
  def __init__(self,idd,nomyape,num_piso,num_depa,cant_dormi,cant_baños,superficie_cubierta):
    self.__idd = idd
    self.__nomyape = nomyape
    self.__num_piso = num_piso
    self.__num_depa = num_depa
    self.__cant_dormi = cant_dormi
    self.__cant_baños = cant_baños
    self.__superficie_cubierta = float(superficie_cubierta.replace(",","."))
  @property
  def nomyape(self):
    return self.__nomyape
  @property
  def num_depa(self):
    return int(self.__num_depa)
  @property
  def num_piso(self):
    return int(self.__num_piso)
  @property
  def cant_baños(self):
    return int(self.__cant_baños)
  @property
  def cant_dormi(self):
    return int(self.__cant_dormi)
  @property
  def superficie_cubierta(self):
    return float(self.__superficie_cubierta)
  
  def __str__(self):
    return f"{self.__nomyape}\n"
  

    
