from clase_publicaciones import publicaciones

class libro_impreso(publicaciones):
  __nombre_autor: str
  __fecha_edicion: str
  __cant_paginas:int
  def __init__(self,titulo,categoria,preciobase, nombre_autor,fecha_edicion,cant_paginas):
    super().__init__(titulo,categoria,preciobase)
    self.__nombre_autor = nombre_autor
    self.__fecha_edicion= int(fecha_edicion)
    self.__cant_paginas = cant_paginas
  @property
  def nombre_autor(self):
    return self.__nombre_autor
  @property
  def fecha_edicion(self):
    return self.__fecha_edicion
  @property
  def cant_paginas(self):
    return self.__cant_paginas
  def __str__(self):
    return super().__str__() + f"Nombre del autor: {self.__nombre_autor} \nFecha de edición: {self.__fecha_edicion}\nCantidad de páginas: {self.__cant_paginas}\n"
  