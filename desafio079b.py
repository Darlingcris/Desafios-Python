#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o #número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos #digitados, em ordem crescente.


valores=[]

while True:
    
    digitado=(int(input("Digite o valor: ")))
       
    if digitado in valores:
            del digitado
            print("Valor ja existente! Nao sera adicionado...")
    else:
            valores.append(digitado)

    resposta=" "

    while resposta not in "sn":
        resposta=str(input("Quer continuar [S/N]? ")).strip().lower()[0]
    if resposta=="n":
        break

valores.sort()
print("=-"*15)
print()
print(f"A sua lista é composta: {valores}")
print()
print("=-"*15)