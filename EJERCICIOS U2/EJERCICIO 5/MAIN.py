from equipos import *
from fechas import *
if __name__ == '__main__':
  op = int(input("Ingrese opcion:\n 1_Cargar equipos\n 2_Cargar fechas\n 3_Obtener listado de un equipo\n 4_Agregar tiempo real a pedido\n 5_Tiempo real por conductor\n 6_Calcular comisiones\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GE = gestorequipos()
      GE.cargar_equipos_desde_csv()
      GE.mostrar()
    elif op == 2:
      GF = gestorfechas()
      GF.cargar_fechas_desde_csv()
      GF.mostrar()
    elif op == 3:
      GE.buscar(GF)
    elif op == 4:
      pass
    elif op == 5:
      pass
    elif op == 6:
      pass
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Cargar equipos\n 2_Cargar fechas\n 3_Obtener listado de un equipo\n 4_Agregar tiempo real a pedido\n 5_Tiempo real por conductor\n 6_Calcular comisiones\n 0_Para finalizar\n"))
  


