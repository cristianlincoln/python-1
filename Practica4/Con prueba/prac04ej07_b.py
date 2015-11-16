import divisores
import suma_lista

def son_sociables (lista):
    sociables = True
    i = 0
    while i <len(lista)-1 and sociables:
        div_n1 = divisores(lista[i])
        div_n1 = div_n1[:-1]
        suma_div_n1 = suma lista(div_n1)
        if suma_div_n1 != lista[i+1]:
            sociables = False
        else:
            i +=1
    div_n1 = divisores(lista[-1])
    div_n1 = div_n1[:-1]
    suma_div_n1 = suma_lista(div_n1)
    if suma_div_n1 != lista[0]:
        sociables = False
    return sociables
