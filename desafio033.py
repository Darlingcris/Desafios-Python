#faça um programa que leia tres numeros e
# mostre qual è o maior e qual è o menor. 

import math
a=int(input("\nDigite o primeiro numero: "))
b=int(input("\nDigite o segundo numero: "))
c=int(input("\nDigite o terceiro numero: "))

menor=a
if b<a and b<c:
    menor=b
if c<b and c<a:
    menor=c
print("\nO menor numero digitado foi o {}".format(menor))
    
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print("\nO maior numero digitado foi o {}".format(maior))




    







