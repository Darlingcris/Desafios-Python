#faça um programa que leia um numero qualquer e mostre o seu fatorial. fazer com o While e o For.
#fatorial e o numero com a !.ex: 5!=5*4*3*2*1=120

from math import factorial
numero=int(input("Digite um numero para saber o seu fatorial: !"))
fatorial=factorial(numero)
print("O fatorial do numero {}! tem como resultado o valor {}.".format(numero,fatorial))

numero=int(input("Digite um numero para saber o seu fatorial: !"))
fatorial=1
c=numero
while c>=1:
    print("{}".format(c),end=" ")
    print("x" if c>1 else "=",end=" ")
    fatorial*=c
    c-=1
print("{}".format(fatorial))

numero=int(input("Digite um numero para saber o seu fatorial: !"))
fatorial=1
contador=numero
while contador>=1:
    print("{}".format(contador),end=" ")
    print("x" if contador>1 else "=",end=" ")
    fatorial*=contador
    contador-=1
print("{}".format(fatorial))


numero=int(input("Digite um numero para saber o seu fatorial: !"))
fatorial=1
for x in range (numero,0,-1):
    print("{}".format(x),end=" ")
    print("x" if x>1 else "=",end=" ")
    fatorial*=x
print("{}".format(fatorial))
