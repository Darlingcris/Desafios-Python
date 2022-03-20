#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados #em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o #maior número no dado.



from random import randint
from time import sleep
from operator import itemgetter

jogo={"jogador 1":(randint(1,6)),
      "jogador 2":(randint(1,6)),
      "jogador 3":(randint(1,6)),
      "jogador 4":(randint(1,6))}

for k,v in jogo.items():
    print(f"O {k} obteve o numero: {v}")
    sleep(1)

print()
print('=-'*17)
print("{:^42}".format("\033[1;32mRANKING DOS JOGADORES\033[m"))
print("--"*17)

ranking=list(sorted(jogo.items(),key=itemgetter(1),reverse=True))
for i,n in enumerate(range(0,4)):         
    print(f"{i+1}° lugar: {ranking[n][0]} com {ranking[n][1]} ponto(s).")
    sleep(1)