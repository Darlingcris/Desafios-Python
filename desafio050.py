#desenvolva um programa que leia seis numeros
#inteiro e mostre a soma apenas daqueles que 
#forem pares. Se o valor digitado for impar,
#descondidere-o.

s=0
contador=0
for n in range (1,7):
    numeros=(int(input("\nDigite o {}° numero: ".format(n))))
    if numeros%2==0:
        s+=numeros
        contador+=1
print("\nVoce me informou {} numero(s) par(es) e a somatoria e: {}.".format(contador,s))
