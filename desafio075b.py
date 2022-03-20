# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


valores=tuple(int(input("Digite um numero: ")) for n in range(1,5))

print(f"Os valores digitados foram: {valores}")
print(f"O numero Nove (9) apareceu {valores.count(9)} vez(es).")

tres=valores.count(3)

if tres==1:
    print(f"O numero Tres (3) foi digitado na {valores.index(3)+1}° casa.")
else:
    print("O numero Tres (3) nao foi digitado.")

print(f"Os valores pares digitados sao: ",end=" ")

for n in valores:
    if n%2==0:
        print(n, end="  ")