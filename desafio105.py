#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um #dicionário com as seguintes informações:
#quatidade de notas;a maior nota; a menor nota; a media da turma;a situaçao (opcional)


def notas(*d,sit=False):
    """
     Args:
        Funcao para analisar a nota de varios alunos.
    Returns:
        parametro n= coloca uma ou varias notas dos alunos (pode colocar varias notas)
        parametro sit= valor opcional, indicando se deve ou nao adicionar a situacao.
        return = mostra um dicionario com varias situacoes com a situacao da turma.
    """
    dados={'total':len(d),'maior':max(d),'menor':min(d),'media':(sum(d)/len(d))}
    if sit==True:    
        if dados['media']>=7:
            dados['situacao']='Boa!'       
        elif 7>dados['media']>=5:
            dados['situacao']='Regular!'
        else:
            dados['situacao']='Ruim!'
    return dados
resp=notas(6,8,5,9,3, sit=True)
print(resp)