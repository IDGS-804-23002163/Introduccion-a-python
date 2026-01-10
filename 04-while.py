x=0
tem=''

while x<=10:
    tem+=str(x)+'x'
    x+=2
    
print("la suma de los numeros pares menores a 10 es:")
print(tem)

'''operacion de multiplicacion de a x b utilizando sumas
a= 3 
b=4

'''

print("ingresa un numero")
num1 = input()
print("ingresa otro numero")
num2 = input()

num1 = int(num1)
num2 = int(num2)

resultado = 0
contador = 0
while contador < num2:
    resultado += num1
    contador += 1

print("la multiplicacion de {} por {} es {}".format(num1, num2, resultado))
