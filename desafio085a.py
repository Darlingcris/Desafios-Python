#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que #mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem #crescente.


numeros=[[],[]]

for c in range(1,8):
    valores=int(input(f"Digite o {c}° numero: "))
     
    if valores%2==0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
            
    
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros pares digitados foram: {numeros[0]}")
print(f"Os numeros primos digitados foram: {numeros[1]}")