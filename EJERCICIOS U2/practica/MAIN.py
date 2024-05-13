from gestor_cliente import *
from gestor_movimiento import *
if __name__=='__main__':
  GC = gestor_cliente() 
  GC.cargar_cliente_desde_csv()
  GC.mostrar()
  GM = gestor_movimiento() 
  GM.cargar_movimiento_desde_csv()
  GM.mostrar()
  #menu:
  op = int(input("Ingrese opcion:\n 1_Actualizar saldo\n 2_Informar si no tuvo movimientos en abril\n 3_Ordenar\n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GC.actualizar_saldo(GM)
    elif op == 2:
      GC.movi_abril(GM)
    elif op == 3:
      GM.ordenar()
      GM.mostrar()
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Actualizar saldo\n 2_Informar si tuvo movimientos en abril\n 3_Ordenar\n 0_Para finalizar\n"))