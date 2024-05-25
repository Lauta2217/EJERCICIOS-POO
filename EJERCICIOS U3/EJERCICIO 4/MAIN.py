from clase_lista import *
from gestor_CD import *
from gestor_libro_impreso import *
from clase_cd import CD
from clase_libro_impreso import libro_impreso

def agregar_publicacion(lista,publi):
    if publi.upper() == str("CD"):
        cd = gestor_CD()
        lista.agregarpublicacion(cd.crear_cd())
    elif publi.lower() == "libro impreso":
        libro = gestor_libro_impreso()
        lista.agregarpublicacion(libro.crear_libro_impreso())
    else:
        print("Publicacion no existente\n")
        return
        
    
if __name__ == '__main__':
    lista = Lista() 
    op = int(input("""Ingrese opcion: 
                 1_Agregar publicacion
                 2_Determinar tipo de publicacion de una posicion
                 3_Mostrar cantidad de publicaciones de cada tipo
                 4_Mostrar publicaciones con sus precios
                 0_Para finalizar
                 """))
    while op!=0:
        if op == 1:
            publi = str(input("Ingrese tipo de publicacion CD o libro impreso: \n"))
            agregar_publicacion(lista,publi)
        elif op == 2:
            i = 1
            for publicaciones in lista:
                print("\n\n")
                print(f"posicion: {i}\n{publicaciones}\n")
                i+=1
            pos = int((input("Ingrese posicion a consultar\n")))
            publi = lista.buscar(pos-1)
            if isinstance(publi,CD):
                print(f"La publicacion que se encuentra en la posicion {pos} es tipo CD\n")
            elif isinstance(publi,libro_impreso):
                print(f"La publicacion que se encuentra en la posicion {pos} es tipo libro impreso\n")
            else:
                print("Publicacion no existente en esa posicion ingresada\n")
        elif op == 3:
            lista.contar()
        elif op == 4:
            lista.determinar_precio()
            for publi in lista:
                print(f"titulo:{publi.gettitulo()}\ncategoria:{publi.getcategoria()}\nprecio:{publi.getpreciobase():.2f}\n")
            
        else: print("Numero ingresado no corresponde")
        op = int(input("""Ingrese opcion: 
                 1_Agregar publicacion
                 2_Determinar tipo de publicacion de una posicion
                 3_Mostrar cantidad de publicaciones de cada tipo
                 4_Mostrar publicaciones con sus precios
                 0_Para finalizar
                 """))
  

"""
1
CD
Como vivir mejor
autoayuda
1000
lauta lope
60
1
libro impreso
python
programacion
2000
lauta lopez
1999
500
"""