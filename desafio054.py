#crie um programa que leia o ano de nasciemento
#de sete pessoas. No final, mostre quantas
#pessoas ainda nao atingiram a maioridade
#e quantas ja sao maiores. (21 anos)


from datetime import date

ano=date.today().year
maior=0
menor=0

for x in range(1,8):
    anoNascimento=int(input("Digite o ano de nascimento da {}° pessoa: ".format(x)))
    idade=ano-anoNascimento
    
    if idade>=21:
        maior+=1
         
    else:
        menor+=1
print("Temos {} pessoas que atingiram a maioridade".format(maior))
print("E {} pessoas que NAO atingiram a maioridade".format(menor))











   