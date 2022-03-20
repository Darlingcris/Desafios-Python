#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior #e o menor valor digitado e as suas respectivas posições na lista.


numeros=[]
maior=menor=0

for n in range(1,6):
    entrada=int(input(f"Digite o {n}° valor: "))
    numeros.append(entrada)

    if n==1:
        maior=menor=entrada
    else:
        if entrada>maior:
            maior=entrada
                
        if entrada<menor:
            menor=entrada


print(f"\nLista: {numeros}")       
print(f"O maior valor digitado foi {maior}, nas posiçoes:",end=" ")

for i,n in enumerate(numeros):
    if n==maior:
        print(f"{i+1}...",end=" ") 

print(f"\nO menor valor digitado foi {menor}, nas posicoes:",end=" ")

for i,n in enumerate(numeros):
    if n==menor:
        print(f"{i+1}...",end=" ")