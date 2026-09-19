#declarar un arreglo
numeros=[10,20,30,40,50]

#para ver un numero en la posicion 2 es el 30
print(numeros[2])

#modificar el numero de la posicion 3 con 15
numeros[3]=15

#y aqui se mando a imprimir
print(numeros)

#como agregar valor al final de un arreglo, con appened
numeros.append(60)
#imprime los numeros
print(numeros)

#eliminar  con pop en la posicion 1 que es el 20
numeros.pop(1)
print(numeros)

#removemos el 30, eliminamos por valor
numeros.remove(30)
print(numeros)

frutas=["mango","manzana","uva","pera","maracuya"]

#eliminamos por valor eliminamos uva
frutas.remove("uva")
print(frutas)

#eliminamos maracuya
frutas.pop(3)
print(frutas)

#append
frutas.append("chocolate")
print(frutas)

#para modificar un valor
frutas[2]="fresa"
print(frutas)

#declarar un arreglo vacio
arreglo=[]

#ingrsar el tama;o del arreglo
#input 
#se puso el 1 
arreglo=[]
n = int(input("ingrese la longitud del arreglo:"))
n1=int(input("ingresa el valor 0"))
arreglo.append(n1)
print(arreglo)





