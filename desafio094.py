#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um #dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) #A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.



dados=dict()
juntos=list()
idade=0
while True:
    dados['Nome']=str(input("Nome: ")).strip().title()
    dados['Sexo']=str(input("Sexo [M/F]: ")).strip().upper()[0]
    while dados['Sexo'] not in 'FM':
        dados['Sexo']=str(input("\033[1;31mOpcao invalida!\033[m.Digite o sexo [M/F]: ")).strip().upper()[0]
    dados['Idade']=int(input("Idade:"))
    juntos.append(dados.copy())
    idade+=dados['Idade']
    cont=str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    while cont not in'SN':
        cont=str(input("\033[1;31mOpcao invalida!\033[m. Quer continuar [S/N]: ")).strip().upper()[0]
    if cont=='N':
        break      
print('=-'*40)
print(juntos)
print('=-'*40)
print(f"Cadastros: {len(juntos)} pessoas.")
print("-"*40)
print(f"Media do grupo: {idade/len(juntos):.2f}.")
print("-"*40)
print(f"Mulheres cadastradas:", end=" ")
for dados in juntos:
    if dados['Sexo']=='F': 
        print(f"{dados['Nome']}",end=" ; ")
print()
print("-"*40)
print("\nPessoas acima da media de idade:")
for dados in juntos:
    if dados['Idade']>idade/len(juntos):
        for k,v in dados.items():
            print(f"{k:<5}={v}",end=" ")
        print()
print("=-"*20)