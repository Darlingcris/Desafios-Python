#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros
#elementos de uma sequencia de Fibonacci.

numero=int(input("Digite quantos termos voce quer: "))

t1=0
t2=1
print("{} -> {} ->".format(t1,t2),end=" ")
t3=t1+t2   
contador=3
while contador<=numero:
       t3=t1+t2
       print("{} ->".format(t3),end=" ")
       t1=t2
       t2=t3
       contador+=1
print(" FIM")

numero=int(input("digite o termo que voce quer ver: "))
t1=0
t2=1
print("{} -> {} ->".format(t1,t2),end=" ")
t3=t1+t2
contador=3
while contador<=numero:
       t3=t1+t2
       print("{} ->".format(t3),end=" ")
       t1=t2
       t2=t3
       contador+=1
print("Fim")
  



