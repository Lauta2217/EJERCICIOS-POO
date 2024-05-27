from clase_lista import Lista
from parajson import Jsoon
from docente import Docente
from personal_apoyo import Personal_apoyo
from investigador import Investigador
from docente_investigador import Docente_Investigador

def buscar(nom):
    if nom.lower() == "docente":
        docente = Docente()
        elem = docente.crear_docente()
        return elem
    elif nom.lower() == "personal apoyo":
        pa = Personal_apoyo()
        elem = pa.crear_personal_apoyo()
    elif nom.lower() == "investigador ":
        inv = Investigador()
        elem = inv.crear_investigador()
        return elem
    elif nom.lower() == "investigador docente":
        invd = Docente_Investigador()
        elem = invd.dcrear_investigador_docente()
        return elem
    else:
        print("CUALQUIER COSA PUSISTE")
    
if __name__ == '__main__':
	lista = Lista()
	jsooon = Jsoon()
	lista.agregarelemento_lista(jsooon.cargar_personal())
	for cale in lista:
		print(f"{cale}")
		print("------------------\n")
		print("CARGADOOOOOS")
	op = int(input("""Ingrese opcion: 
					1_Insertar en posicion determinada 
					2_Cargar a mano
					3_Mostrar agente de determinada posicion
					4_Mostrar agentes especializados en una carrera
					5_Contar cantidad de investigadores y docentes investigadores por area
					6_Listado ordenado por apellido
					7_Determinar cantidad de dinero a solicitar
     					8_Almacenar en otro json
					0_Para finalizar
					"""))
	while op!=0:
		if op == 1:
			clase = str(input("Ingrese tipo de personal\n"))
			pos = int(input("Ingrese la posicion donde lo desea\n"))
			elemento = buscar(clase)
			lista.insertarelemento(elemento,pos)
		elif op == 2:
			clase = str(input("Ingrese tipo de personal\n"))
			elemento = buscar(clase)
			lista.agregarelemento(elemento)
		elif op == 3:
			lista.mostrarelemento(pos = int(input("Ingrese posicion para consultar\n")))
		elif op == 4:
			lista.agentes_especializados(carrera = str(input("Ingrese carrera a consultar\n")))
		elif op == 5:
			lista.agentes_area(area = str(input("Ingrese area a consultar\n")))
		elif op == 6:
			lista.listado_agentes()
		elif op == 7:
			lista.solicitar_dinero(cate = str(input("Ingrese categoria: I, II, III, IV o V\n")))
		elif op == 8:
			jsooon.guardar_agentes(lista)
		else: print("Numero ingresado no corresponde")
		op = int(input("""Ingrese opcion: 
					1_Insertar en posicion determinada 
					2_Cargar a mano
					3_Mostrar agente de determinada posicion
					4_Mostrar agentes especializados en una carrera
					5_Contar cantidad de investigadores y docentes investigadores por area
					6_Listado ordenado por apellido
					7_Determinar cantidad de dinero a solicitar
     					8_Almacenar en otro json
					0_Para finalizar
					"""))