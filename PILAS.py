""" Crear una pila vacia """
historial = []

""" Aplicar / agregar """
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("historial:", historial)

""" Ver el elemneto superior """
pagina_actual = historial[2]
print("pagina actual:", pagina_actual)

""" Desapilar / pop """
pagina_salida = historial.pop()
print("saliendo de:", pagina_salida)

print("Historial actualizado:", historial)
