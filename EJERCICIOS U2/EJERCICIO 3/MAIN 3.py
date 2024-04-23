import numpy as np 
class gestor:
  def __init__(self):
    self.__matriz = np.zeros((5,7))
    
  def mostrar(self):
    print(self.__matriz[0][1])
    
  def cargarDatos(self):
    sucursal = int(input("Ingrese sucursal\n"))
    dia = int(input("Ingrese dia de la semana\n"))
    self.__matriz[sucursal-1][dia-1] += float(input("Ingrese importe de factura del dían\n"))
  
  def calcularFacturacion(self):
    sucu = int(input("Ingrese sucursal\n"))
    total = 0
    for importe in self.__matriz[sucu-1]: #mariano lo optimizó (es trabajar sobre la lista directamente sin usar i)
      total += importe
    print(f"Total facturado {total}\n")
    
  def sucursalpiola(self):
    dia = int(input("Dia de la semana a evaluar\n"))
    indicemax = np.argmax(self.__matriz[:,dia-1],axis=0) # axis = 0 evalua horizontalemente donde esten los : y axis = 1 evalua veticalmente
    print(f"la sucursal que mas vendio fue: {indicemax + 1}")
    
  def sucursalnopiola(self):
    mi = 999999999999
    i = 0
    acum = 0
    for i in range(5):
      for importe in self.__matriz[i]:
        acum += importe
      if mi > acum:
        mi = acum
        j = i
      acum = 0
    print(f"La sucursal que menos vendió fue {j+1}")
    
  def total(self):
    acum = 0
    for i in range(5):
        acum += np.sum(self.__matriz[i])
    print(f"El total de todas las sucursales es: {acum}")
    
if __name__=='__main__':
   gestor = gestor()
   band = True
   op = int(input("Ingrese opcion:\n 1_Cargar facturacion\n 2_Calcular facturacion total para una sucursal\n 3_Ingresar un día y obtener sucursal que más facturo\n 4_Calcular sucursal con menos facturacion durante la semana\n 5_Calcular total de todas las sucursales 0_Para finalizar\n"))
   while op!=0:
    if op == 1:
      gestor.cargarDatos()
    elif op == 2:
      gestor.calcularFacturacion()
    elif op == 3:
     gestor.sucursalpiola()
    elif op == 4:
     gestor.sucursalnopiola()  
    elif op == 5:
      gestor.total()
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Cargar facturacion\n 2_Calcular facturacion total para una sucursal\n 3_Ingresar un día y obtener sucursal que más facturo\n 4_Calcular sucursal con menos facturacion durante la semana\n 5_Calcular total de todas las sucursales 0_Para finalizar\n"))
"""
1
1
100
2
1
1000
3
1
10
4
1
5
5
1
1
4
1
"""
