
from EJERCICIO1 import Caja_Ahorro

def CrearCajaAhorro():
    print("Ingrese los datos que se piden\n")
    nro_cuenta = int(input("Numero de cuenta: \n"))
    CUIL = str(input("CUIL:\n"))
    ape = str(input("Apellido: \n"))          
    nom = str(input("Nombre: \n"))
    saldo = float(input("Saldo: \n"))
    return Caja_Ahorro(nro_cuenta, CUIL, ape, nom, saldo)

def cargarcajas(Lista):
  for i in range(1):
    c = CrearCajaAhorro()              #con esta funcion itero tantas veces como instancias de la clase quiera 
    Lista.append(c)                    #y a una funcion le asigno el valor que me devuelve una funcion que es 
                                       #una instacia de la clase y luego se lo agrego a mi lista

def validar_cuit(cuit):
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return False

    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    cuit = cuit.replace("-", "")

    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]

    aux = 11 - (aux - (int(aux / 11) * 11))

    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    return aux == int(cuit[10])
