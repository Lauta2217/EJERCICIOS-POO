from clase_libro_impreso import *
class gestor_libro_impreso:
  def crear_libro_impreso(self):
    print("creando libro")
    libro = libro_impreso(str(input("ingrese titulo ")),str(input("ingrese categoria ")),int(input("ingrese precio base ")),str(input("ingrese nombre del autor ")),str(input("ingrese fecha de edición ")),int(input("ingrese cantidad de paginas ")))
    return libro