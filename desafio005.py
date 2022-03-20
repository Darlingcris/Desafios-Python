#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor.

x=int(input("Digite um numero inteiro: "))
a=x-1
s=x+1
print("O numero {} tem como antecessor o numero {} e como sucessor o numero {}.\n".format(x,a,s))

x=int(input("Digite um numero inteiro: "))
print("O numero {} tem como antecessor o numero {} e como sucessor o numero {}.\n".format(x,x-1,x+1))