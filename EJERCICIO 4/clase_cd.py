from clase_publicaciones import publicaciones
class CD(publicaciones):
    __tiempo: int
    __nombre_narrador: str
    def __init__(self,titulo,categoria,preciobase, nombre_narrador,tiempo):
        super().__init__(titulo,categoria,preciobase)
        self.__nombre_narrador = nombre_narrador
        self.__tiempo = tiempo
    @property
    def tiempo(self):
        return self.__tiempo
    @property
    def nombre_narrador(self):
        return self.__nombre_narrador
    def __str__(self):
        return super().__str__() + f"Tiempo: {self.__tiempo}\nNarrador:  {self.__nombre_narrador}"
    