print(25**(1/2))

x="="*3
print(x)

print("0"*4)                                    #para repetir 4 vezes o conteudo.

print("Eu sou a melhor programadora!"*4)        #repeti atè a string.

x=input("Digite o seu nome: ")                 
print("Prazer {:10}!".format(x))          #coloca a palavra no espaço de caracteres que vc quer.

x=input("Digite o seu nome: ")
print("Prazer {:>10}!".format(x))         #palavra alinhada à direita do espaço.      

x=input("Digite o seu nome: ")
print("Prazer {:<10}!".format(x))         #palavra alinhada à esquerda do espaço. 

x=input("Digite o seu nome: ")
print("Prazer {:^10}!".format(x))         #palavra centralizada no espaço.

x=input("Digite o seu nome: ")
print("Prazer {:=^10}!".format(x))        #palavra centralizada e destacada no espaço.