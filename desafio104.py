#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do #Python, só que fazendo a validação para aceitar apenas um valor numérico. 

def leiaInt(n):
    valor=input(n)    
    if valor.isnumeric():
        return valor
    else:
        valor=input('Digite um numero inteiro: ')
        return leiaInt(n)   
            
num=leiaInt('Digite um numero inteiro: ')
print(f'O numero digitado foi {num}.')