#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o #número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos #digitados, em ordem crescente.



numeros=list()

for n in range(1,6):
    listagem=int(input(f"Digite o {n}° numero: "))
    
    if len(numeros)==0 or numeros[-1]<listagem:
        numeros.append(listagem)
    else: 
        for i in range(len(numeros)):
            if listagem<numeros[i]:
                numeros.insert(i,listagem)
                break

print(numeros)