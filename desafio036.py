
#Escreva um programa para aprovar o emprestimo
#bancario para a compra de uma casa.
#O programa vai perguntar o valor da casa,
#o salario do comprador e em quantos anos ele
#vai pagar.
#Calcule o valor da prestacao mensal, sabendo
#que ela nao pode exceder 30% do salario
#ou entao o emprestimo sera negado.


pv=float(input("Qual o valor da casa? R$ "))
s=float(input("Qual e o salario do comprador? R$ "))
n=int(input("Em quantas parcelas mensais o comprador deseja pagar? "))
i=float(input("Qual a taxa de juros do Banco? % "))

prest=pv*((1+i/100)**n*(i/100)/((1+i/100)**n-1))
apr=s*(30/100)

if prest<=apr:
    print("\nCredito Aprovado!")
    print("\nO valor da prestacao e de R${:.2f} por mes.".format(prest))
else:
    print("\nO valor das parcelas ultrapassa R${} do salario do comprador.".format(apr))
    print("\nO valor da prestacao e de R${:.2f} por mes.".format(prest))
    print("\nCredito Reprovado!")

print("\nFim do programa.")











#e=str(input("O comprador dara entrada? ")

    #if entrada==0:
    #else:


