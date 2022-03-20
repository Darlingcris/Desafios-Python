#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo #usuário. O programa será interrompido quando o número solicitado for negativo.


resultado=0
contador=1
while True:
    numero=int(input("Quer ver a Tabuada de qual numero? (Digite um numero negativo para finalizar.) "))
    if numero < 0:
        break
    print("~"*15)
    print(f"TABUADA DO {numero}")
    print("~"*15)
    contador=1
    while contador<=10:
        resultado=numero*contador
        print(f"{numero} x {contador:2} = {resultado}")
        contador+=1
    print("="*15)
print("Programa finalizado com sucesso!")