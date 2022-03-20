
#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve #mostrar, para cada palavra, quais são as suas vogais.



texto=("casa","sapato","sonho","vitoria","sorte","juventude","emprego","amor","vitoria","amizade","sorriso","sol")    
for n in texto:
    print(f"\nA palavra '{n}' tem as vogais: ",end=" ")
    for letra in n:
        if letra in "aeiou":
            print(f"{letra}", end=" ")














