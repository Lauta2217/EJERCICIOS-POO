
import funciones

def test():
    listaCaja = []
    funciones.cargarcajas(listaCaja)
    for caja in listaCaja:
        caja.MostrarDatos()

    CUIL = input("Ingrese CUIL para extraer:\n")
    for caja in listaCaja:
        if(caja.getCUIL() == CUIL):
            caja.Extraer()
            caja.MostrarDatos()

    CUIL = input("Ingrese CUIL para ingresar saldo:\n")
    for caja in listaCaja:
        if(caja.getCUIL() == CUIL):
            caja.Ingresar()
            caja.MostrarDatos()

    for caja in listaCaja:
        if(funciones.validar_cuit(caja.getCUIL()) == True):
            print("Cuit válido\n")
        else:
            print("Cuit inválido\n")
