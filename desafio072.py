#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até #vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


valor=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezesete","dezoito","dezenove","vinte")
while True:
    numero=int(input("Digite um numero entre 0 e 20: ")) 
    while numero<0 or numero>20:
        print("\033[1;31mValor invalido!\033[m")
        numero=int(input("Digite um numero entre 0 e 20: "))
    print(f"Voce digitou o numero {valor[numero]}")
    resposta=" "    
    while resposta not in "SN":
        resposta=str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if resposta=="N":
        break
print("Programa Finalizado!")