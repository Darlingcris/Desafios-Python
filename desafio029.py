#Escreva um programa que leia a velocidade de
#um carro.
#se ele ultrapassar 80km/h mostre uma mensagem
#dizendo que ele foi multado.
#a multa vai custar R$7.00 por cada Km
#acima do limite.

v=float(input("\nQual a velocidade do carro? Km "))

if v>80:
    print("\nA velocidade e superior a 80 km/h. Voce foi MULTADO.")
    print("\nO valor a pagar sera de R$ {:.2f} reais.".format((v-80)*7))
print("\nDirija com seguranca!") 

#print("\nO valor a pagar sera de R$ {} reais.".format(v-km)*7) #imprimi 5.0 reais a linha sete vezes