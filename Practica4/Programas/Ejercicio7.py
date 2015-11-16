
son_sociables = True
div_ultimo = 0
numero = 0
div_primero = 0
div_anterior = 0
contador = 0
lista = [220,284]
for num in lista:
    for i in range(1,num):
        if num%i == 0:
            div_anterior = div_anterior + i
            div_ultimo = div_anterior
    if contador == 0:
        div_primero = div_anterior
        contador = contador + 1        
        div_anterior = 0
    if contador > 0:
        if numero

        
print(div_primero, div_anterior)
            
            
        
