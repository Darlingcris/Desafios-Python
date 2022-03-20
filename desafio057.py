
#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F. Caso esteja errado
#peça a difitaòao novamente ate ter um valor correto.

sexo=str(input("Digite o sexo [M/F]: ")).upper().strip()

while sexo!="F" and sexo!="M":
    sexo=(str(input("DADO INVALIDO. Digite o sexo [M/F]: "))).upper().strip()

if sexo=="F":
    print("\nSexo Feminino registrado com sucesso!")
else:
    print("\nSexo Masculino registrado com sucesso!")
print("\nPrograma finalizado.")