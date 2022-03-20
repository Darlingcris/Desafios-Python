#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No #final, mostre o conteúdo da estrutura na tela.


lista=dict()

lista['nome']=str(input("Nome do(a) aluno(a): ")).strip().title()
lista['media']=float(input("Media do(a) aluno(a): "))
lista['situaçao']='Aprovado','Recuperaçao','Reprovado'

print(f"O nome é igual a {lista['nome']}")
print(f"A media é igual a {lista['media']}.")

if lista['media']>=7:   
    print(f"A situaçao é igual a {lista['situaçao'][0]}.")
elif 5<lista['media']<7:
    print(f"A situaçao é igual a {lista['situaçao'][1]}.")
else:
    print(f"A situaçao é igual a {lista['situaçao'][2]}.")