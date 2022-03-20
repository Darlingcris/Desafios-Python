#crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario 
#digitar o valor 999. que e a condiçao de parada. No final, mostre quantos numeros foram digitados
#e qual foi a soma entre eles(desconsiderando o Flag(999))

numero=0
soma=0
contador=0

while numero!=999:
    numero=int(input("Digite um numero inteiro [999 para parar]: "))
    if numero!=999:
        soma+=numero
        contador+=1
    else:
        print("\nO programa foi finalizado.",end=" ")    
    
print("Foram digitados um total de {} numeros e a soma entre eles e {}.".format(contador,soma))