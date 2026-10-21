pila = []
while True:
        print("1-Insertar ")
        print("2-Borrar")
        print("3-Listar")
        print("4-Salir")

        opcion=input("Elige una:")

        if opcion=="1":
            numero = int(input("Elige un numero:"))
            pila.append(numero)
        elif opcion=="2":
            if len(pila)>0:
                pila.pop()
                print("eliminado")
            else:
                print("esta vacia")
        elif opcion=="3":
            print(pila)
        elif opcion=="4":
            break
        else:
            print("no hay mas")

   
