# Um professor quer sortear um dos seus quatros 
#alunos para apagar o quadro. Faça um programa
#que ajude ele, lendo o nome deles e escrevendo
#o nome do escolhido.

import random
alunos=[]
i=0
while i<4:
    aluno=input("Digite o nome do aluno: ")
    alunos.append(aluno)  
    i+=1

x=random.choice(alunos)

print("O aluno escolhido foi {}".format(x))










