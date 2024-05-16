import csv
from tkinter import *
class Pedido():
  def __init__(self,patente,identificador,comida,tiempo_Estimado,tiempo_Real,precio):
    self.__patente = str(patente)
    self.__identificador = int(identificador)
    self.__comida = str(comida)
    self.__tiempo_Estimado = int(tiempo_Estimado)
    self.__tiempo_Real = int(tiempo_Real)
    self.__precio = float(precio)
  def __str__(self):
    return f"Patente: {self.__patente}\nID: {self.__identificador}\nComida: {self.__comida}\nTiempo Estimado: {self.__tiempo_Estimado}\nTiempo Real: {self.__tiempo_Real}\nPrecio: {self.__precio}\n"
  def __gt__(self, other):
        return self.__patente > other._Pedido__patente
  def __lt__(self, other):
        return self.__patente < other._Pedido__patente
  @property
  def patente(self):
    return self.__patente
  @property
  def identificador(self):
    return self.__identificador
  @property
  def comida(self):
    return self.__comida
  @property
  def tiempo_Estimado(self):
    return self.__tiempo_Estimado
  @property
  def tiempo_Real (self):
    return self.__tiempo_Real
  @property
  def precio(self):
    return float(self.__precio)
  def settiempo_Real(self,otro):
    self.__tiempo_Real = otro
  
class Moto():
  def __init__(self,patente,marca,nombreyapellido,km):
    self.__patente = patente
    self.__marca = marca
    self.__nombreyapellido = nombreyapellido
    self.__km = km
  def __str__(self):
    return self.__marca
  @property
  def patente(self):
    return self.__patente
  @property
  def marca(self):
    return self.__marca
  @property
  def nombreyapellido(self):
    return self.__nombreyapellido
  @property
  def km(self):
    return self.__km
class gestor():
  def __init__(self,frame,lista_P = [],lista_M=[]):
    self.__lista_P = lista_P
    self.__lista_M = lista_M
    self.__frame = frame
  def cargar_pedidos_desde_csv(self):
    with open("pruebas/tkinter/EJERCICIO3TKINTER/datosPedidos.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv,delimiter=';')
      for fila in reader:
        pedido = Pedido(*fila)
        self.__lista_P.append(pedido)
    Label(self.__frame,text="pedidos cargados correctamente").pack()
    
  def cargar_motos_desde_csv(self):
    with open("pruebas/tkinter/EJERCICIO3TKINTER/datosMotos.csv", newline='') as archivo_csv:
      reader = csv.reader(archivo_csv)
      for fila in reader:
        moto = Moto(*fila)
        self.__lista_M.append(moto)
    Label(self.__frame,text="Motos cargados correctamente").pack()
    
  def mostrar_P(self):
    for pedido in self.__lista_P:
      Label(self.__frame,text="\t-------------------------------------------------------\n").pack()
      Label(self.__frame,text=f"{pedido}").pack()
      
  def mostrar_M(self):
    for moto in self.__lista_M:
      Label(self.__frame,text=f"{moto}").pack()
  
  def asignar_pedido_a_moto(self):
    
    Label(self.__frame,text="INGRESE patente").pack()
    p = Entry(self.__frame)
    p.pack()
    Label(self.__frame,text="INGRESE identificador").pack()
    i = Entry(self.__frame)
    i.pack()
    Label(self.__frame,text="INGRESE comida").pack()
    c = Entry(self.__frame)
    c.pack()
    Label(self.__frame,text="INGRESE ingrese tiempo estimado").pack()
    te = Entry(self.__frame)
    te.pack()
    Label(self.__frame,text="INGRESE precio").pack()
    pre = Entry(self.__frame)
    pre.pack()
    def agregar():
      band = False
      patente = str(p.get())
      identificador = int(i.get())
      comida = str(c.get())
      tiempo_Estimado = int(te.get())
      tiempo_Real = 0
      precio = float(pre.get())
      for moto in self.__lista_M:
        if patente.lower() == moto.patente.lower():
          patente = moto.patente
          band = True
          
      if band:
        pedido = Pedido(patente,identificador,comida,tiempo_Estimado,tiempo_Real,precio)
        self.__lista_P.append(pedido)
        Label(self.__frame,text="SE AGREGOO").pack()
      else:
        Label(self.__frame,text="No está la patente").pack()
        
    boton = Button(self.__frame,text="Toca para agregar pedido",command=agregar)
    boton.pack()
   
  def Mod_Tiempo_Real(self):
    Label(self.__frame,text="INGRESE patente").pack()
    p = Entry(self.__frame)
    p.pack()
    Label(self.__frame,text="INGRESE identificador").pack()
    i = Entry(self.__frame)
    i.pack()
    Label(self.__frame,text="INGRESE tiempo real a agregar al pedido").pack()
    t = Entry(self.__frame)
    t.pack()
    def agregar_tiempo_real():
      patente = str(p.get())
      identificador = int(i.get())
      tiempo = int(t.get())
      j = 0
      band = False
      while j < len(self.__lista_P) and not band:
        if patente.upper() == self.__lista_P[j].patente and identificador == self.__lista_P[j].identificador:
          band = True
        else:
          j+=1
      if band:
        self.__lista_P[j].settiempo_Real(tiempo)
        Label(self.__frame,text=f"Se cambio el tiempo a {self.__lista_P[j].tiempo_Real}").pack()
      else:
        Label(self.__frame,text="No se encontró el pedido").pack()
    boton = Button(self.__frame,text="Toca para cambiar tiempo real",command=agregar_tiempo_real)
    boton.pack()
  
  def calcular_pedido(self):
    Label(self.__frame,text="INGRESE patente").pack()
    p = Entry(self.__frame)
    p.pack()
    def calcular():
      patente = str(p.get())
      i = 0
      suma = 0
      for pedido in self.__lista_P:
        if pedido.patente.strip().lower() == patente.strip().lower():
          i += 1
          suma += int(pedido.tiempo_Real)
      if i!=0:
        Label(self.__frame,text=f"Promedio de tiempo real de la patente {patente.upper()} es:{float(suma/i)}").pack()
      else:
        Label(self.__frame,text=f"La patente {patente.upper()} no tiene pedidos").pack()
        
    boton = Button(self.__frame,text="calcular pedido",command=calcular)
    boton.pack()
  def Comisiones(self):
    Label(self.__frame,text="INGRESE patente").pack()
    p = Entry(self.__frame)
    p.pack()
    def calcular_comisiones():
      patente = str(p.get())
      suma = 0
      Label(self.__frame,text="Identificador de pedido          Tiempo estimado                Tiempo real                  Precio").pack()
      for pedido in self.__lista_P:
        if pedido.patente == patente.upper():
          Label(self.__frame,text=f"{pedido.identificador:<30}      {pedido.tiempo_Estimado:<50} {pedido.tiempo_Real:<20} {pedido.precio:<10}" ).pack() 
          suma += float(pedido.precio)
      Label(self.__frame, text=f"total: {suma:.2f}\n").pack()
      Label(self.__frame,text=f"Comision: {(suma * 0.20):.2f}\n").pack()
    boton = Button(self.__frame,text="calcular comisiones",command=calcular_comisiones)
    boton.pack()
  def ordenar(self):
      self.__lista_P = sorted(self.__lista_P)
      Label(self.__frame,text="Lista de pedidos ordenados:").pack()
      for pedido in self.__lista_P:
        Label(self.__frame,text=f"{pedido}\n").pack()