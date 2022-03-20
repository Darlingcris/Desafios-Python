#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e #passo. Seu programa tem que realizar três contagens através da função #criada:                                                                                                   #a) de 1 até 10, de 1 em 1                   
#b) de 10 até 0, de 2 em 2                                                                    
#c) uma contagem personalizada


from time import sleep
def contador (cont1,cont2,cont3):
    print("=-"*20)
    print(f"Contagem de {cont1} ate {cont2} de {cont3} em {cont3}:")
    if cont3==0:
        cont3=1
    if cont3<0:
        cont3*=-1
    if cont1>cont2 and cont3>0:
        cont3=-cont3
    if cont1>cont2:
        cont2-=1
    if cont1<cont2:
        cont2+=1    
    for n in range(cont1,cont2,cont3):  
        print(n,end=" ")
        sleep(.2)
    print("Fim!")   
contador(1,10,1)
contador(10,0,2)
print("=-"*20)
print("Digite a sequencia desejada: ")
cont1=int(input("Inicio: "))
cont2=int(input("Fim: "))
cont3=int(input("Passo:" ))
contador(cont1,cont2,cont3)