def contenido_GC(cadena):
    porcentaje = 100
    si_A = False
    si_T = False
    for caracter in cadena:
        if caracter == "A":
            porcentaje = 66,67
            si_A = True
        if caracter == "T":
            porcentaje = 66,67
            si_T = True
    if si_T and si_A:
        porcentaje = 50       
    return porcentaje


##cadena = input("Dame una cadena: ")
##print(contenido_GC(cadena))
            
            
        
