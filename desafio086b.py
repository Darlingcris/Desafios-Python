#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No #final, mostre a matriz na tela, com a formatação correta.



matriz=[[],[],[]]

for n in range(0,3):
    valor=int(input(f"Digite um valor para [0,{n}]: "))
    matriz[0].append(valor)

for n in range(0,3):
    valor=int(input(f"Digite um valor para [1,{n}]: "))
    matriz[1].append(valor)

for n in range(0,3):
    valor=int(input(f"Digite um valor para [2,{n}]: "))
    matriz[2].append(valor)
   
print(f"{matriz[0]}")
print(f"{matriz[1]}")
print(f"{matriz[2]}")
