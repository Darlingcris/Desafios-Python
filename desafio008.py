# Escreva um programa que leia um valor em metros, e o exiba convertido 
# em centimetros e milimetros.

m=float(input("Digite um valor em metros: "))
cm=m*100
mm=m*1000
print("O valor {} digitado em metro(s), corresponde a {} centimentros e a {} milimetros.\n".format(m,cm,mm))

m=float(input("Digite um valor em metros: "))
print("O valor {} digitado em metro(s), corresponde a {} centimentros e a {} milimetros.\n".format(m,m*100,m*1000))

m=float(input("Digite um valor em metros: \n"))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000
print("O valor {} digitado em metro(s), corresponde a:\n\n{} km\n{} Hm\n{} Dam\n{} Dm\n{} Cm\n{} Mm\n".format(m,km,hm,dam,dm,cm,mm))