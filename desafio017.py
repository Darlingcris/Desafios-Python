# Faça um programa que leia o comprimento do cateto 
#oposto e do cateto adjacente de um triangulo retangulo
#Calcule e mostre o comprimento da hipotenusa.

from math import sqrt,hypot
co=float(input("Digite o valor do cateto oposto: "))
ca=float(input("Digite o valor do cateto adjacente: "))
x=(co**2)+(ca**2)
print("O comprimento da Hipotenusa e {:.2f}.\n".format(sqrt(x)))

co=float(input("Digite o valor do cateto oposto: "))
ca=float(input("Digite o valor do cateto adjacente: "))
h=hypot(co,ca)
print("O comprimento da Hipotenusa e {:.2f}.\n".format(hypot(h)))