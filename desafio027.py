#Faça um programa que peça o nome completo de uma pessoa
#mostrando em seguida o primeiro e o ultimo nome separadamente.

n=str(input("\nQual o seu nome? ")).upper().strip().split()
print("\nSeu primeiro nome e \"{}\".".format(n[0]))
print("\nSeu ultimo nome e \"{}\".".format(n[-1]))


n=str(input("\nQual o seu nome? ")).upper().strip()
print("\nSeu primeiro nome e \"{}\".".format(n.split()[0]))
print("\nSeu ultimo nome e \"{}\".".format(n.split()[-1]))
 