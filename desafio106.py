#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual #vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def manual(msg):
    
    from time import sleep
    while True:
        
        l=(len(msg)+4)
        print('\033[1;37;42m-'*l)
        print(f"\033[1;37;42m  {msg}  ")
        print('\033[1;37;42m-'*l)
        print('\033[m')
        r=input('Funçoes ou Biblioteca [Fim finaliza] -> ')
        
        if r=='fim':
            break

        else:        
            t=(len(r)+5)
            print()
            print('\033[1;37;44m-'*31,end="")
            print('-'*t )
            print("\033[1;37;44m  Acessando o manual do comando",end=" ")
            print(f"'{r}'  ")
            print('\033[1;37;44m-'*31,end="")
            print('-'*t)
            print('\033[m')
            sleep(.3)
            print("\033[7;37;40m")
            help(r)
            print("\033[m")

    print('\033[1;37;35m='*13)
    print("\033[1;37;35m  Até Logo!  ")
    print('\033[1;37;35m='*13)
    print('\033[m')
    
manual('SISTEMA DE AJUDA PYHELP')  