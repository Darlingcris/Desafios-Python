#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador #perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint
print("°"*20)
print("Jogo: PAR ou IMPAR")
print("°"*20)
escolha=" "
resultado=jogador=0
jogar="s"
while True:
    escolha=str(input("Voce escolhe PAR ou IMPAR [P/I]? ")).lower()[0]
    while escolha!="p" and escolha!="i":
        print("\033[1;31mDigito invalido!\033[m")
        escolha=str(input("Voce escolhe PAR ou IMPAR [P/I]? ")).lower()[0]
    jogador=int(input("Digite um valor: "))
    computador=randint(0,10)
    resultado=computador+jogador
    print(f"O computador escolheu {computador} e voce escolheu {jogador}. A soma é {resultado}.",end= " ")
  
    if escolha=="p":
        if resultado%2==0:
            print("\033[1;33mVoce venceu!\033[m")
        else: 
            print("\033[1;32mO computador venceu!\033[m")
    if escolha=="i":
        if resultado%2==1:
            print("\033[1;33mVoce venceu!\033[m")
        else:
            print("\033[1;32mO computador venceu!\033[m")
    jogar=str(input("Quer continuar a jogar[S/N]? ")).lower()[0]
    while jogar!="s" and jogar!="n":
            print("\033[1;31mDigito invalido!\033[m")
            jogar=str(input("Quer continuar a jogar[S/N]? ")).lower()[0]
    if jogar not in "s":
            break
print("-="*20)
print("O jogo foi finalizado!")