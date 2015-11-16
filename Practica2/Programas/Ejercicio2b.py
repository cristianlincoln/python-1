##num = int(input("Dame un numero entero positivo: "))
##
##resultado = 0
##
##for i in range(num+1):
##    if i**2 <= num:
##        resultado = i
##    
##
##print(resultado)

    

#Leer valores.

m = 0
while m<=0:
    m = int(input("Dame el valor de m (positivo): "))

#Calcular la raiz entera

i  = 1
while i**2 <=m:
    raiz = i
    i += 1

#Imprimir

print("La raiz cuadrada entera de {0} es {1}" .format(m,raiz))




        
        
