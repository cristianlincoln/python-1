def es_narcista(n):
    es_narcista = True
    comparar = n
    suma_potencia = 0
    while es_narcista and n != 0:
        suma_potencia = suma_potencia + (n%10)**3
        n = n//10
    if suma_potencia != comparar:
        es_narcista = False
    return es_narcista

numero = int(input("Dame un numero: "))
print(es_narcista(numero))
