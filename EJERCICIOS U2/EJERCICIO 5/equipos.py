import csv
from fechas import * 
class Equipos():
  def __init__(self,idd_equipo, nom_equipo,goles_a_favor, goles_en_contra, dif_de_goles,puntos):
    self.__idd_equipo = idd_equipo
    self.__nom_equipo = nom_equipo
    self.__goles_a_favor = int(goles_a_favor)
    self.__goles_en_contra = int(goles_en_contra)
    self.__dif_de_goles = int(dif_de_goles)
    self.__puntos = puntos
  def __str__(self): #cuando yo coloque print(equipos) muestra por pantalla lo que retorna la funcion
    return self.__nom_equipo
  def __gt__(self, other): #esto es para el ordenamiento con el operador >
    if self.__puntos == other.__puntos: #Verifica si los puntos son iguales
      if self.__dif_de_goles == other.__dif_de_goles: #Verifica si la diferencia de goles es la misma
        return self.__goles_a_favor > other.__goles_a_favor #Si los puntos y la diferencia de goles son iguales, compara la cantidad de goles a favor 
      else:
        return self.__dif_de_goles > other.__dif_de_goles #Si los puntos son iguales pero la diferencia de goles no lo es, devuelve True si la diferencia de goles del equipo actual es mayor que la del otro equipo, de lo contrario, devuelve False.
    else:
      return self.__puntos > other.__puntos #i los puntos del equipo actual son mayores que los del otro equipo, devuelve True; de lo contrario, devuelve False.
    
  def listar(self): #esta funcion coloca los datos de un equipo en forma de lista
    return [self.__idd_equipo,self.__nom_equipo,self.__goles_a_favor,self.__goles_en_contra,self.__dif_de_goles,self.__puntos]
        
class gestorequipos():
  def __init__(self,lista = []):
    self.__lista = lista
    
  def cargar_equipos_desde_csv(self):
    with open("UNIDAD 2/EJERCICIOS U2/EJERCICIO 5/equipos2024.csv",newline='') as archivo_csv: #sirve para abrir un archivo y le da un nombre "archivo_csv"
      reader = csv.reader(archivo_csv) #almacena los datos del archivo en una variable
      for fila in reader: #itera los datos del archivo que fueron pasados a la variable por fila
        equipos = Equipos(*fila) #a una variable le asigna los atributos que tiene el archivo y que deben ser iguales a los que tiene la clase
        self.__lista.append(equipos) #agrega los atributos a la lista
    print("Los equipos fueron cargados correctamente\n")
    
  def mostrar(self):
    for equipos in self.__lista:
      print(equipos)#usa el operador str    
      
  def buscar(self,GF):
    i = 0
    nom = input("Ingrese nombre del equipo a buscar\n").strip().lower()
    for equipos in self.__lista: #Recorro los equipos de la lista
      if nom == equipos._Equipos__nom_equipo.strip().lower(): #comparo si el nombre ingresado coincide con el nombre del equipo actual strip()elimina espacios en blanco y lower()convierte cadenas en minusculas
        f = GF.buscarfechas(equipos._Equipos__idd_equipo) #me traigo una lista con fechas desde el otro gestor
        print(f"Equipo:{nom} \n")
        print(" Fecha         Goles a Favor       Goles en Contra      Diferencia de Goles        Puntos")
        for fecha in f:
          i+=1
          print(f"{fecha:<20}{equipos._Equipos__goles_a_favor:<17} {equipos._Equipos__goles_en_contra:<30} {equipos._Equipos__dif_de_goles:<15} {equipos._Equipos__puntos:<20}")
        print("-----------------------------------------------------------------------------------------------\n")
        print(f"Total:                {(i * int(equipos._Equipos__goles_a_favor)):<17} {(i * int(equipos._Equipos__goles_en_contra)):<30} {(i * int(equipos._Equipos__dif_de_goles)):<15} {(i * int(equipos._Equipos__puntos)):<20}")
                                      #la i es porque la profe me dijo que habia que sumar los datos de los
                                      #equipos tantas veces como partidos que jugaron tonce multiplico por las veces que sale 
  def actualizar(self,GF):
    for equipos in self.__lista: #Recorro los equipos de la lista
      print(equipos)
      if  GF.buscarequipo(equipos._Equipos__idd_equipo): #verifico si el equipo ha jugado
        print(f" el equipo: {equipos._Equipos__nom_equipo}Si jugó\n")
        equipos._Equipos__goles_a_favor += int(GF.obtener_goles_favor(equipos._Equipos__idd_equipo)) #sumo los goles que hizo en cada partido
        equipos._Equipos__goles_en_contra += int(GF.obtener_goles_contra(equipos._Equipos__idd_equipo))# sumo los goles que le hicieron
        equipos._Equipos__dif_de_goles = int(equipos._Equipos__goles_a_favor - equipos._Equipos__goles_en_contra) #saco la dif de goles(goles a favor - goles en contra)
  
  def mostrar_todo(self,GF): #copia del buscar nada mas que le quite un par de cosas para que muestre todos los equipos
    for equipos in self.__lista:
        f = GF.buscarfechas(equipos._Equipos__idd_equipo)
        print(f"Equipo:{equipos._Equipos__nom_equipo} \n")
        print(" Fecha         Goles a Favor       Goles en Contra      Diferencia de Goles        Puntos")
        for fecha in f:
          print(f"{fecha:<20}{equipos._Equipos__goles_a_favor:<17} {equipos._Equipos__goles_en_contra:<30} {equipos._Equipos__dif_de_goles:<15} {equipos._Equipos__puntos:<20}")
        print("-----------------------------------------------------------------------------------------------\n")
  
  def ordenar(self):
      self.__lista = sorted(self.__lista) #ordena solito en base al operador __str__
      print("Equipos ordenados:")
  
  def cargar_archivo(self):
    archivo_csv = "UNIDAD 2/EJERCICIOS U2/EJERCICIO 5/E2024ordenados.csv" #a una variable le asigno un archivo
    with open(archivo_csv, mode='w', newline='') as file: #Se abre el archivo en modo escritura con la w
      writer = csv.writer(file) #Se crea un objeto escritor de CSV (writer) asociado al archivo abierto
      for equipos in self.__lista: # me muevo por cada equipo de la lista
        fila = equipos.listar() #llamo la funcion que me lista los datos de los equipos
        writer.writerow(fila) #Este método toma una lista como argumento y escribe sus elementos como una fila en el archivo
          
  
    

        