#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No #final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de #cada aluno individualmente.


media=total=0
lista=list()
c=-1
while True:    
    nome=str(input("Nome: ")).strip().title()
    nota1=float(input("Nota1: "))
    nota2=float(input("Nota2: "))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    resp=" "
    while resp not in"sn":
        resp=str(input("Quer continuar [s/n]? ")).lower()[0]
    if resp in "n":
        break
    total+=1
print()
print("~~"*20)
print(f'{"N°":<4}{"Nome":<15}{"Média":>4}')
print("~~"*20)
for i,n in enumerate(range(0,total+1)):
    print(f"{i+1:<1}° {lista[n][0]:<15} {lista[n][2]:>4.2f}")
    print("--"*20)
while c!= 999:
        c=int(input("Quer ver a nota de qual aluno (999 finaliza): "))
        for i,n in enumerate(range(0,total+1)):
            if c==i+1:
                print(f"Notas do(a) aluno(a) {lista[n][0]}: {lista[n][1]}") 
        print("**"*20)