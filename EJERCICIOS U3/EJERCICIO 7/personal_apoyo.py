from personal import Personal
class Personal_apoyo(Personal):
    __categoria: str
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__categoria = kwargs.get('categoria',None)
    @property
    def categoria(self):
        return self.__categoria
    def __str__(self):
        return super().__str__() + f"\ncategoria:{self.__categoria}"
    def crear_personal_apoyo(self):
        pa = Personal_apoyo(cuil = str(input("cuil:")),
                          apellido = str(input("ape:")),
                          nombre = str(input("nom:")),
                          sueldo_basico = float(input("sueldo:")),
                          antiguedad = int(input("antiguedad:")),
                          categoria = str(input("categoria:"))
                            )
        return pa
    def sueldo_PA(self):
        sueldo = super().sueldo_basico  
        sueldo+= (sueldo * (super().antiguedad/100))
        if self.__categoria in range(1,10):
            sueldo+= sueldo * 0.1
        elif self.__categoria in range(11,20):
            sueldo+= sueldo * 0.2
        elif self.__categoria in range(21,22):
            sueldo+= sueldo * 0.3
        return sueldo