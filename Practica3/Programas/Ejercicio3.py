cadena = input("Dame una palabra: ")
cadena2 = input("Dame otra palabra: ")

subcadena = False
n = 0
long = len(cadena)


if len(cadena) > len(cadena2):
    subcadena = False
    
elif len(cadena) == 0 or len(cadena2) == 0:
    subcadena = False
    
    
else:
    for i in range(len(cadena2)):
        if cadena[n] == cadena2[i]:
            n = n+1
##            subcadena = True
            if n == long:
                subcadena = True
                break
        elif cadena[n] != cadena2[i]:
            n = 0
##            subcadena = False
            
                     
if subcadena:
    print("Si es subcadena")
else:
    print("No es subcadena")
    
