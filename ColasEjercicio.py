from collections import deque

cola = deque()
while True:
     print("\nMenu\n")
     print("1-Insertar")
     print("2-Borrar")
     print("3-Listar")
     print("4-Salir")

     opcion = input(" elige una:")
     if opcion=="1":
        numero = int(input("Selecciona un numero:"))
        cola.append(numero)
        print("agregado")
     elif opcion =="2":
        if len(cola)>0:
            cola.popleft()
            print("eliminado")
        else:
            print("estaba vacia")
     elif opcion=="3":
        print("Cola:",list(cola))
     elif opcion =="4":
        break
     else:
        print("esa no es una opcion")

