#crie um programa que leia um numero inteiro
#e mostre na tela se ele e Par ou Impar.

n=int(input("Digite um numero inteiro: "))
p=n%2


if p==0:
    print("\nO numero {} e \"PAR\".".format(n))
else:
    print("\nO numero {} e \"IMPAR\".".format(n))


