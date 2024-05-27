import json
from docente import Docente
from personal_apoyo import Personal_apoyo
from investigador import Investigador
from docente_investigador import Docente_Investigador

class Jsoon:
    def cargar_personal(self):
        with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 7/personal_1.json", 'r',encoding='utf-8') as file:
            data = json.load(file)
        
        personal = []
        for info in data['personal']:
            tipo = info['tipo'].lower()
            if tipo == 'docente':
                personal.append(Docente(**info))
            elif tipo == 'personal_apoyo':
                personal.append(Personal_apoyo(**info))
            elif tipo == 'investigador':
                personal.append(Investigador(**info))
            elif tipo == 'docente_investigador':
                personal.append(Docente_Investigador(**info))
        return personal
    
    def guardar_agentes(self,lista):
        agentes= []
        for agente in lista:
            if isinstance(agente, Docente):
                agentes.append({
                    'tipo': 'docente',
                    'cuil': agente.cuil,
                    'apellido': agente.apellido,
                    'nombre': agente.nombre,
                    'sueldo_basico': agente.sueldo_basico,
                    'antiguedad': agente.antiguedad,
                    'carrera': agente.carrera,
                    'cargo': agente.cargo,
                    'catedra': agente.catedra
                })
            elif isinstance(agente, Investigador):
                agentes.append({
                    'tipo': 'investigador',
                    'cuil': agente.cuil,
                    'apellido': agente.apellido,
                    'nombre': agente.nombre,
                    'sueldo_basico': agente.sueldo_basico,
                    'antiguedad': agente.antiguedad,
                    'area_investigacion':agente.area_investigacion,
                    'tipo_investigacion': agente.tipo_investigacion
                })
            elif isinstance(agente, Docente_Investigador):
                agentes.append({
                    'tipo': 'Docente_Investigador',
                    'cuil': agente.cuil,
                    'apellido': agente.apellido,
                    'nombre': agente.nombre,
                    'sueldo_basico': agente.sueldo_basico,
                    'antiguedad': agente.antiguedad,
                    'carrera': agente.carrera,
                    'cargo': agente.cargo,
                    'catedra': agente.catedra,
                    'area_investigacion':agente.area_investigacion,
                    'tipo_investigacion': agente.tipo_investigacion,
                    'categoria_incentivo': agente.categoria_incentivo,
                    'importe_extra': agente.importe_extra
                })
            elif isinstance(agente, Personal_apoyo):
                agentes.append({
                    'tipo': 'docente',
                    'cuil': agente.cuil,
                    'apellido': agente.apellido,
                    'nombre': agente.nombre,
                    'sueldo_basico': agente.sueldo_basico,
                    'antiguedad': agente.antiguedad,
                    'categoria': agente.categoria,
                })

        with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 7/personalv2.json", 'w') as file:
            json.dump({'personal': agentes}, file, indent=4)
        print("CARGADOS\n")
