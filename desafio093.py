#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do #jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No #final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.



soma=0
lista=list()
dados={'Nome':" ",'Gols': (),'Total':0}
print()
dados['Nome']=str(input("Nome: ")).strip().title()
partidas=int(input("Partidas jogadas: "))

for g in range(1,partidas+1):
    gols=int(input(f"Quantos gols obteve na {g}° partida? "))
    lista.append(gols)
    dados['Gols']=lista
    soma+=gols

dados['Total']=soma
print('=-'*24)
print(dados)

print("=-"*24)
for k,v in dados.items():
    print(f"{k}:   {v}")
print("=-"*24)
print(f"O jogador {dados['Nome']} jogou {partidas} partidas:")
print()
for i,g in enumerate(lista):
    print(f"Partida {i+1} => fez {g} gols.")
print()
print(f"Totalizando {dados['Total']} gol(s).")