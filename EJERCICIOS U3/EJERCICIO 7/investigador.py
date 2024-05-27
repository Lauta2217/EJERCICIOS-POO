from personal import Personal
class Investigador(Personal):
    __area_investigacion: str
    __tipo_investigacion: str
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__carrera = kwargs.get('carrera',None)
        self.__cargo = kwargs.get('cargo',None)
        self.__catedra = kwargs.get('cargo',None)
        self.__area_investigacion = kwargs.get('area_investigacion',None)
        self.__tipo_investigacion = kwargs.get('tipo_investigacion',None)
    @property
    def area_investigacion(self):
        return self.__area_investigacion
    @property
    def tipo_investigacion(self):
        return self.__tipo_investigacion
    def __str__(self):
        return super().__str__() + f" area:{self.__area_investigacion} tipo:{self.__tipo_investigacion} "
    def crear_docente(self):
        inv = Investigador(cuil = str(input("cuil:")),
                          apellido = str(input("ape:")),
                          nombre = str(input("nom:")),
                          sueldo_basico = float(input("sueldo:")),
                          antiguedad = int(input("antiguedad:")),
                          area_investigacion = str(input("area:")),
                          tipo_investigacion = str(input("tipo:"))
                          )
        return inv
    def sueldo_I(self):
        sueldo = super().sueldo_basico 
        sueldo+= (sueldo * (super().antiguedad/100))
        return sueldo
    