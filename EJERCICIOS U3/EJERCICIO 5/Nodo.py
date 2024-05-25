class Nodo:
    __dato: int # un atributo del tipo datoes
    __siguiente: int
    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
    
    @property
    def siguiente(self):
        return self.__siguiente
    def setsiguiente(self,dato):
      self.__siguiente = dato

    @property
    def dato(self):
        return self.__dato
    def setdato(self, dato):
        self.__dato=dato
        
    def __str__(self):
      return f" numero: {self.__dato}"