#escreva um programa que pergunte o salario de um funcionario
#e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00
#calcule um aumento de 10%. 
#para salarios inferiores ou iguais
#o aumento è de 15%

s=float(input("\nQual o salario que voce recebe? R$ "))
a=(15*s)/100
b=(10*s)/100

if s<=1250:
    print("\nVoce tera de aumento 15%, acrescentando R$ {:.2f} em seu salario. O valor a ser pago sera de R$ {:.2f}.".format(a,s+a))
if s>1250:
    print("\nVoce tera de aumento 10%, acrescentando R$ {:.2f} em seu salario. O valor a ser pago sera de R$ {:.2f}.".format(b,s+b))

s=float(input("\nQual o salario que voce recebe? R$ "))

if s<=1250:
    novo= s + (s*15/100) 
else:
    novo= s + (s*10/100)
print("\nO valor a ser pago sera de R$ {:.2f}.".format(novo))