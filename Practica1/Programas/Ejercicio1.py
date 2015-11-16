#Programa para calcular la temperatura de sensación.

temp_aire = int(input("Dame la temperatura del aire en Celsius: ")) # Pedimos al usuario la temperatura del aire
velocidad = int(input("Dame la velocidad en Km/H: ")) # Pedimos al usuario la velocidad del aire

temp_sen = 13.12 + 0.6215 * temp_aire - 11.37 * velocidad ** 0.16 + 0.3965 * temp_aire * velocidad ** 0.16 # Pedimos la temperatura

print("La temperatura de sensación es {0:.2f}".format(temp_sen)) #Imprimimos el resultado
