# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização #de detalhes do aproveitamento de cada jogador.



lista=list()
dados={'Nome':' ' ,'Gols': ( ),'Total':0}
jogadores=list()
while True:   
    soma=0
    lista.clear()
    dados.clear()
    dados['Nome']=str(input("Nome: ")).strip().title()
    partidas=int(input("Partidas jogadas: "))   
    for g in range(1,partidas+1):
        lista.append(int(input(f"Quantos gols obteve na {g}° partida? ")))
        dados['Gols']=lista.copy()
    for d in lista:
        soma+=d
        dados['Total']=soma
    jogadores.append(dados.copy())
    cont=str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    while cont not in 'SN':
        cont=str(input("\033[1;31mErro!\033[m Quer continuar [S/N]? ")).strip().upper()[0]
    if cont=='N':
        break
print(jogadores)
print("=-"*24)
print("cod ",end=" ")
for i in dados.keys():
    print(f"{i:<15}", end="")
print()
for k,v in enumerate(jogadores):
    print(f"{k:>3} ", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("=-"*24)
while True:
    busca=int(input("Quer mostrar os dados de qual jogador (999 para finalizar): "))
    if busca==999:
        break
    if busca>=len(jogadores):
        print(f"\033[1;31mErro!\033[m Jogador {busca} inexistente.")
    else:
        print(f"*** LEVANTAMENTO DO JOGADOR {jogadores[busca]['Nome']}: ***")
        for i,g in enumerate(jogadores[busca]["Gols"]):
            print(f"No jogo {i+1} fez {g} gols.")
    print("=-"*24)
print('Programa finalizado com sucesso.')