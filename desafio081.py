#Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, #mostre:                                                                                                   #A) Quantos números foram #digitados.                                                                                                #B) A lista de valores, ordenada de forma #decrescente.                                                                                          C) #Se o valor 5 foi digitado e está ou não na lista.


lista=[]

while True:
    numero=int(input("Digite um numero: "))
    lista.append(numero)
    lista.sort(reverse=True)

    continuar=" "

    while continuar not in "SN":
        continuar=str(input("Quer continuar [s/n]? ")).strip().upper()[0]
    if continuar=="N":
        break

#if 5 in lista:
#        print("\nO numero 5 foi digitado na lista.")
#else:
#        print("\nO numero 5 nao foi digitado na lista.")

print(f"\nForam digitados {len(lista)} elementos.")
print(f"\nA lista em ordem decrescente é: {lista}")
print("O numero 5 foi digitado na lista." if 5 in lista else "O numero 5 nao foi digitado na lista.")