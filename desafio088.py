#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos #jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista #composta.


from random import randint
from time import sleep
print("=-"*20)
print("{:^35}".format("JOGOS DA MEGA SENA"))
print("=-"*20)
jogos=int(input("Quantos jogos voce quer que eu sortei? "))
print("~~"*20)

for n in range(0,jogos):
    sorteio=[randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    num=0
    while num < len(sorteio): 
        if sorteio.count(sorteio[num]) > 1:
            sorteio[num]=randint(1,60)
        
        else:
           num+=1     
    (sleep(.5))
    sorteio.sort()
    print(sorteio)