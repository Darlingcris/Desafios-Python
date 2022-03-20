#crie um programa que leia uma frase e diga 
#se ela e uma Palindromo (frase pode ser lida
# de tras pra frente ou vice versa significa
# a mesma coisa) desconsiderando os espaços.


frase=str(input("Digite uma frase para saber se e um Palindromo: ")).upper().strip()
palavras=frase.split()
junto="".join(palavras)
inverso=""
for x in range(len(junto)-1,-1,-1): 
    inverso+=junto[x]
if junto==inverso:
    print("A frase forma um PALINDROMO!")
else:
    print("A frase NAO forma um palindromo!")

frase=str(input("Digite uma frase para saber se e um Palindromo: ")).upper().strip().replace(" ","")
inverso=""

for x in range(len(frase)-1,-1,-1):
    inverso+=frase[x]
if frase==inverso:
    print("A frase forma um PALINDROMO!")
else:
    print("A frase NAO forma um palindromo!")

frase=str(input("Digite uma frase para saber se e um Palindromo: ")).upper().strip().replace(" ","")
inverso=frase[::-1]

if frase==inverso:
     print("A frase forma um PALINDROMO!")
else:
    print("A frase NAO forma um palindromo!")

    
   





