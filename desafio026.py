#crie um programa que leia uma frase qualquer e mostre:
#Quantas vezes aparece a letra A
#Em que posiçao ela aparece a primeira vez
#Em que posiçao aparece a ultima vez


frase=str(input("Digite uma frase: ")).lower().strip()
print("\nNa frase existe(m) {} letra(s) \"A\".".format(frase.lower().count("a")))
print("\nA primeira posicao da letra \"A\" se encontra na casa {}.".format(frase.find("a")+1))
print("\nA ultima posicao da letra \"A\" se encontra na casa {}.".format(frase.rfind("a")+1))