from tkinter import *
from pedidos import *

def scroll_canvas(canvas,event):
  canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
def menu(root):
  menu_principal = Menu(root)
  # Crear un Canvas para contener la barra de desplazamiento
  #canvas = Canvas(root)
  #canvas.pack(side=LEFT, fill=BOTH, expand=True)
  
  canvas = Canvas(root)
  canvas.pack(fill = BOTH, expand = True)
  
  # Vincular el evento de ratón al Canvas
  canvas.bind_all("<MouseWheel>", lambda event:scroll_canvas(canvas,event))
  
  # Crear una barra de desplazamiento y asociarla al Canvas
  scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
  scrollbar.pack(side=RIGHT, fill=Y)

  # Configurar el Canvas para trabajar con la barra de desplazamiento
  canvas.configure(yscrollcommand=scrollbar.set)
  canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

  # Crear un Frame dentro del Canvas para colocar los elementos
  frame = Frame(canvas)
  canvas.create_window((0, 0), window=frame, anchor="nw")
  #ajustar el tamaño del frame al tamaño del root
  frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
  # Aquí puedes agregar tus elementos (botones, etiquetas, etc.) al Frame
  GP_M = gestor(frame)
  GP_M.cargar_motos_desde_csv()
  GP_M.cargar_pedidos_desde_csv()
  #creacion de submenu
  menu_motos = Menu(menu_principal)
  menu_funciones_motos = Menu(menu_motos)
  menu_motos.add_cascade(label ="FUNCIONES PARA MOTOS\n",menu = menu_funciones_motos)
  menu_funciones_motos.add_command(label = "Mostrar motos cargadas\n", command = GP_M.mostrar_M)

  
  menu_funciones_pedidos = Menu(menu_motos)
  menu_motos.add_cascade(label ="FUNCIONES PARA PEDIDOS\n",menu = menu_funciones_pedidos)
  menu_funciones_pedidos.add_command(label = "Mostrar pedidos cargados\n", command = GP_M.mostrar_P)
  menu_funciones_pedidos.add_command(label = "Asignar pedido a moto\n",command = GP_M.asignar_pedido_a_moto)
  menu_funciones_pedidos.add_command(label = "Modificar tiempo real\n",command = GP_M.Mod_Tiempo_Real)
  menu_funciones_pedidos.add_command(label = "Calcular pedido\n",command = GP_M.calcular_pedido)
  menu_funciones_pedidos.add_command(label = "Calcular comisiones\n",command = GP_M.Comisiones)
  menu_funciones_pedidos.add_command(label = "Ordenar pedidos\n",command = GP_M.ordenar)
  
  
  

  #agregar menu al menu principal
  menu_principal.add_cascade(label = "MOTOS Y PEDIDOS", menu = menu_motos)
  
  #agregar menu a la pantalla principal es decir root
  root.config(menu = menu_principal)
def main():
    root = Tk()
    root.resizable(False,False)
    root.title("EJERCICIO MOTOS")
    root.geometry("700x500+300+150") #lo primero es largo segundo ancho y despues padding en el mismo orden
    menu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
