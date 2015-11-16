peso = float(input("Dame tu peso en kg: "))
altura = float(input("Dame tu altura en metros: "))
imc = peso / (altura**2)

if imc >= 40:
    print("El IMC es {0:.2f}, la persona tiene obesidad mórbida" .format(imc))
elif imc >= 30:
    print("El IMC es {0:.2f}, la persona tiene obesidad" .format(imc))
elif imc >= 25:
    print("El IMC es {0:.2f}, la persona tiene sobrepeso" .format(imc))
elif imc >= 18.5 and imc <= 24.99:
    print("El IMC es {0:.2f}, la persona tiene un peso normal" .format(imc))
else:
    print("El IMC es {0:.2f}, la persona tiene bajo peso" .format(imc))
