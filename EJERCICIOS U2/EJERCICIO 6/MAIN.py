import csv
from cuentas import *
from transacciones import *

if __name__ =='__main__':
  GC = gestorcuenta()
  GC.cargar_cuentas()
  GC.mostrar()
  
  GT = gestortransacciones()
  GT.cargar_transacciones_csv()
  GT.mostrar()
  
  op = int(input("Ingrese opcion:\n 1_Informar datos de un cliente\n 2_Modificar porcentaje anual de rendimiento\n 3_Actualizar saldo respecto a porcentaje anual de rendiemiento\n 4_Actualizar saldo de un cvu por transacciones\n 5_Cargar cuentas actualizadas a csv\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GC.actulizarsaldo_DNI(GT)
      GC.mostrar()
    elif op == 2:
      Cuenta.modificar_por_anual()
    elif op == 3:
      GC.aumentarsaldo()
    elif op == 4:
      GC.actulizarsaldo_CVU(GT)
    elif op == 5:
      GC.cargar_csv()
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Informar datos de un cliente\n 2_Modificar porcentaje anual de rendimiento\n 3_Actualizar saldo respecto a porcentaje anual de rendiemiento\n 4_Actualizar saldo de un cvu por transacciones\n 5_Cargar cuentas actualizadas a csv\n 0_Para finalizar\n"))
  
  
  