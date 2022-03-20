#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um #jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que #algum dado não tenha sido informado corretamente.


def funcao(n,g):
    if n=="":
        n="desconhecido"
    if g=="":
        g="0"
    return f"O jogador {n} fez {g} gols no campeonato."
nome=input("Nome do Jogador: ").strip().title()
gols=input("Numero de Gols: ")
print(funcao(nome,gols))