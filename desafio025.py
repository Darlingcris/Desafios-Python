#crie um programa que leia o nome de uma pessoa e diga
#se ela tem "SILVA" no nome.

n=str(input("Digite o seu nome completo: ")).strip()
n=n[0:].upper().count("SILVA")
print(n)


n=str(input("Digite o seu nome completo: ")).strip()
n=n.lower()
print("Seu nome tem \"Silva\"? {}".format("silva" in n))

n=str(input("Digite o seu nome completo: ")).strip()
print("Seu nome tem \"Silva\"? {}".format("silva" in n.lower()))