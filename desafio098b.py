#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e #passo. Seu programa tem que realizar três contagens através da função #criada:                                                                                                   #a) de 1 até 10, de 1 em 1                   
#b) de 10 até 0, de 2 em 2                                                                    
#c) uma contagem personalizada

#exercicio 98 sem def():


from time import sleep
for n in range(1,11,1):
    print(n, end=" ")
    sleep(.2)
print("Fim!")

for n in range(10,-1,-2):
    print(n,end=" ")
    sleep(.2)
print("Fim!")

cont1=int(input("Inicio: "))
cont2=int(input("Fim: "))
cont3=int(input("Passo:" ))
if cont3==0:
    cont3=1
if cont1>cont2 and cont3>0:
    cont3=-cont3

for n in range (cont1,cont2-1,cont3):
    print(n, end=" ")
print("Fim!")