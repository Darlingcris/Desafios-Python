#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras #que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre #o conteúdo das três listas geradas.


lista=[]
listaP=[]
listaI=[]

while True:
    lista.append(int(input("Digite um numero: ")))
    lista.sort()
    cont=" "
    while cont not in "SN":
        cont=str(input("Quer continuar[s/n]? ")).strip().upper()[0]
    if cont=="N":
        break

for n in lista:
    if n%2==0:
        listaP.append(n)

    else:
        listaI.append(n)

print("=-"*15)
print(f"\nForam digitados: {lista}")
print(f"\nOs numeros pares sao: {listaP}")
print(f"\nOs numeros impares sao: {listaI}")
print("=-"*15)