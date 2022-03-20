
#Crie um programa que faça o computador jogar
#JoKenpo (pedra,papel,tesoura) com voce.

from random import randint
from time import sleep
opcoes=("Pedra","Papel","Tesoura")
computador=randint(0,2)
jogador=int(input("\nDigite a opcao que voce deseja: \n0 - Pedra: \n1 - Papel: \n2 - Tesoura:"))
while jogador<0 or jogador>2:
   jogador=int(input("\nDigite a opcao que voce deseja: \n0 - Pedra: \n1 - Papel: \n2 - Tesoura:"))
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!\n")
print("-=" *35)
print("\nO computador escolheu {} e o jogador escolheu {}.".format(opcoes[computador],opcoes[jogador]), end=" ")
if computador==0 and jogador==2:
    print("O computador venceu!\n")
elif computador==1 and jogador==0:
    print("O computador venceu!\n")
elif computador==2 and jogador==1:
    print("O computador venceu!\n")
elif computador==jogador==0 or computador==jogador==1 or computador==jogador==2:
    print("EMPATE!!!\n")
else:
    print("Voce venceu!\n")
print("-="*35)

  



