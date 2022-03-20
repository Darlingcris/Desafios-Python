#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a #listagem de números gerados e também indique o menor e o maior valor que estão na tupla



from random import randint
n1=randint(0,10)
n2=randint(0,10)
n3=randint(0,10)
n4=randint(0,10)
n5=randint(0,10)
maior=menor=0

sorteio=(n1,n2,n3,n4,n5)
print(sorteio)
   
print(f"O maior valor é: {max(sorteio)}.")
print(f"O menor valor é: {min(sorteio)}.")