def crear_lista_digitos(numero):
    lista = []
    while numero > 0:
        numero2 = numero%10
        lista = [numero2] + lista
        numero = numero//10
    return lista

numero = int(input("Dame un numero entero: "))
print(crear_lista_digitos(numero))
        
        
        
            
        
