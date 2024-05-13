from gestor_empleados import *
from gestor_matricula import *
from gestor_programacapacitacion import *
if __name__ == '__main__':
  
  GE = gestor_empleados()
  GE.cargar_empleados_desde_csv()
  GE.ordenar()
  
  GP = gestor_programacapacitacion()
  GP.cargar_programas_desde_csv()
  GP.ordenar()
  
  GM = gestor_matricula()
  GM.cargar_matriculas_desde_csv(GE,GP)
  
  op = int(input("""Ingrese opcion: 
                 1_Informar programas registrados del empleado
                 2_Mostrar empleados registrados en el programa
                 3_Mostrar empleados sin programa
                 0_Para finalizar
                 """))
  while op!=0:
    if op == 1:
      idd = str(input("Ingrese idd del empleado\n"))
      GE.buscar_programas_del_empleado(idd)
    elif op == 2:
      programa = str(input("Ingrese nombre de programa\n"))
      GP.buscar_empleados_en_programa(programa)
    elif op == 3:
      GE.informar_empleados()
    else: print("Numero ingresado no corresponde")
    op = int(input("""Ingrese opcion: 
                 1_Informar programas registrados del empleado
                 2_Mostrar empleados registrados en el programa
                 3_Mostrar empleados sin programa
                 0_Para finalizar
                 """))
  

