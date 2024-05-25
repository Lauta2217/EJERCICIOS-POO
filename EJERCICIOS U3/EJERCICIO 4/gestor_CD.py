from clase_cd import *
class gestor_CD:
  def crear_cd(self):
    print("Creando CD")
    cdd = CD(str(input("Titulo: ")),str(input("Categoria: ")),int(input("Precio base: ")),str(input("Nombre del narrador: ")),int(input("Tiempo: ")))
    return cdd
    
  