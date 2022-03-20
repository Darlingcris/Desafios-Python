#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No #final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de #cada aluno individualmente.


media=0
lista=list()
nomes=list()
notas=list()

while True:
    
    nome=str(input("Nome: "))
    nomes.append(nome)
    nota1=float(input("Nota1: "))
    nota2=float(input("Nota2: "))
    media=nota1+nota2/2
    notas.append(nota1)
    notas.append(nota2)
    nomes.append(notas[:])
    lista.append(nomes[:])
    nomes.clear()
    notas.clear()
    resp=" "
    while resp not in"sn":
        resp=str(input("Quer continuar [s/n]? ")).lower()[0]
    if resp in "n":
        break

print("~~"*20)
print(lista)




























