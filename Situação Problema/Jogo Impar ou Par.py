import random

def jogos_levelUp():
    print('menu jogo')
    print('[1] - impar')
    print('[2] - Par')
    escolha = int(input('Selecione uma das opções'))
    
    if escolha == 1:
        print('você vai ser impar')
        
    elif escolha == 2:
        print('você vai ser par')
        
    print('selecione um numero')
    num = int(input(''))
    n_aleatorio = random.randint(1,10)
    print("O computador escolheu", n_aleatorio)
    soma = num + n_aleatorio
    total = soma % 2 == 0
         
    if escolha == 1:
        if total:
            print('voce perdeu')  
        else:
            print('voce ganhou')                
    if escolha == 2:
         if total:
            print('voce ganhou')                          
         else:
            print('voce perdeu')
                          
    print('Deseja continuar?')
    print('[1] - Sim')
    print('[2] - Não')
    num = int(input('Escolha uma das opcoes'))
    if num == 1:
        (jogos_levelUp)
    else:
        print('O jogo acabou!')
             
jogos_levelUp()           
             
    
    
    