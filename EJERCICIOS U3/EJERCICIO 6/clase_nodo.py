from calefactor import Calefactor
class Nodo:
    __calefactor: Calefactor # un atributo del tipo calefactores
    __siguiente: object
    def __init__(self, calefactor):
        self.__calefactor=calefactor
        self.__siguiente=None
    @property
    def siguiente(self):
        return self.__siguiente    
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
  
    def getcale(self): #devuelve el objeto
        return self.__calefactor