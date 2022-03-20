#crie um programa que mostre na tela todos 
#os numeros pares que estao no intervalo
#entre 1 e 50.

for numeros in range (1+1,51,2):
    #print(".")                  #melhor soluçao :)
    print(numeros)
print("\nFim do Programa\n")


for numeros in range(1,51):
    #print(".")              #saber quantas vezes foi feito o Laço
    if numeros%2==0:
       
       print(numeros)
print("\nFim do Programa\n")