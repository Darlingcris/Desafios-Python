#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular  
#(largura e comprimento) e mostre a área do terreno.



def formula (largura,comprimento):
    r=largura * comprimento
    print(f"A area do terreno {largura} X {comprimento} é de {r:.1f} metros quadrados.")

#programa principal

largura=float(input("Qual é a largura do terreno (m)? "))
comprimento=float(input("Qual é o comprimento do terreno (m)? "))
formula(largura,comprimento)











