
#Desenvolva uma logica que leia o peso
#e a altura de uma pessoa, calcule seu
#IMC e mostre seu status de acordo com
#a tabela abaixo:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: Peso ideal
#25 ate 30: Sobrepeso
#30 a 40: Obesidade
#acima de 40: obesidade morbida


idade=int(input("Quantos anos voce tem: "))
altura=float(input("Digite a sua altura: (m) "))
peso=float(input("Digite o seu peso: (kg) "))
imc=peso/(altura**2)

print("\nA sua idade e {} e o seu Indice de Massa Corporal (IMC) e {:.1f}.".format(idade,imc), end=" ")

if idade<=15:
    print("Voce deve verificar o resultado na tabela de IMC INFANTIL.")
elif idade>=60:
    print("Voce deve verificar o resultado na tabela de IMC IDOSO.")
elif 15<idade<60:
    if imc<18.5:
        print("Voce esta ABAIXO do Peso.")
    elif imc<25:
        print("O seu Peso e IDEAL!")
    elif imc<30:
        print("ATENçAO! Voce esta com SOBREPESO!")
    elif imc<40:
        print("ATENçAO!! Voce esta OBESO!!")
    else:
        print("ATENçAO!!! OBESIDADE MORBIDA!!!")

print("\nSempre cuide da sua SAUDE!!!")



