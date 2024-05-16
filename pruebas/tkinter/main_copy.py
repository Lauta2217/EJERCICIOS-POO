from tkinter import *
#creacion de la ventana 
def main():
  from gestor_persona import gestor_persona
  root = Tk()
  root.title("EJERCICIOS\n")
  root.geometry("500x500+450+100")
                
  #entrada de datos
  GP = gestor_persona(root)
  Label(root,text="INGRESE NOMBRE Y EDAD DE PERSONA A CARGAR\n").pack()
  Label(root,text="nombre:").pack() 
  entrada1 = Entry(root)
  entrada1.pack()
  Label(root,text="edad:").pack() 
  entrada2 = Entry(root)
  entrada2.pack()
  #limpiar pantalla
  def borrar_contenido():
    # Obtener todos los widgets hijos de la ventana principal
    widgets = root.winfo_children()
      
    # Destruir cada widget
    for widget in widgets:
      widget.destroy()
  #agregar más contenidos a la pantalla
  def mostrar_nuevo_contenido():
    # Aquí puedes crear y agregar los nuevos widgets que deseas mostrar
    nuevo_label = Label(root, text="Datos")
    nuevo_label.pack()
    GP.mostrar()
  #evento de boton
  def boton_pulsado():
    nom = str(entrada1.get())
    edad = int(entrada2.get())
    GP.cargar(nom,edad)
  def boton_pulsado2():
    borrar_contenido()
    mostrar_nuevo_contenido()

  #creacion de boton
  #Button(root,text="Hola que onda\n").pack() #.pack permite ponerlo en pantalla
  boton = Button(root,text="ENVIAR",command=boton_pulsado)
  boton2 = Button(root,text="MOSTRAR",command=boton_pulsado2)
  boton.pack()
  boton2.pack()
  #mantiene la ventaba abierta
  root.mainloop()

if __name__ == '__main__':
  main()