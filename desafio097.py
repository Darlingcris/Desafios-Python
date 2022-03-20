#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e #mostre uma mensagem com tamanho adaptável. 



def escreva(msg):
    t=len(msg) + 4
    print('-'*t)
    print(f'  {msg}')
    print('-'*t)
          
#programa principal

escreva(str(input("Escreva o texto: ")).strip().title())