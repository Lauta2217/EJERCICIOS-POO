from personal import Personal
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__carrera = kwargs.get('carrera',None)
        self.__cargo = kwargs.get('cargo',None)
        self.__catedra = kwargs.get('cargo',None)
    @property
    def carrera(self):
        return self.__carrera
    @property
    def cargo(self):
        return self.__cargo
    @property
    def catedra(self):
        return self.__catedra
    def __str__(self):
        return super().__str__() + f"\ncarrera:{self.__carrera}\ncargo:{self.__cargo}\ncatedra:{self.__catedra}\n"
    
    def crear_docente(self):
        docente = Docente(cuil = str(input("cuil:")),
                          apellido = str(input("ape:")),
                          nombre = str(input("nom:")),
                          sueldo_basico = float(input("sueldo:")),
                          antiguedad = int(input("antiguedad:")),
                          carrera = str(input("carrera:")),
                          cargo = str(input("cargo:")),
                          catedra = str(input("catedra:")))
        return docente
    def sueldo_D(self):
        sueldo = super().sueldo_basico 
        sueldo+= (sueldo * (super().antiguedad/100))
        if self.__cargo == "simple":
            sueldo+= sueldo * 0.1
        elif self.__cargo == "semiexclusivo":
            sueldo+= sueldo * 0.2
        elif self.__cargo == "exclusivo":
            sueldo+= sueldo * 0.5
        return sueldo