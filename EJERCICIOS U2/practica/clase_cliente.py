class Cliente:
  __nom: str
  __ape: str 
  __DNI: int
  __num_t: int 
  __saldo_A: float
  def __init__(self,nom,ape,DNI,num_t,saldo_A):
    self.__nom = nom
    self.__ape = ape
    self.__DNI = DNI
    self.__num_t = num_t
    self.__saldo_A = saldo_A
    
  def __str__(self):
    return f"Apellido:  {self.__ape}\nNombre:  {self.__nom}\nNumero de tarjeta:  {self.__num_t}\n"
  
  def getNom(self):
    return self.__nom
  def getApe(self):
    return self.__ape
  def getDNI(self):
    return self.__DNI
  def getnum_T(self):
    return self.__num_t
  def getsaldo_A(self):
    return self.__saldo_A
  def setsaldo(self,saldo):
    self.__saldo_A = saldo
    return