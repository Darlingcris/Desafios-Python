x="7"
print(type(x))          #para saber qual è o tipo da variavel

x=7                     #sò coloca entre parenteses se for uma funçao
print(type(x))

n1=2                    #o numero està como inteiro 
n2=4
x=n1+n2
print(x)

n1=float(input("Digite o primeiro numero: "))
n2=float(input("Digite o segundo numero: "))
x=n1+n2
#print("A soma entre", n1,"e",n2,"e igual a",x,".")             #muitas aspas
print("A soma entre {} e {} e igual a {}.".format(n1,n2,x))     #usar o format

curso="Curso de Pyton"
print(curso.upper())            #usado para colocar todas as letras em maiusculo

curso="Curso de Pyton"
print(curso.isupper())          #usado para verificar se todas as letras estao em maiusculo

x1=int(input("Digite o primeiro numero: "))
x2=int(input("Digite o segundo numero: "))
y=x1+x2
print("A soma entre {} e {} e igual a {}.".format(x1,x2,y))