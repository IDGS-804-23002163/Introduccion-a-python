
import os





''' 
def funcion1():
    print("esta es la funcion1")
    
def funcion2():
    os.system("cls")
    
def funcion3():
    print("esta es la funcion3")
    
    
def main():
    funcion1()
    funcion2()
    funcion3()
    
    
if __name__ == "__main__":
    main()
    



crear una programa que permita realisar las operaciones basicas
utilizando funciones para cada operacion y un menu principal para desplegar y 
elegir que operacion realizar
'''


def suma():
    print("Ingresa dos números para sumarlos")
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = num1 + num2
    return resultado


def resta():
    print("ingresa dos numeros para restarlos")
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingresa el segundo numero: "))
    resultado=num1-num2
    return resultado

def multiplicacion():
    print("ingresa dos numeros para multiplicar")
    num1=int(input("ingrsa el primer numero: "))
    num2=int(input("ingresa el segundo numero: "))
    resultado=num1*num2
    return resultado

def division():
    print("ingresa dos numeros para dividir")
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingresa el segundo numero: "))
    resultado=num1/num2
    return resultado

def main():
    print("menu principal")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")   
    opcion=input("ingresa una opcion: ")
    if opcion=="1":
        print(suma())
    elif opcion=="2":
        print(resta())
    elif opcion=="3":
        print(multiplicacion())
    elif opcion=="4":
        print(division())
        
if __name__ == "__main__":
    main()
    