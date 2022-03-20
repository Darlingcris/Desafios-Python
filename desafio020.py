#O mesmo professor do desfio anterior que sortear
#a ordem de apresentaòao de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

import random
alunos=[]
i=0
while i<4:
    aluno=input("Digite o nome do aluno: ")
    alunos.append(aluno)   
    i+=1

x=random.sample(alunos,4)
print("A sequencia para apresentaçao dos trabalhos e: {}".format(x))


