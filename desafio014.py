#Crie um algoritimo que peça a temperatura em Celsius e converta para Fihrenheit.

c=float(input("Digite a temperatura em Celsius (C°): "))
f=c/5*9+32
print("\nA temperatura de {:.1f}°C corresponde a {:.1f}°F.\n".format(c,f))

