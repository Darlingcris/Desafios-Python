#desenvolva um programa que leia o comprimento
#de tres retas e diga ao usuario se elas
#pode ou nao formar um triangulo.

a=float(input("Digite o comprimento da primeira reta: "))
b=float(input("Digite o comprimento da segunda reta: "))
c=float(input("Digite o comprimento da terceira: "))

if a<b+c and b<a+c and c<a+b:
    print("\nE possivel construir um triangulo com essas medidas.")
else:
    print("\nNao e possivel construir um triangulo com essas medidas.")


