from clase_nodo import Nodo
from calefactor_elec import Calefactor_elec
from calefactor_gas import Calefactor_gas
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
            self.__actual=self.__comienzo 
            self.__indice=0 
            raise StopIteration # raise fuerza el lanzamiento de esta excepcion
        else:  #si el indice es distinto al tope
            self.__indice+=1 #aumentamos el indice en 1 por cada iteracion
            dato = self.__actual.getcale() #dato va a tener el objeto de la posicion actual
            self.__actual=self.__actual.siguiente # a la posicion actual le asignamos el siguiente para seguir iterando
            return dato # retornamos nuestro objeto
        
    def agregar_calefactor(self,lista_cale): #insertar por cola
        nodito = None
        for calefactor in lista_cale:
            nodo = Nodo(calefactor) #se crea un nodo con la calefactor
            nodo.setSiguiente(self.__comienzo) #al siguiente nodo se le asigna None
            self.__comienzo= nodo #se asigna el nodo como comienzo
            nodito = nodo
            self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
            print("CALEFACTOR CARGADOO\n")
        self.__actual = nodito
            
    def insertar_pos(self,pos):
        elemento = Calefactor_elec("Philips","PH12442","Argentina",8000,"contado",1,True,1500)
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
        
    def agregar_uno(self,elemento):
        nodo = Nodo(elemento) #se crea un nodo con la calefactor
        nodo.setSiguiente(self.__comienzo) #al siguiente nodo se le asigna None
        self.__comienzo= nodo #se asigna el nodo como comienzo
        self.__actual = nodo
        self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista
        print("CALEFACTOR CARGADOO\n")
        
    def cargar_cale(self,tipo,lista):
        if tipo.lower() == "electrico":
            marca = str(input("Ingrese marca\n"))
            modelo = str(input("Ingrese modelo\n"))
            pais = str(input("Ingrese pais de fabricacion\n"))
            precio = float(input("Ingrese precio de lista\n"))
            pago = str(input("Ingrese tipo de pago contado o cuotas\n"))
            if pago == "contado":
                cuotas = 1
            else:
                cuotas = int(input("Ingrese cuotas. si eligio contado coloque 1\n"))
            prom = str(input("Ingrese promocion: si o no\n"))
            if prom == "si":
                prom = True
            else:
                prom = False
            potencia = int(input("Ingrese potencia maxima\n"))
            elemento = Calefactor_elec(marca,modelo,pais,precio,pago,cuotas,prom,potencia)
            print(elemento)
            lista.agregar_uno(elemento)
            
        elif tipo.lower() == "gas":
            
            marca = str(input("Ingrese marca\n"))
            modelo = str(input("Ingrese modelo\n"))
            pais = str(input("Ingrese pais de fabricacion\n"))
            precio = float(input("Ingrese precio de lista\n"))
            pago = str(input("Ingrese tipo de pago contado o cuotas\n"))
            if pago == "contado":
                cuotas = 1
            else:
                cuotas = int(input("Ingrese cuotas. si eligio contado coloque 1\n"))
            prom = str(input("Ingrese promocion: si o no\n"))
            if prom == "si":
                prom = True
            else:
                prom = False
            matricula = str(input("Ingrese matricula\n"))
            calo = int(input("Ingrese calorias\n"))
            elemento = Calefactor_gas(marca,modelo,pais,precio,pago,cuotas,prom,matricula,calo)
            lista = Lista()
            lista.agregar_uno(elemento)
        else:
            raise TypeError('El tipo ingresado es incorrecto.')
    def informar_pos(self,pos):
        if 0 < pos <= self.__tope:
            aux = self.__actual
            for _ in range(pos-1):
                aux = aux.siguiente
            if isinstance(aux.getcale(),Calefactor_elec):
                print(f"El calefactor de la posicion:{pos} es del tipo electrico")
            elif isinstance(aux.getcale(),Calefactor_gas):
                print(f"El calefactor de la posicion:{pos} es del tipo gas")
        else:
            raise IndexError('La posicion indicada se encuentra fuera de rango.')
    def cale_gas_min(self,lista):
        minn = 99999
        for cale in lista:
            if isinstance(cale,Calefactor_gas):
                if cale.calcular_precio() < minn:
                    minn = cale.calcular_precio()
                    aux = cale  
            else:
                pass
        print(f" Datos del calefactor de gas de menor precio: \nmarca:{aux.marca}\nmodelo:{aux.modelo}\ncalorias:{aux.calorias}")      
    def buscar_marca(self,marca,lista):
        band = False
        for cale in lista:
            if cale.marca.lower() == marca.lower() and isinstance(cale,Calefactor_elec):
                print(f"modelo:{cale.modelo}\npotencia:{cale.potencia_max}\nprecio de lista:{cale.precio_de_lista}\n")
                band = True
        if not band:
            print("Marca ingresada incorrecta o no hay calefactores electricos con esa marca\n")
    def buscar_promo(self,lista):
        for cale in lista:
            if cale.promocion:
                print(f"Marca:{cale.marca}\nModelo:{cale.modelo}\nPais de fabricacion:{cale.pais_de_fabricacion}\nImporte de venta:{cale.calcular_precio()}\n")
                
                
                
           
        
    