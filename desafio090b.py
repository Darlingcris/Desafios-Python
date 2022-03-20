#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No #final, mostre o conteúdo da estrutura na tela.


lista=dict()   

lista['Nome']=str(input("Nome do Aluno:")).strip().title()
lista['Media']=float(input(f"Média de {lista['Nome']} é: "))


if lista['Media']>=7:
    lista['Situaçao']='Aprovado'
elif 5<lista['Media']<7:
    lista['Situaçao']='Recuperaçao'
else:
    lista['Situaçao']='Reprovado'

for k,v in lista.items():
    print(f'{k} é igual a {v}.')