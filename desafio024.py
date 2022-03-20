#crie um programa que leia o nome de uma cidade e diga
#se ela começa ou nao com o nome "SANTO"

n=str(input("Digite o nome da cidade: ").strip())
s=n.lower().split()

if s[0]=="santo":
    print("\nO nome da cidade comeca com o nome \"Santo\".")
else:
    print("\nO nome da cidade nao comeca com o nome \"Santo\".")


n=str(input("\nDigite o nome da cidade: ")).strip()
print(n[:5].upper()=="SANTO")
