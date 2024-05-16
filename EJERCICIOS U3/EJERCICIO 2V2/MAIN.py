from gestor_material import *
from gestor_ladrillo import *
if __name__ == '__main__':
  GM = gestor_material()
  GM.cargar_material_desde_csv()
  GM.mostrar()
  GL = gestor_ladrillo()
  GL.cargar_ladrillo_desde_csv(GM)
  GL.mostrar()
  op = int(input("""Ingrese opcion: 
                 1_Detallar costo y caracteristica del material ingresado
                 2_Mostrar para cada ladrillo el costo total de fabricacion del pedido
                 3_Mostrar datos para todos 
                 0_Para finalizar
                 """))
  while op!=0:
    if op == 1:
      idd = int(input("Ingrese idd del ladrillo\n"))
      GL.buscar(idd)
    elif op == 2:
      GL.total(GL)
    elif op == 3:
      GL.mostrar_todo(GL)
    else: print("Numero ingresado no corresponde")
    op = int(input("""Ingrese opcion: 
                 1_Detallar costo y caracteristica del material ingresado
                 2_Mostrar para cada ladrillo el costo total de fabricacion del pedido
                 3_Mostrar datos para todos 
                 0_Para finalizar
                 """))