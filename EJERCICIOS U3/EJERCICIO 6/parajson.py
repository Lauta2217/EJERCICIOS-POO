import json
from calefactor import Calefactor
from calefactor_elec import Calefactor_elec
from calefactor_gas import Calefactor_gas
class jsoon:
    def cargar_calefactores(self):
        with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 6/calefactores.json", 'r',) as file:
            data = json.load(file)
        lista = []
        for calefactor in data['calefactores']:
            if calefactor['tipo'] == 'electrico':
                nuevo_calefactor = Calefactor_elec(
                    calefactor['marca'], calefactor['modelo'], calefactor['pais_de_fabricacion'],
                    calefactor['precio_de_lista'], calefactor['forma_de_pago'],
                    calefactor['cant_cuotas'], calefactor['promocion'],
                    calefactor['potencia_max']
                )
            else:
                nuevo_calefactor = Calefactor_gas(
                    calefactor['marca'], calefactor['modelo'], calefactor['pais_de_fabricacion'],
                    calefactor['precio_de_lista'], calefactor['forma_de_pago'],
                    calefactor['cant_cuotas'], calefactor['promocion'],
                    calefactor['matricula'], calefactor['calorias']
                )
            lista.append(nuevo_calefactor)
        return lista

    def guardar_calefactores(self,lista):
        calefactores = []
        for calefactor in lista:
            if isinstance(calefactor, Calefactor_elec):
                calefactores.append({
                    'tipo': 'electrico',
                    'marca': calefactor.marca,
                    'modelo': calefactor.modelo,
                    'pais_de_fabricacion': calefactor.pais_de_fabricacion,
                    'precio_de_lista': calefactor.precio_de_lista,
                    'forma_de_pago': calefactor.forma_de_pago,
                    'cant_cuotas': calefactor.cant_cuotas,
                    'promocion': calefactor.promocion,
                    'potencia_max': calefactor.potencia_max
                })
            else:
                calefactores.append({
                    'tipo': 'gas',
                    'marca': calefactor.marca,
                    'modelo': calefactor.modelo,
                    'pais_de_fabricacion': calefactor.pais_de_fabricacion,
                    'precio_de_lista': calefactor.precio_de_lista,
                    'forma_de_pago': calefactor.forma_de_pago,
                    'cant_cuotas': calefactor.cant_cuotas,
                    'promocion': calefactor.promocion,
                    'matricula': calefactor.matricula,
                    'calorias': calefactor.calorias
                })

        with open("UNIDAD 3/EJERCICIOS U3/EJERCICIO 6/calefactores2.json", 'w') as file:
            json.dump({'calefactores': calefactores}, file, indent=4)
