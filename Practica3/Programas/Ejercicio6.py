##entero = -1
##entero3 = ""
##lista = []
##
##while entero < 0:
##    entero = int(input("Dame un numero entero > 0: "))
##
##entero2 = str(entero)
##
##for i in entero2:
##    lista.append(int(i))
##
##print(lista)
##
##for i in lista:
##    entero3 = entero3 + str(i)
##
##int(entero3)
##
##print(entero3)

entero = -1
lista = []
nuevo = 0

while entero < 0:
    entero = int(input("Dame un numero entero > 0: "))

while entero != 0:
    numero = entero%10
    entero = entero//10
    lista = [numero] + lista
print(lista)
    
##n = 1
##
##for i in lista:
##    nuevo = nuevo + i*n
##    n = n*10
    
##multi=10**(len(lista)-1)
##for d in lista:
##    nuevo = nuevo + (d*multi)
##    multi = multi//10 
##
##print(nuevo)
