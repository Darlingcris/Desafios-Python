#faça um programa que leia o peso de cinco
#pessoas. No final, mostre qual foi o maior
#e o menor peso lido.




#peso=float(input("Digite o peso da pessoa: Kg "))
#peso2=float(input("Digite o peso da segunda pessoa: Kg "))

#if peso>peso2:
#    print("O maior peso digitado e {:.2f}".format(peso))
#else:
#    print("O maior peso digitado e {:.2f}".format(peso2))
    
maior=0
menor=0
for p in range(1,6):
    peso=float(input("Digite o peso da {}° pessoa: kg ".format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print("O maior peso inserido foi de {:.2f}Kg".format(maior))
print("O menor peso inserido foi de {:.2f}Kg".format(menor))

       

   
   