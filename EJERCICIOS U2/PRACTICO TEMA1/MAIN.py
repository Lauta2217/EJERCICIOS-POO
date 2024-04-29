from clase_evaluacion import *
from clase_patinadores import *
from gestorEva import *
from gestorPati import *
"""Listar los datos de los patinadores que participaron en estilo libre y en escuela.
  respecto a este inciso, entendí que deberia de mostrar a las personas que participen
  en ambos estilos, pero yo lo trabaje como que participan en uno solo. Así que en esa funcion
  directamente los mostré a todos los patinadores
"""

if __name__=='__main__':
  GE = gestor_evaluaciones() #asigno la clase
  GE.cargar_evaluaciones_desde_csv()
  GE.mostrar() 
  GP = gestor_patinadores() #asigno la clase
  GP.cargar_patinadores_desde_csv()
  GP.mostrar()
  #menu:
  op = int(input("Ingrese opcion:\n 1_Buscar patinador\n 2_Buscar patiandor con mayor puntaje\n 3_Obtener listado de todos los patinadores\n 4_Buscar un patinador por DNI y Estilo\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GE.mostrarestilo(GP)
    elif op == 2:
      GE.mayorpuntaje(GP)
    elif op == 3:
      GE.listartodo(GP)
    elif op == 4:
      GE.buscar_DE() #busco por dni y estilo
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Buscar patinador\n 2_Buscar patiandor con mayor puntaje\n 3_Obtener listado de todos los patinadores\n 4_Buscar un patinador por DNI y Estilo\n 0_Para finalizar\n"))