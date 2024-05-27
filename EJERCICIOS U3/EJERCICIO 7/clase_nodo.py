from personal import Personal
class Nodo:
    __calefactor: Personal
    __siguiente: object
    def __init__(self, personal):
        self.__personal= personal
        self.__siguiente=None
    @property
    def siguiente(self):
        return self.__siguiente    
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    @property
    def getpersonal(self): #devuelve el objeto
        return self.__personal