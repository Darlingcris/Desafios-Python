#Crie um programa que leie quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares
#ela pode comprar. Considere (US$1=R$ 3.27)

x=float(input("Qual o valor que voce tem disponivel neste momento? R$"))
d=3.27
print("Voce pode comprar US${:.2f}.\n".format(x/d))

x=float(input("Qual o valor que voce tem disponivel neste momento? R$"))
print("Voce pode comprar US${:.2f}.\n".format(x/3.27))

x=float(input("Qual o valor do celular: R$"))
euro=5.60
print("Voce pode comprar este celular por €{:.2f}.\n".format(x/euro))