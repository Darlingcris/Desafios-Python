#Refaça o desafio 35 dos triangulos, acrescentando
#o recurso de mostrar que tipo de triangulo
#sera formado:
#Equilatero: todos os lados iguais
#Isosceles: dois lados iguais
#Escaleno: todos os lados diferentes

medida1=float(input("Digite o tamanho da primeira reta: "))
medida2=float(input("Digite o tamanho da segunda reta: "))
medida3=float(input("Digite o tamanho da terceira reta: "))

if medida1<medida2+medida3 and medida2<medida1+medida3 and medida3<medida1+medida2:
    print("\nO valor das retas formam um TRIANGULO", end=" ")
    if medida1==medida2==medida3:
        print("EQUILATERO.")
    elif medida1!=medida2!=medida3!=medida1:
        print("ESCALENO.")
    else:
        print("ISOSCELES.")
else:
    print("\nO valor das retas NAO formam um triangulo.")

