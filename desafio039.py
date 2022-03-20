
#Faça um programa que leia o ano de nascimento
#de um jovem e informe, de acordo com sua idade.
#Se ele ainda vai se alistar ao serviço militar
#se è a hora de se alistar
#Se ja passou do tempo do alistamento
#Seu programa tambem devera mostrar o tempo que
#falta ou se passou do prazo.

from datetime import date


anoNascimento=int(input("Digite o ano que voce nasceu com 4 digitos: "))
anoAtual=date.today().year
idade=anoAtual-anoNascimento



if idade>18:
    saldo=idade-18
    print("\nVoce tem {} anos em {}. Deve Procurar a Junta do Serviço Militar (JSM). Voce ja deveria ter se alistado ha {} ano(s).".format(idade,anoAtual,saldo))
    ano=anoAtual-saldo
    print("Voce deveria ter se alistado no ano de {}.".format(ano))
elif idade<18:
    saldo=18-idade
    print("\nVoce tem {} anos em {} e NAO deve se Alistar. Falta(m) {} ano(s) para o seu Alistamento.".format(idade,anoAtual,saldo))
    ano=anoAtual+saldo
    print("Voce deve se Alistar em {}.".format(ano))
else:
    print("\nVoce tem {} anos em {}. E DEVE Fazer o Alistamento Militar ESTE ANO.".format(idade,anoAtual))




  

