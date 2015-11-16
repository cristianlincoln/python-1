##entero = -1
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


entero = -1
lista = []
invertida = []

while entero < 0:
    entero = int(input("Dame un numero entero > 0: "))

while entero != 0:
    numero = entero%10
    entero = entero//10
    lista = [numero] + lista

##for elem in lista:
##    invertida = [elem] + invertida
    
print(lista)
