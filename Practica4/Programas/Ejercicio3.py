def son_amigos(n1,n2):
    amigos = False
    suma_n1 = 0
    suma_n2 = 0

    for i in range(1,n1):
        if n1%i == 0:
            suma_n1 = suma_n1 + i
    for j in range(1,n2):
        if n2%j == 0:
            suma_n2 = suma_n2 + j
    if suma_n1 == n2 and suma_n2 == n1:
        amigos = True
    return amigos

numero1 = int(input("Dame un numero entero: "))
numero2 = int(input("Dame otro numero: "))
print(son_amigos(numero1, numero2))
