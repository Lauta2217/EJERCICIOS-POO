from clase_publicaciones import publicaciones
class Nodo:
    __publicacion: publicaciones # un atributo del tipo publicaciones
    __siguiente: object
    def __init__(self, publicacion):
        self.__publicacion=publicacion
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getpubli(self): #devuelve el objeto
        return self.__publicacion