#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar #o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a #soma entre elas (desconsiderando o flag).


soma=contador=0

while True:
    numero=int(input("Digite um numero: (Digite 999 para finalizar!) "))
    if numero==999:
        break
    soma+=numero
    contador+=1
print(f"Foram digitados {contador} numeros. A soma entre os numeros digitados é {soma}.")