tupla=("uno","dos","tres")
print(tupla)
#tuplas con multiples tipos de datos
perfil = ("Ana", 28, True, 1.75) # (nombre, edad, es_estudiante, altura)
print(perfil)
#tuplas comn tuplas dentro 
coordenadas = ((10.0, 20.5), (30.1, 40.2)) # (punto1, punto2)
print(coordenadas[0]) # Accede a la primera tupla: (10.0, 20.5)
print(coordenadas[0][1]) # Accede al segundo elemento de la primera

#desestructuracion de una tupla
datos_usuario = ("Carlos", "carlos@email.com")
nombre, email = datos_usuario # Desestructura la tupla en dos variables
print(f"Nombre: {nombre}, Email: {email}")
