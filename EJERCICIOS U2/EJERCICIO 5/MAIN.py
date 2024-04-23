from equipos import * #se importan todas las funciones del modulo equipos
from fechas import * #se importan todas las funciones del modulo fechas

if __name__ == '__main__':
  #menu:
  op = int(input("Ingrese opcion:\n 1_Cargar equipos\n 2_Cargar fechas\n 3_Obtener listado de un equipo\n 4_Actualizar datos y mostrarlos\n 5_Ordenar equipos\n 6_Cargar equipos ordenados \n 0_Para finalizar\n"))
  while op!=0:
    if op == 1:
      GE = gestorequipos()
      GE.cargar_equipos_desde_csv()
      GE.mostrar()
    elif op == 2:
      GF = gestorfechas()
      GF.cargar_fechas_desde_csv()
      GF.mostrar()
    elif op == 3:
      GE.buscar(GF)
    elif op == 4:
      GE.actualizar(GF)
      GE.mostrar_todo(GF)
    elif op == 5:
      GE.ordenar()
    elif op == 6:
      GE.cargar_archivo()
    else: print("Numero ingresado no corresponde\n")
    op = int(input("Ingrese opcion:\n 1_Cargar equipos\n 2_Cargar fechas\n 3_Obtener listado de un equipo\n 4_Actualizar datos y mostrarlos\n 5_Ordenar equipos y cargarlos\n 6_Cargar equipos ordenados \n 0_Para finalizar\n"))
  


  """
  if self.__puntos == other.__puntos:
      if self.__dif_de_goles == other.__dif_de_goles:
        if self.__goles_a_favor > other.__goles_a_favor:
          return self.__goles_a_favor > other.__goles_a_favor
      else: 
        return self.__dif_de_goles > other.__dif_de_goles
    else:
      return self.__puntos > other.__puntos
  """