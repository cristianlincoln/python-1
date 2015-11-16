

lista = [14288, 15472, 14536, 14264, 12496]
lista_suma = []
suma = 0
sociables = True

for num in lista:
    for i in range(1,num):
        if num%i == 0:
            suma = suma + i
    lista_suma.append(suma)
    suma = 0
    ultimo = lista_suma[-1]
    primero = lista[0]
del lista_suma[-1]
del lista[0]

for i in range(len(lista)):
    if lista[i] != lista_suma[i]:
        sociables = False
        break
if primero != ultimo:
    sociables = False

print(sociables)
            

            
            
        
