import csv
import os
class Moto():
  def __init__(self,patente,marca,nombreyapellido,km):
    self.__patente = patente
    self.__marca = marca
    self.__nombreyapellido = nombreyapellido
    self.__km = km
  def __str__(self):
    return self.__marca
  
class gestorMoto():
  def __init__(self,lista = []):
    self.__lista = lista
  def cargar_motos_desde_csv(self):
    os.system("cls")
    with open("UNIDAD 2/EJERCICIOS/EJERCICIO 4/datosMotos.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        moto = Moto(*fila)
        self.__lista.append(moto)
    print("Motos cargados correctamente")
          
  def mostrar(self):
    os.system("cls")
    for moto in self.__lista:
      print(moto)
  
  def verificarpatente(self):
    while True:
        patente = input("Ingrese patente del pedido\n").strip().lower()
        for moto in self.__lista:
            if patente == moto._Moto__patente.strip().lower(): #para poder acceder a los datos es la variable._clasequecorresponde__variabledelaclase
                return patente.upper()
        print("Patente no encontrada, ingrese otra nuevamente\n")
        
  def tiempo_real_por_conductor(self,GP):
    os.system("cls")
    patent = self.verificarpatente()
    tr = 0
    for moto in self.__lista:
      if moto._Moto__patente.strip().lower() == patent.strip().lower():
        print("estoy en tiuempo real por conductor")
        tr = GP.calcular_pedido(patent)
    print(f"El tiempo promedio real es: {tr}\n")
  def calcular_comisiones(self,GP):
    os.system("cls")
    for moto in self.__lista:
      print(f"Patente de la moto:{moto._Moto__patente}\n")
      print(f"Conductor: {moto._Moto__nombreyapellido}")
      GP.Comisiones(moto._Moto__patente)