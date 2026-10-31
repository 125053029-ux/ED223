class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if(self.cabeza is None):
            self.cabeza = nuevo_nodo
            return

        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)

        if(self.cabeza == None):
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        while(actual.siguiente):
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_al_Inicio(self):
        if(self.cabeza is None):            
            return
        self.cabeza = self.cabeza.siguiente
    def Eliminar_Nodo_al_Final(self):
        if(self.cabeza is None):           
            return

        if(self.cabeza.siguiente is None):
            self.cabeza = None
            return
        actual = self.cabeza

        while(actual.siguiente.siguiente):
            actual = actual.siguiente

        actual.siguiente = None

    def Imprimir_ListaEnlazada(self):
        actual = self.cabeza

        while(actual):
            print(actual.numero, " -> ", end=" ")
            actual = actual.siguiente

        print("None")

Mi_lista = ListasEnlazadas()

Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Final()
Mi_lista.Imprimir_ListaEnlazada()