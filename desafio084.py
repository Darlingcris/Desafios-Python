#Faça um programa que leia nome e peso de várias pessoas,                                      guardando #tudo em uma lista. No final, #mostre:                                                                                                   #A) quantas foram cadastradas.                
#B) Uma listagem com as pessoas mais #pesadas.                                                                                                  #C) Uma listagem com as pessoas mais leves.



dados=list()
geral=list()
pesado=leve=0
nome1=nome2=" "
while True:

    print("=-"*15)
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: Kg ")))
    geral.append(dados[:])
    dados.clear()
    print("~~"*15)
    
    continuar=" "
    while continuar not in "SN":
        continuar=str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if continuar=="N":
        break

pesado=leve=geral[0][1]

for p in geral:
    if p[1]>pesado:
        pesado=p[1]
        
    elif p[1]<leve:
          leve=p[1]
          
print(f"Foram cadastradas {len(geral)} pessos.")
print(f"A pessoa mais pesada tem {pesado} kg, de: ",end=" ")
for p in geral:
    if p[1]==pesado:
        print(f"{p[0]} \ ",end=" ")
print()
print(f"A pessoa mais magra pesa {leve} kg, de: ",end=" ")
for p in geral:
    if p[1]==leve:
        print(f"{p[0]} \ ",end=" ")