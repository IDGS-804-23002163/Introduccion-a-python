lista=["dario", 33, 9,5, True, "german", 20.8]

print(lista)
print(lista[1])
print(lista[2])
print(lista[-1])
print(lista[2:3])
print(lista[3:])

lista.append("veganas")
print(lista)
lista.insert(2,"nadia")

lista.extend("uno", 1.1 ,False)


lista.remove(9)

lista.pop()

lista2=["tres", "cuatro"]

lista3=lista+lista2
print(lista3)

print(lista3*4)

lista4=[3,4,3,25,3,4,6,6,4,3,7,5,7,3,4,7,9,67,5,3,45,34,5,3]

lista4.sort()
print(lista4)