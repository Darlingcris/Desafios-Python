#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

x=int(input("Digite um numero: "))
d=x*2
t=x*3
r=x**(1/2)
print("O dobro do numero {} e {}, \nO seu triplo e {} \nA sua raiz quadrada e {:.2f}.\n".format(x,d,t,r))


x=int(input("Digite um numero: "))
print("O dobro do numero {} e {}, \nO seu triplo e {} \nA sua raiz quadrada e {:.2f}.\n".format(x,x*2,x*3,x**(1/2)))

 #x**(1/2) = pow(x,(1/2))

x=int(input("Digite um numero: "))
print("O dobro do numero {} e {}, \nO seu triplo e {} \nA sua raiz quadrada e {:.2f}.\n".format(x,x*2,x*3,pow(x,(1/2))))