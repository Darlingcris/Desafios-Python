#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#exercicio 99 sem def():


num=list()
while True:
    n=int(input("Digite os valores inteiros:"))
    num.append(n)
    cont=str(input("Quer continuar? ")).strip().upper()[0]
    while cont not in "SN":
        cont=str(input("Quer continuar? ")).strip().upper()[0]
    if cont=="N":
        break
print(f"Ao todo foram informados {len(num)} valores.")
print(f"E o maior valor informado foi {max(num)}.")