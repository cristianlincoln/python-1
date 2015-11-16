def divisores(numero):
    lista = []
    for i in range(1,numero):
        if numero%i == 0:
            lista.append(i)
    return lista

numero = int(input("Dame un numero: "))
print(divisores(numero))
