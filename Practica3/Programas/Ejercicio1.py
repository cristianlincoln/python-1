palabra = input("Dame una palabra: ")
forma_ing = "ing"
palabra2 = ""
if palabra[-2:] == "ar" or palabra[-2:] == "er" or palabra[-2:] == "ir":
    palabra2 = palabra[:-2]+forma_ing
    print("La palabra es {0}".format(palabra2))
else:
    print("La palabra es {0}".format(palabra))

