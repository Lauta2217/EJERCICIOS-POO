class Evaluacion:
    __DNI: int
    __Estilo_P: str
    __Valoracion1: float
    __Valoracion2: float
    __Valoracion3: float
  
    def __init__(self,DNI,Estilo_P,Valoracion1,Valoracion2,Valoracion3):
      self.__DNI = DNI
      self.__Estilo_P = Estilo_P
      self.__Valoracion1 = float(Valoracion1)
      self.__Valoracion2 = float(Valoracion2)
      self.__Valoracion3 = float(Valoracion3)
    
    def __str__(self):
      return f"DNI:{self.__DNI}\nESTILO:{self.__Estilo_P}\nVALORACION1:{self.__Valoracion1}\nVALORACION2:{self.__Valoracion2}\nVALORACION3:{self.__Valoracion3}\n"

    def getEstilo(self):
      return self.__Estilo_P
    
    def getDNI(self):
      return self.__DNI
    
    def promVa(self):
      return ((self.__Valoracion1 + self.__Valoracion2 + self.__Valoracion3) / 3)
    
    def getValoraciones(self):
      return f"{self.__Valoracion1} | {self.__Valoracion2} | {self.__Valoracion3}"
  
    def __gt__(self,other): #sobre carga de operador >
        return self.promVa() > other.promVa()
      

        
        
    
    
      
      
        
