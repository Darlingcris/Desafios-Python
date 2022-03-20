#Faça um programa que leie a altura e a largura de uma parede em metros, calcule a sua àrea e a 
#quantidade de tinta necessaria para pintà.la. Sabendo que cada litro de tinta pinta uma area 
#de 2m quadrados.


a=float(input("Qual e a Altura da parede? "))
l=float(input("Qual e a Largura da parede? "))
p=(a*l)/2
print("\nA quantidade necessaria para pintar sera de {:.2f} litros de tinta.\n".format(p))

a=float(input("Qual e a Altura da parede? "))
l=float(input("Qual e a Largura da parede? "))
print("\nA area da sua parede e de {:.2f} metros quadrados, e a quantidade necessaria de tinta sera de {:.2f} litros.".format(a*l,(a*l)/2))