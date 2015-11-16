def expansion_triplete_CAG(cadena):
    nueva = ""
    comparar = "CAG"
    encontrado = 0
    contador = 0
    maximo = 0
    for i in range(len(cadena)):
        contador = contador + 1
        nueva = nueva + cadena[i]
        if contador == 3:
            if nueva == comparar:
                encontrado = encontrado + 1
                contador = 0
                nueva = ""
                if encontrado > maximo:
                    maximo = encontrado
            else:
                encontrado = 0
                contador = 0
                nueva = ""
        
    if maximo == 0:
        return
    else:
        return maximo

cadena = input("Dame una cadena: ")
print(expansion_triplete_CAG(cadena))
              
        
            
