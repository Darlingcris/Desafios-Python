#desenvolva um programa que leia o primeiro
#termo e a razao de uma PA. No final, Mostre
#os 10 primeiro termos dessa progressao.
#OBS: PA= (1,100,10) o primeiro n=1 a razao=10


primeiroTermo=int(input("Digite o primeiro termo da sua PA: "))
razao=int(input("Digite a razao da sua PA: "))
pa=int(input("Qual a posiçao voce quer encontrar? "))
posicao=primeiroTermo+(pa-1)*razao
print(posicao)
   

print("="*45)
print("{:^45}".format("10 termos de uma PA"))
print("="*45)
primeiroTermo=int(input("\nDigite o primeiro termo da sua PA: "))
razao=int(input("Digite a razao da sua PA: "))
for pa in range(1,11):
    posicao=primeiroTermo+(pa-1)*razao
    print(posicao, end=" → ")
print("Fim")


print("="*45)
print("{:^45}".format("10 termos de uma PA"))
print("="*45)
primeiroTermo=int(input("\nDigite o primeiro termo da sua PA: "))
razao=int(input("Digite a razao da sua PA: "))
decimo=primeiroTermo+(11-1)*razao
for pa in range(primeiroTermo,decimo,razao):    
    print(pa, end=" → ")
print("Fim")