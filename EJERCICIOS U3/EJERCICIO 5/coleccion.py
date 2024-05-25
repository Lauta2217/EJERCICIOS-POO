
from Nodo import Nodo
from interface import interface_coleccion
class  lista_enlazada(interface_coleccion):
    __comienzo: int
    __actual: int
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo =  None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope: #si el indice es igual al tope, entonces se detiene la iteracion
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration # raise fuerza el lanzamiento de esta excepcion
        elif self.__comienzo==None: #si la lista esta vacia, entonces se detiene la iteracion
            self.__actual=self.__comienzo #se asigna el actual como el comienzo
            self.__indice=0 #se asigna el indice como 0 
            raise StopIteration
        else:  #si el indice es distinto al tope
            self.__indice+=1 #aumentamos el indice en 1 por cada iteracion
            dato = self.__actual.dato#dato va a tener el objeto de la posicion actual
            self.__actual=self.__actual.siguiente # a la posicion actual le asignamos el siguiente para seguir iterando
            return dato # retornamos nuestro objeto
    
    def agregarelemento(self, elemento):
        nodo = Nodo(elemento) #se crea un nodo con la publicacion
        print(f"{type(nodo)}")
        nodo.setsiguiente(self.__comienzo) #al siguiente nodo se le asigna None
        self.__comienzo=nodo #se asigna el nodo como comienzo
        self.__actual=nodo #se asigna el nodo como actual
        self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
    
    def insertarelemento(self, elemento, pos):
        nodo = Nodo(elemento)
        if self.__comienzo == None or pos == 1:
            nodo.setsiguiente(self.__comienzo)
            self.__actual = nodo
            self.__comienzo = nodo
                
        elif 0 < pos <= self.__tope:
            aux = self.__comienzo
            for _ in range(pos-2):
                aux = aux.siguiente
            nodo.setsiguiente(aux.siguiente)
            aux.setsiguiente(nodo)      
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
        self.__tope += 1
    
    def mostrarelemento(self,pos):
        if pos < 1 or pos > self.__tope:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
        elif 0 < pos <= self.__tope:
            aux = self.__comienzo
            for _ in range(pos-1):
                aux = aux.siguiente
            print(f"Datos en la posicion {pos}: {aux}")
        

           


            
            
        
        
    
    