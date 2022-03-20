
#Escreva um programa que leia dois nuemros
#inteiros e compare-os, mostrando na tela
#uma mensagem:
#O primeiro valor è maior
#O segundo valor è maior
#Nao existe valor maior, os dois sao iguais

numero1=float(input("Digite o primeiro numero: "))
numero2=float(input("Digite o segundo numero: "))

if numero1>numero2:
    print("O numero {} e maior que o numero {}".format(numero1,numero2))
elif numero1<numero2:
    print("O numero {} e menor que o numero {}".format(numero1,numero2))
else:
    print("Os numeros {} e {} sao iguais.".format(numero1,numero2))