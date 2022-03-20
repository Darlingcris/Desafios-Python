#desenvolva um programa que leia o nome, idade
#e sexo de 4 pessoas. No final do programa, mostre:
#a media de idade do grupo
#qual e o nome do Homem mais velho
#quantas mulheres tem menos de 20 anos



M=" "
F=" "
maior=0
mulherMenor=0
soma=0
nomevelho=" "
for dados in range(1,5):
    print("----{}° Pessoa----".format(dados))
    nome=str(input("Nome: ")).strip().upper()
    sexo=str(input("Sexo [M/F]: ")).upper()
    idade=int(input("Idade: "))

    soma+=idade
    idadeMedia=soma/4
    
    if idade==1  and sexo in "M":
        maior=idade
        nomevelho=nome
    if sexo in "M" and idade>maior:
        maior=idade
        nomevelho=nome
    if sexo in "F" and idade<20:
        mulherMenor+=1
print("\nA idade media do grupo e {}.".format(idadeMedia))
print("O homem mais velho tem {} e se chama {}.".format(maior,nomevelho))
print("Existem {} mulhere(s) com menos de 20 anos.".format(mulherMenor))