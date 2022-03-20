#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F. Caso esteja errado
#peça a difitaòao novamente ate ter um valor correto.

nome=str(input("Qual o nome da pessoa? ")).upper().strip()
sexo=str(input("Qual o sexo (M/F)? ")).upper().strip()


while sexo!="F" and sexo!="M":
    print("Valor invalido! Tente novamente...")
    sexo=str(input("Qual o sexo (M/F)? ")).upper().strip()

if sexo=="F":
    print("O nome e {} e o sexo e Feminino.".format(nome,sexo))
else:
    print("O nome e {} e o sexo e Masculino.".format(nome,sexo))




   
   

