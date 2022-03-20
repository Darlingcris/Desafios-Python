#Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10.
#So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos papites foram
#necessarios para vencer.

from random import randint
computador=randint(0,10)
tentativas=0
jogador=-1
while jogador!=computador:
    jogador=int(input("Digite um numero entre 0 e 10: "))
    while jogador<0 or jogador>10:
        jogador=int(input("NUMERO INVALIDO. Digite um numero entre 0 e 10: "))
    if jogador<computador:
        print("O numero e menor que o numero escolhido pelo computador.") 
    elif jogador>computador:
        print("O numero e maior que o numero escolhido pelo computador.")       
    else:   
        print("\nVoce ACERTOU!", end=" ")
    tentativas+=1
print("Foram {} tentativa(s).".format(tentativas))
    




