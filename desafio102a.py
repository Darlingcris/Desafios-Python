#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o #número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou #não na tela o processo de cálculo do fatorial.


def fatorial(num):
    """Fazer o fatorial do numero.
    Args:
        param [num]: o numero a ser calculado.
        opcao[s]: mostra o processo do calculo.
    Returns:
        Retorna o fatorial.
    """
    f=1
    for n in range(num,0,-1):
        f*=n    
    return f    

def show(opcao):
    
    if opcao=="s":
        for n in range(fat,0,-1):
            print(f"{n}", end=" ")
            print("X" if n>1 else "=", end=" ")
        return fatorial(fat)
    else:
        return "Programa Finalizado!"

help(fatorial)

fat=int(input("Voce quer ver a fatorial de qual numero? "))
print(fatorial(fat))

opcao=input("Voce quer ver o processo [S/N]? ")
print(show(opcao))