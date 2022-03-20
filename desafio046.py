#faça um programa que mostre na ela uma contagem regressiva 
#para o estouro de fogos de artificios, indo de 10 ate 0,
# com uma pausa de um segundo entre eles.


from time import sleep
for contagem in range(10,-1,-1):
    sleep(1)
    print("...")
    print(contagem)
    
print("{:#^50}".format(" FELIZ ANO NOVO!!! "))
  
