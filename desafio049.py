#refaça o desafio 9, mostrando a tabuada
#de um numero que o usuario escolher,so 
#agora usando um laço de repetiçao.

numero=int(input("\nVoce quer saber a tabuada de qual numero? "))
x=0
print("\n{:#^40}".format(" TABUADA "))
while x<=10:
    print("\n{} x {} = {}".format(x,numero,x*numero))   
    x+=1
print("\n{:#^40}".format(" FIM "))   

numero=int(input("\nVoce quer saber a tabuada de qual numero? "))
print("\n{:=^40}".format(" TABUADA "))
for x in range(0,11):              
    print("\n{} x {} = {}".format(x,numero,x*numero))
print("\n{:=^40}".format(" FIM "))