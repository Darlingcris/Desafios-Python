#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. #No final, mostre uma listagem de preços, organizando os dados em forma tabular.



lista=("caneta",1.50,"caderno",10.00,"leite",2.30,"pao",5.00,"cha",210.00,"arroz",340.00 )
for n in range(0,len(lista),2):
    print(f"{lista[n]:-<10}R$ {lista[n+1]}") 
    