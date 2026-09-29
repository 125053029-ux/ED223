matriz=[
    [1,2,3],
    [4,5,6]
]
print("mostrar la matriz")
for fila in matriz:
print(fila)
""" mostrar una valor especifico """
print("mostrar 6")
print(matriz[1][2])

""" muestra la fila cero """
print(matriz[0])
matriz[1][1]=8
print(matriz)

""" agregar """
matriz.append([7,8,9])
print(matriz)

""" borrar un valor especifico """
matriz[0].pop(2)
print(matriz)
