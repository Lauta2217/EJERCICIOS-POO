from calefactor import Calefactor
class Calefactor_elec(Calefactor):
    __potencia_max: int
    def __init__(self,ma,mo,pdf,pdl,fdp,cc,p,pm):
      super().__init__(ma,mo,pdf,pdl,fdp,cc,p)
      self.__potencia_max = pm
      
    def calcular_precio(self):
      precio = super().precio_de_lista
      if self.__potencia_max > 1000:
        if super().forma_de_pago == "cuotas":
          precio += precio + (precio * 1.30)
        else:
          precio += precio
      if super().promocion == "si":
        precio-= precio * 1.15 
      return precio
    @property
    def potencia_max(self):
      return self.__potencia_max
    def __str__(self):
      return super().__str__() + f"{self.__potencia_max}W"       