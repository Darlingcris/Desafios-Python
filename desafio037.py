
#Escreva um programa que eleia um numero inteiro
#qualquer e peça para o usuario escolher
#qual serà a base de conversao:
#1 para binario
#2 para octal
#3 para hexadecimal

numero=int(input("Digite um numero inteiro: "))
baseNumerica=int(input("""Qual a base numerica que voce deseja fazer a conversao? 
Digite: 1 para Binario, 
        2 para Octal, 
        3 para Hexadecimal: """))

    
if baseNumerica==1:
        print("O numero {} convertido em Binario e: {}".format(numero,bin(numero)[2:]))
elif baseNumerica==2:
        print("O numero {} convertido em Octal e: {}".format(numero,oct(numero)[2:]))
elif baseNumerica==3:
        print("O numero {} convertido em Hexadecimal e: {}".format(numero,hex(numero)[2:]))
else:
        print("Numero invalido! Tente novamente.")
     
     
     


         

