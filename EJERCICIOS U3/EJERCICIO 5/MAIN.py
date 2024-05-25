from coleccion import lista_enlazada
if __name__ == '__main__':
    lista = lista_enlazada()
    for i in range(5):
        #inciso b
        lista.agregarelemento(i)
    
    for i in lista:
        print(f"Posicion {i+1} numero{i}")
    #inciso a
    lista.insertarelemento(10,3)
    print("Ya agregado\n")

    for j in lista:
        print(f"Posicion {j+1} numero{j}")
        
    #inciso c
    lista.mostrarelemento(2)
    print(f"maximo:{max(lista)}")