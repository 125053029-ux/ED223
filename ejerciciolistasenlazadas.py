""" Clase que representa la estructura del nodo """
class Nodo:
    def _init_(self, numero):
        """ valor que tendra el nodo """
        self.numero = numero
        """ apunta a nuestro suigiente nodo """
        self.siguiente = None
        
    """ claseque va a administrar todos los nodos """ 
class ListasEnlazadas:
    def _init_(self):
        self.cabeza = None
    """ insertar otro """
    def Insertar_Nodo_al_Inicio(self,numero):
        nuevo_nodo = Nodo(numero)
        
        if(self.cabeza is None):
            self.cabeza = Nodo(numero)
        
            return
    
  
        nuevo_nodo.siguiente = self.cabeza
    
        self.cabeza = nuevo_nodo
    
    def Insertar_Nodo_al_Final(self,numero):
        nuevo_nodo = Nodo(numero)
        if(self.cabeza == None):
            self.cabeza = nuevo_nodo

            return
        
        actual =self.cabeza
        
        while(actual.siguiente):
            actual = actual.siguiente
            actual.siguiente = nuevo_nodo            
            
    def Imprimir_ListaEnlazada(Self):
        actual = self.cabeza
        while(actual):
            print(actual.numero,"->",end="")
            
            actual =actual.siguiente
        print("None")
            
Mi_lista = ListasEnlazadas()
       
Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Imprimir_ListasEnlazadas()