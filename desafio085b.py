#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que #mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem #crescente.



numeros=[]
par=[]
impar=[]

for c in range(1,8):
    numeros.append(int(input(f"Digite o {c}° numero: ")))
    
    for n in numeros:
    
        if n%2==0:
            par.append(n)
            par.sort()
        else:
            impar.append(n)
            impar.sort()

    numeros.clear()

print(f"Os numeros pares digitados foram: {par}")
print(f"Os numeros primos digitados foram: {impar}")