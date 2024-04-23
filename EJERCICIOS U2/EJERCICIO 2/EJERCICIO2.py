from CF import Caja_Ahorro, CrearCajaAhorro
class Contenedor:
    def __init__(self,Lista=[]):
        self.__Lista = Lista 
    def agregarcaja(self):
        self.__Lista.append(CrearCajaAhorro())
    def obtenerdatos(self,cuil):
        encontrado = False
        i = 0
        while (i < len(self.__Lista)) & (encontrado == False):
            if self.__Lista[i].getCUIL() == cuil:
                encontrado = True
            else:
                i += 1
        if encontrado == False:
            print("cuil no valido\n")
        else:
            self.__Lista[i].MostrarDatos()
        
if __name__ == '__main__':
    contenedor = Contenedor()
    contenedor.agregarcaja()
    contenedor.obtenerdatos(cuil=str(input("ingrese cuil:\n")))

     
     
     
     

      
  

  
  
  

    
    
    
    
