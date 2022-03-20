#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário #vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.


adicionar="S"
eproduto=" "
menor=contador=maisdemil=valorfinal=0
print("-="*10)
print("{:^20}".format("LOJAS MADJÀ"))
print("-="*10)
while True:    
    produto=str(input("Produto: ")).capitalize().strip()
    preco=float(input("Preço: R$ "))
    valorfinal+=preco
    contador+=1
   
    if preco>1000:
        maisdemil+=1

    if contador==1 or preco<menor:
            menor=preco
            eproduto=produto
    

    print(".."*10)
    adicionar=str(input("Adicionar [S/N]? ")).capitalize().strip()[0]

    while adicionar!="S" and adicionar!="N":
        print("\033[1;31mDigito invalido.\033[m") 
        adicionar= str(input("Adicionar [S/N]? ")).capitalize().strip()[0]
    print(".."*10)

    if adicionar=="N":
        break

print("=-"*20)
print(f"Valor total das compras: R$ {valorfinal:.2f}\nExistem {maisdemil} produtos que custam mais de mil reais.\nProduto mais economico: {eproduto}. Valor: R$ {menor}.\n\033[1;32mPrograma finalizado com sucesso!\033[m")