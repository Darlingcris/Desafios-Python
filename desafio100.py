#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A #primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a #soma entre todos os valores pares sorteados pela função anterior.


from random import randint
from time import sleep

def sorteio():  #o professor colocou sorteio(lista), mas funcionou sem eu colocar. 
    print(f"Sorteando os cinco numeros da lista: ", end=" ")
    for n in range(0,5):
        sort=randint(1,10)
        print(sort, end=" ")
        sleep(.4)
        lista.append(sort)
def somapar():    
    soma=0    
    for num in lista: 
        if num%2==0:
            soma+=num
    print(f"\nA somatoria dos numeros pares da lista {lista} é: {soma}")
lista=[]
sorteio()
somapar()