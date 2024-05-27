from docente import *
from investigador import *

class Docente_Investigador(Docente, Investigador):
    __categoria_incentivo: str
    __importe_extra:str
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.__categoria_incentivo = kwargs.get('categoria_incentivo',None)
        self.__importe_extra = kwargs.get('importe_extra',None)
    @property
    def importe_extra(self):
        return self.__importe_extra
    @property
    def categoria_incentivo(self):
        return self.__categoria_incentivo
    def __str__(self):
        return super().__str__()  + f"\ncategoria_incentivo:{self.__categoria_incentivo}\nimporte extra:{self.__importe_extra}\n"
    def crear_docente(self):
        docenteinv = Docente_Investigador(cuil = str(input("cuil:")), 
                                          apellido = str(input("ape:")), 
                                          nombre = str(input("nom:")), 
                                          sueldo_basico = float(input("sueldo:")),
                                          antiguedad = int(input("antiguedad:")), 
                                          carrera = str(input("carrera:")), 
                                          cargo = str(input("cargo:")),
                                          catedra = str(input("catedra:")),
                                          area_investigacion = str(input("area:")),
                                          tipo_investigacion = str(input("tipo:")),
                                          categoria_incentivo = str(input("categoria_incentivo:")),
                                          importe_extra = float(input("importe extra:")))
                        
        return docenteinv
    def sueldo_DI(self):
        sueldo = super().sueldo_basico 
        sueldo+= self.__importe_extra
        return sueldo