from abc import ABC, abstractmethod
class interface_coleccion(ABC):
    @abstractmethod
    def insertarelemento(self,elemento,posicion):
        pass
    @abstractmethod
    def agregarelemento(self,elemento):
        pass
    @abstractmethod
    def mostrarelemento(self,elemento):
        pass