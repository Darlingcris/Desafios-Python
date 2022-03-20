# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado. 

k=float(input("Quantos Km o condutor percorreu? "))
d=int(input("O carro foi alugado por quantos dias? "))
v=(0.15*k) + (60*d)
print("\nO valor a ser pago sera de R${:.2f}.\n".format(v))