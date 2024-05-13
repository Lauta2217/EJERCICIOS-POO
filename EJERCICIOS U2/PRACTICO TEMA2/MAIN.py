from clientes import *
from reparaciones import *
from test import *

if __name__ == '__main__':
  GC = gestor_clientes()
  GC.cargar_csv()
  GC.mostrar()

  GR = gestor_reparaciones()
  GR.cargar_csv()
  GR.mostrar()
  
  op = int(input("Ingrese opcion:\n 1_Informar datos de un cliente\n 2_Cambiar estado\n 3_Reparaciones no terminadas\n 4_Persona con mas de un auto\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GC.mostrarrepa(GR)
    elif op == 2:
      GR.repaterminadas(GC)
    elif op == 3:
      GC.repanoterminadas(GR)
    elif op == 4:
      GC.masdeunauto()
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Informar datos de un cliente\n 2_Cambiar estado\n 3_Reparaciones no terminadas\n 4_Persona con mas de un auto\n 0_Para finalizar\n"))
  