#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras tem ao todo sem considerar os espaços
#quantas letras tem o primeiro nome

nome=str(input("Digite o seu nome completo: ")).strip()
print("\nSeu nome em maiusculo: ",nome.upper())
print("\nSeu nome em minusculo: ",nome.lower())
print("\nA quantidade de caracteres do seu nome e: ",len(nome.replace(" ","")))
nome=nome.split()
print("\nA quantidade de caracteres do seu primeiro nome e: ",len(nome[0]))


nome=str(input("\nDigite o seu nome completo: ")).strip()
print("\nO seu nome em maiusculo e: {}".format(nome.upper()))
print("\nO seu nome em minusculo e: {}".format(nome.lower()))
print("\nO seu nome tem {} letras.".format(len(nome)-nome.count(" ")))
nome=nome.split()
print("\nO seu primeiro nome e {} e tem {} caracteres.".format(nome[0],len(nome[0])))

nome=str(input("\nDigite o seu nome completo: ")).strip()
nome.find(" ")
print("\nO seu primeiro nome tem {} caracteres.".format(nome.find(" ")))