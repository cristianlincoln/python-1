entero = -1
entero2 = -1
lista = []
lista2 = []
lista3 = []
nuevo = 0
nuevo2 = 0
invertida = []

while entero < 0:
    entero = int(input("Dame un numero entero > 0: "))
while entero2 < 0:
    entero2 = int(input("Dame un numero entero > 0: "))

while entero != 0:
    numero = entero%10
    entero = entero//10
    lista.append(numero)

while entero2 != 0:
    numero2 = entero2%10
    entero2 = entero2//10
    lista2.append(numero2)
    
n = 1
n2 = 1

for i in lista:
    nuevo = nuevo + i*n
    n = n*10

for i in lista2:
    nuevo2 = nuevo2 + i*n2
    n2 = n2*10
    
## Sumar listas, no enteros!

    
suma = nuevo + nuevo2


while suma != 0:
    numero3 = suma%10
    suma = suma//10
    lista3.append(numero3)

for elem in lista3:
    invertida = [elem] + invertida
    
print(invertida)

