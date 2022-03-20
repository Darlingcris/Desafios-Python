#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá #analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


lista=[]
cont=0

lista=input("Digite sua expressao para validar: ")

for n in lista:
    
    if n=="(":        
            cont+=1         
    elif n==")":       
            cont-=1
            if cont < 0: 
                break

if cont==0:
    print("Expressao validada com sucesso!")
else:
    print("\033[1;31mExpressao invalida!\033[m")