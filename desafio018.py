#Faça um programa que leia um angulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse angulo.
 
from math import cos,sin,radians
a=float(input("Digite o valor do angulo: "))
r=radians(a)
s=sin(r)
c=cos(r)
print("\nO angulo digitado {}° tem como seno {:.2f} e cosseno {:.2f} tendo assim uma tangente igual a {:.2f}.".format(a,s,c,s/c))
