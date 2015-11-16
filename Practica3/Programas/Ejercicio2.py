cadena = input("Dame una cadena: ")
copia = ""
anterior = " "
contador = 0
for caracter in cadena:
    anterior = caracter
    if caracter != " ":
        copia = copia + caracter
        contador = contador + 1
    if caracter == " " and contador > 2:
        copia = copia + copia[-2] + copia[-1]
        contador = 0
    if anterior == " ":
        copia = copia + " "
        
if anterior != " ":
    copia = copia + copia[-2] + copia[-1]
    
print(copia)
