#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um #dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação #e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import date   
ano=date.today().year        

cadastro={}

cadastro['Nome']=str(input("Nome: ")).strip().title()
nascimento=int(input("Ano de Nascimento (4 digitos): "))
cadastro['Idade']=ano-nascimento
cadastro['CTPS']=int(input("Carteira de Trabalho (0 se nao possui): "))

if cadastro['CTPS']!=0:
    contrato=int(input("Ano de contrataçao: "))
    cadastro['Ano do contrato']=contrato
    cadastro['Salario']=float(input("Salario:R$ "))
    cadastro['Aposentadoria']=(contrato+35)-nascimento 
     #cadastro['Aposentadoria']=cadastro['Idade']+((cadastro['Ano de contrataçao']+35)-ano)
print()
print("=-"*17)
for k,v in cadastro.items():
    print(f"{k:<15}: {v:>15}")
print("=-"*17)