#escreva um programa que faça o computador "pensar" em um 
# numero inteiro entre 0 e 5 e peca para o usuario tentar 
# descobrir qual foi o numero escolhido
# pelo computador.
# o programa devera escrever na tela se o
# usuario venceu ou perdeu.  

from random import randint
from time import sleep

n=int(input("Digite um numero de 0 a 5: "))
c=randint(0,5)

while n!=c:

    if n>c:
        print("\nO numero escolhido e maior que o numero sorteado.")
        n=int(input("\nDigite um numero de 0 a 5: "))
    elif n<c:
        print("\nO numero escolhido e menor que o numero sorteado.")
        n=int(input("\nDigite um numero de 0 a 5: "))

print("\nParabens voce acertou!!!")

#########


n=int(input("\nDigite um numero de 0 a 5: "))
c=randint(0,5)
if c==n:
    print("\nParabens voce venceu!!!")
else:
    print("\nVoce perdeu, jogue novamente!")

#########

n=int(input("\nVou pensar em um numero, tenta advinhar que numero eu pensei de 0 a 5: "))
c=randint(0,5)
print("Processando...")
sleep(2)

if c!=n:
    print("\nGANHEI!!!Eu pensei no numero {} e nao no {}.".format(c,n))
else:
    print("\nPARABENS!Voce conseguiu me vencer!!!")