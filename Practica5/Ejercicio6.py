# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    s = menu_ADN()

    if s == 1:
        cadena = input("Dame una cadena: ")
        print(contenido_GC(cadena))
    elif s == 2:
        cadena = input("Dame una cadena: ")
        print(expansion_triplete_CAG(cadena))
    else:
        print("No es una opcion valida")
