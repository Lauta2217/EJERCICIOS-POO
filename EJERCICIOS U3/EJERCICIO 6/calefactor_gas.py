from calefactor import Calefactor
class Calefactor_gas(Calefactor):
    __matricula: str
    __calorias: int
    def __init__(self,ma,mo,pdf,pdl,fdp,cc,p,mat,cal):
      super().__init__(ma,mo,pdf,pdl,fdp,cc,p)
      self.__matricula = mat
      self.__calorias = cal
      
    def calcular_precio(self):
      precio = super().precio_de_lista
      print(f"{precio}")
      if self.__calorias > 3000:
        if super().forma_de_pago == "cuotas":
          precio += precio + (precio * 1.40)
        else:
          precio += precio
      if super().promocion == "si":
        precio-= precio * 1.15 
      return precio
    @property
    def calorias(self):
      return self.__calorias
    @property
    def matricula(self):
      return self.__matricula
    def __str__(self):
      return super().__str__() + f"{self.__matricula}\n { self.__calorias}\n" 