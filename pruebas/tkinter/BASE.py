from tkinter import *
#creacion de la ventana 
root = Tk()
root.title("Prueba\n")
root.geometry("500x500+450+100")
              
#entrada de datos
Label(root,text="INGRESE DOS NUMEROS Y DELE AL BOTON PARA SUMAR")
entrada1 = Entry(root)
entrada1.pack()
entrada2 = Entry(root)
entrada2.pack()

#evento de boton
def boton_pulsado():
  print("Boton pulsado")
  num1 = int(entrada1.get())
  num2 = int(entrada2.get()) #captura lo que tenga entrada
  #Label(root,text="boton pulsado muestra en pantalla\n").pack()
  Label(root,text =f"{num1+num2}").pack() #printear lo que tiene la entrada
  
#creacion de boton
#Button(root,text="Hola que onda\n").pack() #.pack permite ponerlo en pantalla
boton = Button(root,text="esto es otro boton",command=boton_pulsado)
boton.pack()

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
      nuevo_label = Label(root, text="Nuevo contenido")
      nuevo_label.pack()
      GP.mostrar()


















#mantiene la ventaba abierta
root.mainloop()