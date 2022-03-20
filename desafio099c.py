#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


#exercicio 99 com def() sem usar listas:   

from time import sleep
def maior(*num): 
    print("=-"*15)   
    print("Analisando os valores passados...")
    sleep(2)
    print(f"Os valores foram: {num}")
    print(f"Foram informados {len(num)} valores.")
    print(f"O maior valor foi {max(num)}.")
    

maior(3,5,7,2,8,9)
maior(0)
maior(3,6)
maior(9,2,4,8,30)
maior(15,25,20,0)
maior(1,3,9,0)