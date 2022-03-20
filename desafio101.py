#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento #de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e #OBRIGATÓRIO nas eleições.



def voto(ano):
    from datetime import date
    idade=date.today().year-ano

    if 18<=idade<=65:
        return f"Na idade de {idade} anos: VOTO OBRIGATORIO!"
    elif 16<=idade<18 or idade>65:
        return f"Na idade de {idade} anos: VOTO OPCIONAL!"
    elif idade<16:
        return f"Na idade de {idade} anos: NAO VOTA!"
    
       
print(voto(int(input("Ano de nascimento [4 digitos]: "))))
