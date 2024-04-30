import csv
class Transacciones():
  def __init__(self,CVU,num_transaccion,importe,tipo_transaccion):
    self.__CVU = CVU
    self.__num_transaccion = num_transaccion
    self.__importe = importe
    self.__tipo_transaccion = tipo_transaccion
    
  def __str__(self):
    return self.__CVU
  
class gestortransacciones():
  def __init__(self, lista = []):
    self.__lista = lista
    
  def cargar_transacciones_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/EJERCICIO 6/transaccionesBilletera.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        transacciones = Transacciones(*fila)
        self.__lista.append(transacciones)
    print("billeteras cargadas\n")
    
  def mostrar(self):
    for transa in self.__lista:
      print(transa)
      
  def actualizar(self,saldo,cvu):
    importe = 0
    for transa in self.__lista:
      if transa._Transacciones__CVU == cvu:
        importe += float(transa._Transacciones__importe)
    return float(saldo + importe)