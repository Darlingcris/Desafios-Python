#faça um programa que leia um numero de 0 a 9999 e mostre na tela
#cada um dos digitos separados(unidade, dezena, centena, milhar)

num=int(input("Entre com um numero: "))
m=num // 1000 % 10
c=num // 100 % 10
d=num // 10 % 10
u=num // 1 % 10
print("\nO seu numero tem {} milhar(es).".format(m))
print("O seu numero tem {} centena(s).".format(c))
print("O seu numero tem {} dezena(s).".format(d))
print("O seu numero tem {} unidade(s).".format(u))

