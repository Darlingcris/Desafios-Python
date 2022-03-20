#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o #número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou #não na tela o processo de cálculo do fatorial.



def fatorial(num,opcao="n"):
    """Fazer o fatorial do numero.
    Args:
        param [num]: o numero a ser calculado.
        opcao[s]: mostra o processo do calculo.
    Returns:
        Retorna o fatorial.
    """
    f=1
    for n in range(num,0,-1):
        if opcao=="s":
            print(f"{n}", end=" ")
            print("X" if n>1 else "=", end=" ")
        f*=n    
    return f    

help(fatorial)
fat=int(input("Voce quer ver a fatorial de qual numero? "))
opcao=input("Voce quer ver o processo [S/N]? ")
print(fatorial(fat,opcao))