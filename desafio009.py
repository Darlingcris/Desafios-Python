# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.



x=int(input("Digite um numero inteiro para criar a sua tabuada: ")) 
n=0
while n<=10:
    t =x*n
    print("{} x {} = {} \n".format(x,n,t))
    n=n+1
print("Fim do programa.")    
    