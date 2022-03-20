#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


idade=maior=menor=Tidade=homens=mulheres=dezoito=0
sexo=" "
continuar="S"
print("~~"*20)
print("{:^38}".format("CADASTRO"))

while continuar=="S":
    print("-="*20)
    
    idade=int(input("Idade? "))
    sexo=str(input("Sexo [F/M]? ")).upper()[0]
    Tidade+=1
    
    while sexo not in "FM":
        print("\033[1;31mDigito invalido!\033[m")
        sexo=str(input("Sexo [F/M]? ")).upper()[0]

    print("=-"*20)
    continuar=str(input("Deseja inserir mais dados[S/N]? ")).upper()[0]
    while continuar not in "SN":
        print("\033[1;31mNumero invalido!\033[m")
        continuar=str(input("Deseja inserir mais dados[S/N]? ")).upper()[0]
    
    if Tidade==1:
        maior=menor=idade
    else:
        if idade>maior:
            maior=idade

        if idade<menor:
            menor=idade

    if idade>18:
            dezoito+=1

    if sexo=="M":
        homens+=1

    if sexo=="F":
        if idade<20:
            mulheres+=1
print("=="*20)
print(f"A pessoa com a maior idade tem {maior} anos e com a menor idade tem {menor} anos.")
print(f"Foram cadastradas {dezoito} pessoas maior(es) de dezoito anos.")
print(f"Foram cadastrado(s) {homens} homem(s).")
print(f"Foram cadastrada(s) {mulheres} mulher(es) menor(es) de 20 anos.")