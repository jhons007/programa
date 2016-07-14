import sys
print("programa que muestra un menu")
print("ingrese un rango el primero debe ser menor estrictamente")
print("ingrese el primer numero")
a=input()
a=int(a)
print("ingrese el segundo numero")
b=input()
b=int(b)
resp="si"

def menu():
    while True:
        try:
            print("**********MENU*********")
            print(" 1.- numeros primos")
            print(" 2.- numeros pares")
            print(" 3.- numeros multiplo de 5")
            print(" 4.- numeros capicua")
            print(" 5.- salir")
            
            print("INGRESE UN OPCION")
            c=input()
            c=int(c)
            break
        except:
            print("Vuelva intentar con numero entero")
    if(c==2):
        pares(a,b)
    elif(c==3):
        num(a,b)
    elif(c==4):
        vale(a,b)
    elif(c==5):
        salir()
        
    print("desea continuar on otra opcion")
    resp=input()
    
def pares(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print("los numeros pares es",i,)
def capicua(number):
    num=str(number)
    mid=len(num)/2
    for i in range(0,int(mid)):
        if(num[i]!=num[len(num)-(i+1)]):
            return False
    return True
def vale(a,b):
    for number in range(a,b+1):
        if(capicua(number)):
            print(number)

def ceros(x):
    cont=0
    while(x>0):
        if(x%10==0):
            cont+=1
        x=(x/10)
    return(cont)
def num(a,b):
    for number in range(a,b+1):
        if(ceros(number)>0):
            print(number)
def salir():
    b=0
    while b==0:
        global decidir
        decidir=input("desea realmente salir si o no")
        if decidir.lower()=="si":
            b=1
            print("el programa se esta cerrando")
            sys.exit(1)
        elif decidir.lower()=="no":
            b=1
        else:
            print("debe ingresar de nuevo la opcion")
            b=0
            
    menu()
    
                  
while(resp!="no"):
    menu()
            

