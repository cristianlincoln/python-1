#Ejercicio 1 CosaLosaWosa

num = 1 #Inicializamos el bucle en 1
palabra = "" # Almacenamos la palabra
linea = "" # Guardamos las palabras o numeros
cont_palabras = 0 # Inicializamos el contador de palabras a 0


#Bucle principal del programa

while num <= 110:
    if num % 3 == 0:
        palabra = "Cosa"
        linea = linea + " " + palabra     
    if num % 5 == 0:
        palabra = "Losa"
        linea = linea + " " + palabra
    if num % 7 == 0:
        palabra = "Wosa"
        linea = linea + " " + palabra
    if num % 3 == 0 and num % 5 == 0:
        palabra = "CosaLosa"
        linea = linea + " " + palabra
    if num % 5 == 0 and num % 7 == 0:
        palabra = "LosaWosa"
        linea = linea + " " + palabra
    if num%3 == 0 and num%5 == 0 and num%7 == 0:
        palabra = "CosaLosaWosa"
        linea = linea + " " + palabra    
    if num%3 != 0 and num%5 != 0 and num%7 != 0:
        linea = linea + " " + str(num)    

    num = num + 1 # Aumenta para finalizar el bucle
    nombre = "" # Borra la variable nombre
    cont_palabras = cont_palabras + 1 # Cuenta los numeros o palabras para realizar el salto de línea

    if cont_palabras == 11: # Si tenemos 11 palabras imprime la linea, con el salto y borra la linea y el contador lo pone a 0
        print(linea, end="")
        print()
        cont_palabras = 0
        linea = ""


    


