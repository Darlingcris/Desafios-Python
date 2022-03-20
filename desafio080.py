#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na #posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista=[]

for i in range(0,5):
    numeros= int(input(f"Digite o {i}° numero: "))
    
    if i==0 or numeros>lista[-1]:
        lista.append(numeros)
        print(f"Numero adicionado na ultima posiçao...")
    else:
       cont=0
       while cont<len(lista):
            if numeros<=lista[cont]:
                lista.insert(cont,numeros)
                print(f"Valor adicionado na posiçao {cont} da lista... ")
                break
            cont+=1
    
print(lista)