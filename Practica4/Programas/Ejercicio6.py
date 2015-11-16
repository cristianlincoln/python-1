from Ejercicio4 import contenido_GC
from Ejercicio5 import expansion_triplete_CAG

def menu_adn():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print ("(1) Calcular el GC de una secuencia de ADN")
        print ("(2) Calcular la expansion del triplete 'CGG' de una secuencia")
        opcion = int(input("Elige opción: "))
    return opcion

s = menu_adn()

if s == 1:
    cadena = input("Dame una cadena: ")
    print(contenido_GC(cadena))
elif s == 2:
    cadena = input("Dame una cadena: ")
    print(expansion_triplete_CAG(cadena))
else:
    print("No es una opcion valida")
            
    
