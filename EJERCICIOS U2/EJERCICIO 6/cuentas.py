import numpy as np
import csv
from transacciones import *

class Cuenta():
  porc_anual = 68
  def __init__(self,ape,nom,DNI,tel,saldo,CVU):
    self.__ape = ape
    self.__nom = nom
    self.__DNI = DNI
    self.__tel = tel
    self.__saldo = float(saldo)
    self.__CVU = CVU
  @classmethod
  def modificar_por_anual(cls):
    cls.porc_anual = float(input("Ingrese valor\n"))  
    print(cls.porc_anual)
      
  def __str__(self):
    return f"APELLIDO: {self.__ape}\n NOMBRE: {self.__nom}\n CVU: {self.__CVU}\n SALDO:{self.__saldo}\n"
    
class gestorcuenta():
  def __init__(self):
    self.__lista = np.array([],dtype='object')
    
  def cargar_cuentas(self):
    with open("UNIDAD 2/EJERCICIOS U2/EJERCICIO 6/cuentasBilletera.csv",newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        cuenta = Cuenta(*fila)
        self.__lista = np.append(self.__lista,cuenta)
        
  def mostrar(self):
    for cuenta in self.__lista:
      print(cuenta)
  
  def actulizarsaldo_DNI(self,GT):
    dni = input("Ingrese DNI:\n")
    for cuenta in self.__lista:
      if cuenta._Cuenta__DNI == dni:
        print(f"SALDO SIN ACTUALIZAR {cuenta._Cuenta__saldo}\n")
        cuenta._Cuenta__saldo = GT.actualizar(cuenta._Cuenta__saldo,cuenta._Cuenta__CVU) 
        print(f"SALDO ACTUALIZADO: {cuenta._Cuenta__saldo}\n")  
      
  def aumentarsaldo(self):
    for cuenta in self.__lista:
      cuenta._Cuenta__saldo = cuenta._Cuenta__saldo + (cuenta._Cuenta__saldo * (Cuenta.porc_anual / 365))/100 #CALCULA EL RENDIMIENTO DIARIO
      print(round(cuenta._Cuenta__saldo,3))
      
  def actulizarsaldo_CVU(self,GT):
    cvu = input("Ingrese cvu:\n")
    for cuenta in self.__lista:
      if cuenta._Cuenta__CVU == cvu:
        print(f"SALDO SIN ACTUALIZAR {cuenta._Cuenta__saldo}\n")
        cuenta._Cuenta__saldo = GT.actualizar(cuenta._Cuenta__saldo,cuenta._Cuenta__CVU) 
        print(f"SALDO ACTUALIZADO: {cuenta._Cuenta__saldo}\n")     
        
  def cargar_csv(self):
    nom = "UNIDAD 2/EJERCICIOS U2/EJERCICIO 6/cuentasactualizadas.csv"
    with open(nom,'w',newline='') as archivo_csv:
      writer = csv.writer(archivo_csv)
      for cuenta in self.__lista:
        fila = [cuenta._Cuenta__ape,cuenta._Cuenta__nom,cuenta._Cuenta__DNI,round(cuenta._Cuenta__saldo,2),cuenta._Cuenta__CVU]
        writer.writerow(fila)
  