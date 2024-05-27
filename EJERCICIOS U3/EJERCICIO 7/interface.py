from zope.interface import Interface
class interface_coleccion(Interface):
    def insertarelemento(self,elemento,posicion):
        pass
    def agregarelemento(self,elemento):
        pass
    def mostrarelemento(self,pos):
        pass
    