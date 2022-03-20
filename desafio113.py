#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de #um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(n):
    while True:
        try:
            valor=int(input(n))

        except (KeyboardInterrupt):
            print('O usuario preferiu nao informar os dados.')
            exit()

        except:
            print("\033[1;33mError...\033[m")
            print("Por favor, digite um valor inteiro: ")
            continue
        
        else:
            return valor

def leiaFloat(n):
    while True:
        try:
            v=float(input(n))
        except:
            print("\033[1;34mErro...\033[mPor favor, digite um numero real: ")
            continue
        else:
            return v

#programa principal       
num=leiaInt('Digite um numero inteiro: ')
n=leiaFloat('Digite um numero real: ')
print(f'O numero inteiro digitado foi {num} e o numero real foi {n}')










    
   

