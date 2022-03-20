#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual #será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão #entregues. OBS:
##considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print("--"*10)
print("{:^30}".format("\033[1;34mBANCO MADJÀ\033[m"))
print("--"*10)

valor=nota50=nota20=nota10=nota1=restante1 = restante2 = restante3 = restante4 = 0

valor=int(input("Saque: R$ "))

nota50 = valor // 50
restante1 = valor - (nota50*50)
nota20 = restante1 // 20
restante2 = restante1 - (nota20*20)
nota10= restante2 // 10
restante3 = restante2 - (nota10*10) 
nota1 = restante3 //1
restante4 = restante3 - (nota1*1)

print(f"\nTotal de {nota50:^2} cédula(s) de R$ 50.00\nTotal de {nota20:^2} cédula(s) de R$ 20.00\nTotal de {nota10:^2} cédula(s) de R$ 10.00\nTotal de {nota1:^2} cédula(s) de R$ 1.00")

print("=-"*20)
print("\033[1;34mPROGRAMA FINALIZADO!\033[m")