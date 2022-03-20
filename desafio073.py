#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.


times=("Atlético-MG","Palmeiras","Flamengo","Corinthians","Fortaleza","RB Bragantino","Athletico-PR","Internacional","Fluminense","Atlético-GO","Cuiabá","Ceará","São Paulo","América-MG","Juventude","Santos","Bahia","Sport","Grêmio","Chapecoense")

print("~~"*60)
print("{:^100}".format("TABELA BRASILEIRAO"))
print("~~"*60)

print(f"Lista de times: {times}")
print("--"*60)
print(f"Os 5 primeiros times da tabela: {times[0:5]}")
print("--"*60)
print(f"Os 4 ultimos times da tabela:   {times[-4:]}")
print("--"*60)
print(f"Times em Ordem Alfabetica:      {sorted(times)}")
print("--"*60)
print(f"O time da Chapecoense esta na {times.index('Chapecoense')+1}° posiçao.")
print("=="*60)
#print("O time da Chapecoense esta na {}° posiçao.".format(times.index("Chapecoense")+1))