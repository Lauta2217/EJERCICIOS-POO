from abc import ABC, abstractmethod
class Calefactor(ABC):
    __marca: str
    __modelo: str
    __pais_de_fabricacion: str
    __precio_de_lista: float
    __forma_de_pago: str
    __cant_cuotas: int
    __promocion: str
    def __init__(self,ma,mo,pdf,pdl,fdp,cc,p):
        self.__marca = ma
        self.__modelo = mo
        self.__pais_de_fabricacion = pdf
        self.__precio_de_lista = pdl
        self.__forma_de_pago = fdp
        self.__cant_cuotas = cc
        self.__promocion = p
    
    @abstractmethod
    def calcular_precio(self):
        pass
    @property
    def precio_de_lista(self):
        return self.__precio_de_lista
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @property
    def forma_de_pago(self):
        return self.__forma_de_pago
    @property
    def promocion(self):
        return self.__promocion
    @property
    def pais_de_fabricacion(self):
        return self.__pais_de_fabricacion
    @property
    def cant_cuotas(self):
        return self.__cant_cuotas
    def __str__(self):
        return f"{self.__marca}\n{self.__modelo}\n{self.__pais_de_fabricacion}\n{self.__precio_de_lista}\n{self.__forma_de_pago}\n{self.__cant_cuotas}\n{self.__promocion}\n"
    
	

	
	