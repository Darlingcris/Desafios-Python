#crie um programa que leia dois valores e mostre um menu na tela:
#1 somar.
#2 multiplicar
#3 maior
#4 novos numeros
#5 sair do programa
#seu programa devera realizar a operaçao solicitada em cada caso.

from time import sleep
numero1=float(input("\nDigite o primeiro valor: "))
numero2=float(input("Digite o segundo valor: "))
operacao=0
while operacao!=7: 
    print("\n{:-^60}".format("Qual a operacao voce quer realizar?"))
    operacao=int(input("""\n[1] Somar \n[2] Subtrair \n[3] Multiplicar \n[4] Dividir 
[5] Maior numero \n[6] Novos numeros \n[7] Sair: """)) 
    while operacao<1 or operacao>7:
        operacao=int(input("""\nNumero Invalido. Digite: \n[1] Somar \n[2] Subtrair \n[3] Multiplicar
[4] Dividir \n[5] Maior numero \n[6] Novos numeros \n[7] Sair: """))
    if operacao==1:
        print("\nA somatoria e {} + {} = {}".format(numero1,numero2,numero1+numero2))        
    elif operacao==2:
        print("\nA subtracao e {} - {} = {}".format(numero1,numero2,numero1-numero2))        
    elif operacao==3:
        print("\nA multiplicacao e {} * {} = {}".format(numero1,numero2,numero1*numero2))       
    elif operacao==4:
        print("\nA divisao e {} / {} = {}".format(numero1,numero2,numero1/numero2))       
    elif operacao==5:
            if numero1>numero2:
                print("\nO maior numero digitado entre {} e {} e o numero {}".format(numero1,numero2,numero1))
            else:
                print("\nO maior numero digitado entre {} e {} e o numero {}".format(numero1,numero2,numero2))            
    elif operacao==6:
        numero1=float(input("\nDigite o primeiro valor: "))
        numero2=float(input("Digite o segundo valor: "))    
    else:
        print("\nFinalizando...")
        sleep(1)
        print("\nProgama finalizado com sucesso!")

