def expansion_triplete_CAG(cadena):
    repeticiones = 0
    comparar = "CAG"
    nueva = ""
    contador = 0
    for i in range(len(cadena)):
        if contador != 3:
            nueva = nueva + cadena[i]
            contador = contador + 1
        if comparar == nueva:
            repeticiones = repeticiones + 1
            nueva = ""
            contador = 0
        if contador == 3 and comparar != nueva:
            nueva = ""
            contador = 0
            
    if repeticiones == 0:
        return
    else:
        return repeticiones
    
cadena = input("Dame una cadena: ")
print(expansion_triplete_CAG(cadena))
            
            
        
