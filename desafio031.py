#desenvolva um programa que pergunte a distancia de uma
#viagem em KM. Calcule o preço da passagem
#cobrando R$0.50 por Km para viagens de ate
#200Km e R$0.45 para viagens mais longas.

d=float(input("Qual a distancia da sua viagem em Km? "))

if d<=200:
    print("O preco da passagem e R$ {:.2f} reais.".format(d*.5))
else:
    print("O preco da passagem e R$ {:.2f} reais.".format(d*.45))
print("Boa viagem!!!")
