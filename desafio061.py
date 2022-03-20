#refaça o desafio 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10
#primeiro termos da progressao usando a estrutura while.
#desenvolva um programa que leia o primeiro
#termo e a razao de uma PA. No final, Mostre
#os 10 primeiro termos dessa progressao.
#OBS: PA= (1,100,10) o primeiro n=1 a razao=10

primeiroTermo=int(input("Digite o primeiro termo da sua PA: "))
razao=int(input("Digite a razao da PA: "))
for pa in range(1,11): 
    posicao=primeiroTermo+(pa-1)*razao
    print("{} ->".format(posicao),end=" ")
print("Fim")

primeiroTermo=int(input("Digite o primeiro termo da sua PA: "))
razao=int(input("Digite a razao da PA: "))
pa=primeiroTermo
contador=1
while contador<=10:
      print("{} ->".format(pa),end=" ")    
      pa+=razao
      contador+=1
print("Fim")