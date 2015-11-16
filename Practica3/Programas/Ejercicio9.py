matriz = []
filcol = int(input("Dame el valor de n: "))
es_latino = True

#Crea la matriz
for fila in range(filcol):
    matriz.append([0] * filcol)

#Rellenar matriz

for fil in range(filcol):
    for col in range(filcol):
        matriz[fil][col] = int(input("Dame numeros: "))


#Comprobación de las filas
        
for fil in range(filcol):
    for col in range(filcol):
        if matriz[fil][col] in matriz[fil][col+1:]:
            es_latino = False
            break
        else:
            for restofil in range(fil+1,filcol):
                if matriz[fil][col] == matriz[restofil][col]:
                    es_latino = False
                    break
            

#Imprime la matriz

for fil in range(filcol):
    for col in range(filcol):
        print(matriz[fil][col], end = " ")
    print()

print(es_latino)
