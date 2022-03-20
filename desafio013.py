#Faça um algoritimo que leia o salario de um funcionario e mostre o seu novo salario com 15%
#de aumento.

x=float(input("Qual o seu salario?R$ "))
a=x*15/100
print("\nVoce tera um aumento de R${:.2f} sobre o seu salario. Recebendo um valor final de R${:.2f}.\n".format(a,x+a))

