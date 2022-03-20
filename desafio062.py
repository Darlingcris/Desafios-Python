#desenvolva um programa que leia o primeiro
#termo e a razao de uma PA. No final, Mostre
#os 10 primeiro termos dessa progressao.
#OBS: PA= (1,100,10) o primeiro n=1 a razao=10

#melhore o desafio 61, peguntado para o usuario se ele quer mostrar mais alguns termos. 
#o rograma encerra quando ele disser que quer mostrar OS TEMOS.

primeiroTermo=int(input("Digite o primeiro numero da sua PA: "))
razao=int(input("Digite a razao da sua PA: "))

pa=primeiroTermo
total=0
mais=10
contador=1

while mais!=0:
    total=total+mais
    while contador<=total:
        print("{} ->".format(pa),end=" ")
        pa+=razao
        contador+=1
    print("Pausa")
    mais=int(input("\nVoce quer ver mais quantos termos? "))
print("Programa finalizado!")



    