class publicaciones:
    __titulo: str
    __categoria: str
    __preciobase: float
    def __init__(self, titulo, categoria, preciobase):
        self.__titulo = str(titulo)
        self.__categoria = str(categoria)
        self.__preciobase = float(preciobase)
     
    def gettitulo(self):
        return self.__titulo
    def getcategoria(self):
        return self.__categoria
    def getpreciobase(self):
        return self.__preciobase
       
    def setpreciobase(self, preciobase):
        self.__preciobase = preciobase
    
    def __str__(self):
        return f"Titulo: {self.__titulo}\nCategoria: {self.__categoria}\nPrecio base: {self.__preciobase}\n"
    
  