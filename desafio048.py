#Faça um programa que calcule a soma entre
#todos os numeros impares que sao multiplos
#de tres e que se encontram no intervalo
#de 1 ate 500.


#for numero in range (1,501):
#    if numero%3==0:
#        print(numero)
   

soma=0
contador=0
for numero in range(3,501,3):
    if numero%2!=0:
        print(numero, end=" ")
        soma+=numero
        contador+=1
print("\nA somatoria dos {} valores e: {}".format(contador,soma))

soma=0
contador=0
for numero in range(1,501,2):
    if numero%3==0:
        print(numero, end=" ")
        soma+=numero
        contador+=1
print("\nA somatoria dos {} valores e: {}".format(contador,soma))
