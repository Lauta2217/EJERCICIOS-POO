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
  
def CrearCajaAhorro():
  print("Ingrese los datos que se piden\n")
  nro_cuenta = int(input("Numero de cuenta: \n"))
  CUIL = str(input("CUIL:\n"))
  ape = str(input("Apellido: \n"))          
  nom = str(input("Nombre: \n"))
  saldo = float(input("Saldo: \n"))
  Caja = Caja_Ahorro(nro_cuenta,CUIL,ape,nom,saldo)
  return Caja

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

      
  

  
  
  
