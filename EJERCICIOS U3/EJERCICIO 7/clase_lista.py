from clase_nodo import Nodo
from docente import Docente
from personal_apoyo import Personal_apoyo
from investigador import Investigador
from personal import Personal
from docente_investigador import Docente_Investigador
from interface import interface_coleccion
from zope.interface import implementer
@implementer(interface_coleccion)
class Lista():
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
            self.__actual=self.__comienzo 
            self.__indice=0 
            raise StopIteration # raise fuerza el lanzamiento de esta excepcion
        else:  #si el indice es distinto al tope
            self.__indice+=1 #aumentamos el indice en 1 por cada iteracion
            dato = self.__actual.getpersonal #dato va a tener el objeto de la posicion actual
            self.__actual=self.__actual.siguiente # a la posicion actual le asignamos el siguiente para seguir iterando
            return dato # retornamos nuestro objeto
        
    def agregarelemento_lista(self,lista_personal): #insertar por cola
        nodito = None
        for personal in lista_personal:
            nodo = Nodo(personal) #se crea un nodo con la calefactor
            nodo.setSiguiente(self.__comienzo) #al siguiente nodo se le asigna None
            self.__comienzo= nodo #se asigna el nodo como comienzo
            self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
            nodito = nodo
            print("PERSONAL CARGADOO\n")
        self.__actual = nodito
        
    def insertarelemento(self,elemento,pos):
        nodo = Nodo(elemento)
        if self.__comienzo == None or pos == 1:
            nodo.setSiguiente(self.__comienzo)
            self.__actual = nodo
            self.__comienzo = nodo
                
        elif 0 < pos <= self.__tope:
            aux = self.__actual
            for _ in range(pos-2):
                aux = aux.siguiente
            nodo.setSiguiente(aux.siguiente)
            aux.setSiguiente(nodo)     
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
        self.__tope += 1
        for cale in self:
            print(f"{cale}")
            print("------------------\n")
    def agregarelemento(self,elemento): #insertar por cola
        nodo = Nodo(elemento) #se crea un nodo con la calefactor
        nodo.setSiguiente(self.__comienzo) #al siguiente nodo se le asigna None
        self.__comienzo= nodo #se asigna el nodo como comienzo
        self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
        nodito = nodo
        print("PERSONAL CARGADOO\n")
        self.__actual = nodito
    def mostrarelemento(self,pos):
        if 0 < pos <= self.__tope:
            aux = self.__actual
            for _ in range(pos-1):
                aux = aux.siguiente
            if isinstance(aux.getpersonal,Personal_apoyo):
                print(f"El personal de la posicion:{pos} es del tipo personal apoyo")
            elif isinstance(aux.getpersonal,Docente):
                print(f"El personal de la posicion:{pos} es del tipo docente")
            elif isinstance(aux.getpersonal,Investigador):
                print(f"El personal de la posicion:{pos} es del tipo investigador")
            elif isinstance(aux.getpersonal,Docente_Investigador):
                print(f"El personal de la posicion:{pos} es del tipo docente investigador")
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
        
    def agentes_especializados(self,carrera):
        lista_a = []
        for agente in self:
            if isinstance(agente,Docente_Investigador):
                if agente.carrera.lower() == carrera.lower():
                    lista_a.append(agente)
        lista_a = sorted(lista_a)
        for agente in lista_a:
            print(agente)
            
    def agentes_area(self,area):
        cont1=0
        cont2=0
        for agente in self:
                if isinstance(agente,Docente_Investigador):
                    if area.lower() == agente.area_investigacion.lower():
                        cont1+=1
                elif isinstance(agente,Investigador):
                    if area.lower() == agente.area_investigacion.lower():
                        cont2+=1
        if cont1 != 0 or cont2 !=0:
            print(f"Cantidad de docentes investigadores del area {area} son: {cont1} y investigadores son: {cont2}\n")
        else:
            print("No hay docentes investigadores ni investigadores en ese area. o el area ingresada es incorrecta\n") 
    def listado_agentes(self):
        lista = []
        for agente in self:
            lista.append(agente)

        lista = sorted(lista)
        
        for agente in lista:
            if isinstance(agente,Docente_Investigador):
                print(f"nombre y apellido: {agente.nombre} {agente.apellido}\nTipo: Docente_Investigador\nSueldo:{agente.sueldo_DI()}\n")
            elif isinstance(agente,Investigador):
                    print(f"nombre y apellido: {agente.nombre} {agente.apellido}\nTipo: Investigador\nSueldo:{agente.sueldo_I()}\n")
            elif isinstance(agente,Docente):
                print(f"nombre y apellido: {agente.nombre} {agente.apellido}\nTipo: Docente\nSueldo:{agente.sueldo_D()}\n")
            elif isinstance(agente,Personal_apoyo):
                print(f"nombre y apellido: {agente.nombre} {agente.apellido}\nTipo: Personal apoyo\nSueldo:{agente.sueldo_PA()}\n")
    
    def solicitar_dinero(self,cate):
        dinero = 0
        for agente in self:
            if isinstance(agente,Docente_Investigador):
                if agente.categoria_incentivo.lower() == cate.lower():
                    print(f"Nombre y apellido: {agente.nombre} {agente.apellido}\nImporte extra: {agente.importe_extra}\n")
                    dinero+= agente.importe_extra
        if dinero !=0:
            print(f"Cantidad de dinero que se le debe solicitar al ministerio es de: {dinero}")
        else:
            print("No hay docentes investigadores en ese area\n")
            