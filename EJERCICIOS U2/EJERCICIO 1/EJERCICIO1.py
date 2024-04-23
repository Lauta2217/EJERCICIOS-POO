class Caja_Ahorro:
  def __init__(self,nro_cuenta, CUIL, ape, nom, saldo):
    self.__nro_cuenta = nro_cuenta
    self.__CUIL = CUIL
    self.__ape = ape                          #creacion de la clase ya con sus atributos
    self.__nom = nom
    self.__saldo = saldo
  def MostrarDatos(self):
    print('Numero de cuenta: {}\n CUIL: {}\n Apellido: {}\n Nombre: {}\n Saldo: {}\n'.format(self.__nro_cuenta,self.__CUIL,self.__ape,self.__nom,self.__saldo))
  def getCUIL(self):
    return self.__CUIL #devuelve el valor del CUIT
  def Extraer(self):
    importe = float(input("Ingrese importe extraer:\n")) #al realizar una extraccion de dinero el saldo se debe restar
    if (importe <= self.__saldo): #verifica si el importe a retirar es posible
      self.__saldo -= importe 
    else:
      c = self.__saldo - importe
      print("Importe ingresado es mayor al de saldo su cuenta deberá: {}\n".format(c))
  def Ingresar(self): #permite ingresar saldo a la cuenta
    importe = float(input("Importe a ingresar: \n"))
    if(importe>0): #positivo ya que sino seria una extraccion
      self.__saldo += importe     
    else:
      print("importe invalido\n")
def CrearCajaAhorro():
  print("Ingrese los datos que se piden\n")
  nro_cuenta = int(input("Numero de cuenta: \n"))
  CUIL = str(input("CUIL:\n"))
  ape = str(input("Apellido: \n"))          
  nom = str(input("Nombre: \n"))
  saldo = float(input("Saldo: \n"))
  Caja = Caja_Ahorro(nro_cuenta,CUIL,ape,nom,saldo)
  return Caja

def cargarcajas(Lista):
  for i in range(1):
    c = CrearCajaAhorro()              #con esta funcion itero tantas veces como instancias de la clase quiera 
    Lista.append(c)                    #y a una funcion le asigno el valor que me devuelve una funcion que es 
                                       #una instacia de la clase y luego se lo agrego a mi lista
def validar_cuit(cuit):
    # validaciones minimas
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return False
    
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    cuit = cuit.replace("-", "") # remuevo las barras

    # calculo el digito verificador:
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]

    aux = 11 - (aux - (int(aux / 11) * 11))

    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    return aux == int(cuit[10])
if __name__ == '__main__':
    ListaCaja = [] #creo la lista vacia
    cargarcajas(ListaCaja) 
    for i in range(len(ListaCaja)):
        ListaCaja[i].MostrarDatos() #se para en cada instancia y muestra sus datos
    CUIL = int(input("Ingrese cuil para extraer:\n"))
    for i in range(len(ListaCaja)): #Recorro la lista
        if(ListaCaja[i].getCUIL() == CUIL):
            ListaCaja[i].Extraer()
            ListaCaja[i].MostrarDatos()
    CUIL = int(input("Ingrese cuil para ingresar saldo:\n"))
    for i in range(len(ListaCaja)):
        if(ListaCaja[i].getCUIL() == CUIL):
            ListaCaja[i].Ingresar()
            ListaCaja[i].MostrarDatos()
    for i in range(len(ListaCaja)):
        if (validar_cuit(str(ListaCaja[i].getCUIL()))==True):
         print("Cuit valido\n")
        else:
         print("Cuit invalido")          

      
  

  
  
  
