# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


n1=int(input("Digite o 1° valor: "))
n2=int(input("Digite o 2° valor: "))
n3=int(input("Digite o 3° valor: "))
n4=int(input("Digite o 4° valor: "))

valores=(n1,n2,n3,n4)
print(f"Os valores digitados foram: {valores}")

if n1==9 or n2==9 or n3==9 or n4==9:
    print(f"O numero Nove (9) apareceu {valores.count(9)} veze(s).")

if n1==3 or n2==3 or n3==3 or n4==3:
    print(f"O numero Tres (3) foi digitado na {valores.index(3)+1}° casa.")

if n1%2==0 or n2%2==0 or n3%2==0 or n4%2==0:
    print(f"Os numeros pares sao: {valores}")