
#A conferederacao Nacioanl de Natacao 
#precisa de um programa que leia o ano
#de nasciemtno de um atleta e mostre 
#sua categoria de acordo com a idade:
#ate 9 anos: Mirim
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 25 anos: Senior
#acima: Master

from datetime import date
nascimento=int(input("Qual o ano de nascimento do Atleta (digite o ano com 4 digitos)? "))
while nascimento<1000 or nascimento>9999:
    nascimento=int(input("ANO INVALIDO! Qual o ano de nascimento do Atleta (digite o ano com 4 digitos)?"))
anoAtual=date.today().year
idade=anoAtual-nascimento

if idade<=9:
    print("O Atleta tem {} anos e esta na Categoria Mirim".format(idade))
elif idade<=14:
    print("O Atleta tem {} anos e esta na Categoria Infantil".format(idade))
elif idade<=19:
    print("O Atleta tem {} anos e esta na Categoria Junior".format(idade))
elif idade<=25:
    print ("O Atleta tem {} anos e esta na Categoria Senior".format(idade))
else:
    print("O Atleta tem {} anos e esta na Categoria Master.".format(idade))

