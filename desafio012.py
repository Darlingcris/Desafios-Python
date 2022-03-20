#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

x=float(input("Qual o preço do produto?R$ "))
d=x*5/100
print("\nO desconto sera de R${:.2f}, e o preco final do produto e de R${:.2f}.\n".format(d,x-d))

x=float(input("Qual o preço do produto?R$ "))
d=x*5/100
p=x*8/100
print("\nPara pagamento a vista o produto tem desconto de R${:.2f}, sainda pelo valor de R${:.2f}".format(d,x-d))
print("\nPara o pagamento a prazo o produto tera um aumento de R${:.2f}, e o preco final sera de R${:.2f}.\n".format(p,x+p))