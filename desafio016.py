#crie um programa que leia um numero real qualquer pelo teclado
#e mostre na tela a sua porçao inteira.
#ex: digite um numero: 6.127
#O numero 6.127 tem a parte inteira 6.


from math import floor,trunc
num=float(input("Digite um numero real: "))
print("O valor inteiro do numero {} e {}.\n".format(num,floor(num)))

num=float(input("Digite um numero real: "))
print("O valor inteiro do numero {} e {}.\n".format(num,trunc(num)))

num=float(input("Digite um numero real: "))
print("O valor inteiro do numero {} e {}.\n".format(num,int(num)))