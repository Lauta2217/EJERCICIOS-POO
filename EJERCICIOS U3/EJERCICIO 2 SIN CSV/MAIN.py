from gestor_material import *
from gestor_ladrillo import *

if __name__ == '__main__':
  """mate_refrec = mate_refrec("caca","duro",2,100)
  print(mate_refrec)
  
  ladri1 = ladrillo(20,10,1,1,12,100,None)
  print (ladri1)
  ladri2 = ladrillo(20,10,1,1,12,100,20,None)
  print(ladri2)"""
  GM = gestor_material()
  GM.cargar_material_desde_csv()
  GM.mostrar()
  GL = gestor_ladrillo()
  GL.crear_ladrillo(GM)
  GL.mostrar()
  GL.buscar(idd = int(input("Ingrese id del ladrillo a consultar\n")))
  GL.total(GL)
  GL.mostrar_todo(GL)
  """
1
1
1
s
Arcilla refractaria
3
2
3
n
0
2
  """