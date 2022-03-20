#faça um programa que leia um numero inteiro
#e diga se ele e ou nao um numero primo.
#OBS: o numero primo so pode ser dividido
#por um e por ele mesmo, nenhum outro.

numero=int(input("Digite um numero: "))
total=0
for x in range(1,numero+1):
    if  numero%x==0:
        print("\033[36m", end=" ")
        total+=1
    else:
        print("\033[31m",end=" ")
    print("{}".format(x), end=" ")
print("\n\033[mO numero {} foi divisivel {} vezes.".format(numero,total))
if total==2:
    print("E por isso ele E PRIMO!")
else:
    print("E por isso ele NAO E PRIMO!")

    


   


