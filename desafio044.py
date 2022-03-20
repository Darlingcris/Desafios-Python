print("\n{:=^100}".format(" LOJA DA CRYS "))
valorProduto=float(input("\nDigite o valor do produto: "))
pagamento=int(input("""\nQual sera a forma de pagamento. Digite a opçao desejada: 
\n1 - para pagamento em dinheiro ou cheque: \n2 - para pagamento com Cartao modalidade Debito:
3 - para pagamento em Duas vezes no Cartao: \n4 - para pagamento em Tres ou mais vezes no cartao:"""))

#while pagamento<1 or pagamento>4:
#    pagamento=int(input("""\nNumero INVALIDO!!! Tente novamente! \nQual sera a forma de pagamento. Digite a opçao desejada: 
#\n1 - para pagamento em dinheiro ou cheque: \n2 - para pagamento com Cartao modalidade Debito:
#3 - para pagamento em Duas vezes no Cartao: \n4 - para pagamento em Tres ou mais vezes no cartao:""")))

if pagamento==1:
    print("\nO produto tera \"10%\" de desconto. Saindo pelo valor de R${:.2f}.".format(valorProduto-((10*valorProduto)/100)))
elif pagamento==2:
    print("\nO produto tera \"5%\" de desconto. Saindo pelo valor de R${:.2f}.".format(valorProduto-((5*valorProduto)/100)))
elif pagamento==3:  
    print("\nO produto tera NAO tera desconto.Suas parcelas serao de 2x de R${}".format(valorProduto/2))
elif pagamento==4:
    parcelas=int(input("\nEm quantas parcelas deseja pagar? "))
    valorProduto=valorProduto+(20*valorProduto)/100
    print("\nO produto tera \"20%\" de acrescimo, o valor total sera de R${:.2f}.".format(valorProduto))
    print("Serao {} parcelas de R${:.2f} cada.".format(parcelas,valorProduto/parcelas))
else:
    pagamento=0
    print("\nOPçAO INVALIDA! TENTE NOVAMENTE!!!")
print("\nBoas compras!")


#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento.
#a vista dinherio/cheque: 10% de desconto a vista no cartao:5% de desconto em ate 2x no cartao preço normal
#3x ou mais no cartao: 20% de juros.