from clase_nodo import Nodo
from clase_cd import CD
from clase_libro_impreso import libro_impreso
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope = 0# hace referencia a la cantidad de elementos en la lista, como su nombre lo dice es un tope a la hora de iterar
        self.__indice = 0 #hace referencia a la posicion en la lista
    def __iter__(self):
        return self #retorna el iterador de un objeto, es decir el actual
    def __next__(self):
        if self.__indice==self.__tope: #si el indice es igual al tope, entonces se detiene la iteracion
            raise StopIteration # raise fuerza el lanzamiento de esta excepcion
        elif self.__comienzo==None: #si la lista esta vacia, entonces se detiene la iteracion
            self.__actual=self.__comienzo #se asigna el actual como el comienzo
            self.__indice=0 #se asigna el indice como 0 
            raise StopIteration
        else:  #si el indice es distinto al tope
            self.__indice+=1 #aumentamos el indice en 1 por cada iteracion
            dato = self.__actual.getpubli() #dato va a tener el objeto de la posicion actual
            self.__actual=self.__actual.getSiguiente() # a la posicion actual le asignamos el siguiente para seguir iterando
            return dato # retornamos nuestro objeto
    def agregarpublicacion(self,publicacion):
        nodo = Nodo(publicacion) #se crea un nodo con la publicacion
        nodo.setSiguiente(self.__comienzo) #al siguiente nodo se le asigna None
        self.__comienzo=nodo #se asigna el nodo como comienzo
        self.__actual=nodo #se asigna el nodo como actual
        self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
    def buscar(self,pos):
        if pos < 0 or pos > self.__tope: # se evalua si la posicion ingresada es menor a 0 o la posicion es mayor a la cantidad de le elementos en la lista
            return None # si no se cumple la condicion, se retorna None
        else:
            indice = 0 #se incializa el indice para iterar en 0
            actual = self.__actual #se asigna el actual
            while actual is not None and indice < pos: # mientras el actual sea distinto de None y el indice sea menor a la posicion ingresada
                actual = actual.getSiguiente() #a actual le asignamos siguiente
                indice += 1 #aumentamos el indice en 1 
            if indice == pos and actual is not None: #una vez que se llega a la posicion deseada se retorna el objeto de esta
                return actual.getpubli() 
    def contar(self):
        actual = self.__actual #se asigna el actual
        contcd = 0
        contl = 0
        indice = 0 #se incializa el indice para iterar en 0
        while actual is not None and indice < self.__tope:  # mientras el actual sea distinto de None y el indice sea menor al tope es decir que hayan elementos
                if isinstance(actual.getpubli(),CD): #se evalua si el objeto actual es del tipo CD
                    contcd+=1 # en caso de serlo aumenta en 1
                elif isinstance(actual.getpubli(),libro_impreso): #se evalua si el objeto actual es del tipo libro impreso
                    contl+=1 # en caso de serlo aumenta en 1
                actual = actual.getSiguiente() # se asigna el siguiente elemento para seguir iterando
                indice += 1 # se aumenta el indice en 1 por iteracion
                
        if contcd !=0:
            print(f"Cantidad de publicaciones del tipo CD: {contcd}\n")
        else:
            print("No hay publicaciones tipo CD\n")
        
        if contl !=0:
            print(f"Cantidad de publicaciones del tipo libro impreso: {contl}\n")
        else:
            print("No hay publicaciones tipo libro impreso\n")
            
    def determinar_precio(self):
        actual = self.__actual  #se asigna el actual
        indice = 0 #se incializa el indice para iterar en 0
        while actual is not None and indice < self.__tope:  # mientras el actual sea distinto de None y el indice sea menor al tope es decir que hayan elementos
                publi = actual.getpubli() # se asigna la publicacion actual a una variable
                if isinstance(publi,CD): # se determina si es de la clase CD
                    publi.setpreciobase(publi.getpreciobase()*1.1) # en caso de serlo se determina el precio con la regla de negocio
                elif isinstance(publi,libro_impreso): # se determina si es de la clase libro impreso
                    publi.setpreciobase(float(publi.getpreciobase()-(2024-publi.fecha_edicion))) # en caso de serlo se determina el precio con la regla de negocio
                actual = actual.getSiguiente() # se asigna el siguiente elemento para seguir iterando
                indice += 1 # se aumenta el indice en 1 por iteracion
        
        
                    

        
        
    