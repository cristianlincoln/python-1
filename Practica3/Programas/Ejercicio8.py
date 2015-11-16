matriz = []
filcol = int(input("Dame el valor de n: "))
n = 0
n2 = 0

#Crea la matriz
for fila in range(filcol):
    matriz.append([0] * filcol)

#Rellenar matriz

for fil in range(filcol):
    n2 = n2 + 1
    for col in range(filcol):
        matriz[fil][col] = n
        n = n+1
    n = 0
    n = n - n2

#Imprime la matriz

for fil in range(filcol):
    for col in range(filcol):
        print(matriz[fil][col], end = " ")
    print()
