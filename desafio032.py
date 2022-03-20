#faça um programa que leia um ano qualquer
# e mostre se ele e Bissexto. 

from datetime import date
a=int(input("Digite o ano desejado ou coloque \"0\" para analisar o ano atual: "))
b=(a%4)+(a%400)-(a%100)

if a==0:
    a=date.today().year

if b==0:
    print("\nO ano {} E Bissexto!".format(a))
else:
    print("\nO ano {} NAO e Bissexto!".format(a))
  


