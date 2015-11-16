maximo = 0
seguido = 0
i = 0
while i<len(adn)-2:
    if adn[i:i+3] == "CAG":
        seguidos + = 1
        i += 3
    elif seguidos > 0:
        if seguidos > maximo:
            maximo = seguidos
        seguidos = 0
        i +=1
    else:
        i+=1
if seguidos > maximo:
    maximo = seguidoos

if maximo == 0:
    return None
else:
    return maximo
