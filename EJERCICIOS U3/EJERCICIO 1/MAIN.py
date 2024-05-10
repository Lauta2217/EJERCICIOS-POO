from gestor_edificios import *
if __name__ == '__main__':
  GE = gestor_edificios()
  GE.cargar_edificios_desde_csv()
  GE.mostrar()
  op = int(input("""Ingrese opcion: 
                 1_Mostrar propietarios 
                 2_Mostrar superficie total de un edificio 
                 3_Mostrar superficie de un propietario y porcentaje que ocupa del edificio 
                 4_Contar departamentos que cumplen la condicion
                 0_Para finalizar
                 """))
  while op!=0:
    if op == 1:
      nom_E = input("Ingrese nombre del edificio a mostrar propietarios\n")
      GE.mostrar_propietarios(nom_E)
    elif op == 2:
      nom_E = input("Ingrese nombre del edificio a mostrar superficie\n")
      sup = GE.superficie(nom_E)
      print(f"Superficie del edificio: {sup}\n")
    elif op == 3:
      nom_P = input("Ingrese nombre y apellido del propietario a mostrar superficie\n")
      porcentaje = GE.suppropie(nom_P,GE)
      print(f"Porcentaje que ocupan el/los departamentos de {nom_P} es: {porcentaje:.2f}%\n")
    elif op == 4:
      num = int(input("Ingrese numero de piso a contar\n"))
      GE.contar(num)
    else: print("Numero ingresado no corresponde")
    op = int(input("""Ingrese opcion: 
                 1_Mostrar propietarios 
                 2_Mostrar superficie total de un edificio 
                 3_Mostrar superficie de un propietario y porcentaje que ocupa del edificio 
                 4_Contar departamentos que cumplen la condicion
                 0_Para finalizar
                  """))