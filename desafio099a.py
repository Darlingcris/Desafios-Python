#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#exercicio 99 com def() com entrada para o usuario usando lista:


from time import sleep
def maior(*num):
    num=list()
    print("=-"*15)
    while True:
        n=int(input("Digite os valores inteiros:"))
        num.append(n)
        cont=str(input("Quer continuar? ")).strip().upper()[0]
        while cont not in "SN":
            cont=str(input("Quer continuar? ")).strip().upper()[0]
        if cont=="N":
            break
    print("=-"*15)
    print("Analisando os valores passados...")
    sleep(.5)
    print(f"Os valores foram: {num}")
    print(f"Foram informados {len(num)} valores.")
    print(f"O maior valor foi {max(num)}.")
    print("=-"*15)
maior()