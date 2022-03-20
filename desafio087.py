#Aprimore o desafio anterior, mostrando no final:                                                    A) A A)soma de todos os valores pares digitados.                                                                                                 B) A soma dos valores da terceira coluna.                                                                                                    C) O maior valor da segunda linha.


matriz=[[0,0,0],[0,0,0],[0,0,0]]
somapar=somacoluna=maiorsegundal=0

for l in range (0,3):
    for c in range(0,3):        
        matriz[l][c]=int(input(f"Digite um valor para [{l},{c}]: "))

        if matriz[l][c]%2==0:
                somapar+=matriz[l][c]
    
        while c==2:
               somacoluna+=matriz[l][c]
               break
        
        while matriz[1][c]>maiorsegundal:
            maiorsegundal=matriz[l][c]
       
print()                           
print("=-"*15)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
print("=-"*15)    
print(f"A soma dos valores pares é: {somapar}")
print(f"A soma da terceira coluna é: {somacoluna}")
print(f"O maior numero da seguda linha é: {maiorsegundal}")