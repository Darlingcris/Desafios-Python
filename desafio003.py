#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo,
# e todas as informaçoes possiveis sobre ele.

x=input("Digite o seu sonho: ")
print("O tipo primitivo desse valor e: ",type(x))
print("O tamanho do texto: ",len(x))
print("Os caracteres repetidos \"A\" sao: ",x.count("a"))
print("A letra esta na posicao: ",x.find("e"))
print("Coloque todas as letras em maiusculo: ",x.upper())
print("Coloque todas as letras em minusculo: ",x.lower())
print("Coloque somente a primeira maiuscula: ",x.lower().capitalize())
print("Coloque a primeira letra de cada palavra em maiusculo: ",x.title())
print("As letras maiuscula se tornam minusculas e vice-versa: ",x.swapcase())
print("Verifica se as letras sao todas maiusculas:",x.isupper())
print("Verifique se as letras sao todas minusculas: ",x.islower())
print("Verifique se cada palavra se inicia com a letra maiuscula: ",x.istitle())
print("Verifique se existem letras e numeros: ",x.isalnum())
print("Verifique se possuem apenas letras: ",x.isalpha())
print("Verifique se tem apenas numeros: ",x.isdigit())

x=input("Digite o numero: ")
print(type(x))

x=8
print(type(x))