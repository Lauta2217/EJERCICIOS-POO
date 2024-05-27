class Personal:
    __cuil:str
    __apellido:str
    __nombre: str
    __sueldo_basico: float
    __antiguedad:int
    def __init__(self, **kwargs):
        self.__cuil = kwargs.get('cuil',None)
        self.__apellido = kwargs.get('apellido',None)
        self.__nombre = kwargs.get('nombre',None)
        self.__sueldo_basico = kwargs.get('sueldo_basico',None)
        self.__antiguedad = kwargs.get('antiguedad',None)
    @property
    def cuil(self):
        return self.__cuil
    @property
    def apellido(self):
        return self.__apellido
    @property
    def nombre(self):
        return self.__nombre
    @property
    def sueldo_basico(self):
        return self.__sueldo_basico
    @property
    def antiguedad(self):
        return self.__antiguedad
    
    def __gt__(self,other):
        return self.__nombre.lower() > other.nombre.lower()
    def __lt__(self,other):
        return self.__apellido.lower() < other.apellido.lower()

    def __str__(self):
        return f"ape:{self.__apellido}\nnom:{self.__nombre}\ncuil:{self.__cuil}\nsueldo:{self.__sueldo_basico}\nantiguedad:{self.__antiguedad}\n"
