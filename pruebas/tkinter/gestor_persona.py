from clase_persona import *
from tkinter import *
class gestor_persona:
  __lista: list
  def __init__(self,root,lista = []):
    self.__lista = lista
    self.__root = root
  
  def cargar(self,nom,edad):
    persona = Persona(nom,edad)
    self.__lista.append(persona)
  
  def mostrar(self):
    for persona in self.__lista:
      Label(self.__root,text=f"{persona}\n").pack()