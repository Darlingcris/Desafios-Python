
#Crie um programa que leia duas notas
#de um aluno e calcule sua media, mostrando
#uma mensagem no final de acordo com a 
#media atingida:
#media abaixo de 5.0: reprovado
#media entre 5.0 a 6.9: Recuperaòao
#Media 7.0 ou superior: Aprovado

nota1=float(input("\nDigite a primeira nota: "))
while nota1>10:
    nota1=float(input("\nNOTA INVALIDA. Digite a nota correta: "))
nota2=float(input("\nDigite a segunda nota: "))
while nota2>10:
    nota2=float(input("\nNOTA INVALIDA. Digite a nota correta: "))
media=(nota1+nota2)/2

print("\nAs notas sao: {:.1f} e {:.1f}. A media do aluno e {:.1f}.".format(nota1,nota2,media))

if media<5:
    print("\nO aluno foi REPROVADO!")
elif 7>media>=5:
    print("\nO aluno esta de RECUPERACAO!")
elif media>=7:
    print("\nO aluno foi APROVADO!")
