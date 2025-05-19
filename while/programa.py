while True:
    print("Selecione uma das alternativas abaixo")
    print("")
    print("[1] Fatorial")
    print("[2] Quadrado")
    print("[3] Cubo")
    print("[4] Tabuada")
    print("[0] Sair")
    
    opcao = int(input("Digite sua opcao"))
    if opcao == 0:
        break
    elif opcao == 1:
    
        valor = int(input('Entre com um número para saber o fatorial:'))  
        fatorial = 1  
        while (valor > 1):  
          fatorial = fatorial * valor  
          valor = valor - 1  
        print('O fatorial é {}.'.format(fatorial))
        
        
        
        
        
    elif opcao == 2:
        num1 = int(input("Digite um numero para saber seu quadrado: "))
        quadrado = num1 * num1
        print("seu resultado é", quadrado)
    elif opcao == 3:
        num1 = int(input("Digite um numero para saber seu cubo: "))
        quadrado = num1 * num1 * num1
        print("seu resultado é", quadrado)
    elif opcao == 4:
        num = int(input("digite um numero para saber sua tabuada"))
        print(num, 'X 1 =', num*1)
        print(num, 'X 2=', num*2)
        print(num, 'X 3 =', num*3)
        print(num, 'X 4 =', num*4)
        print(num, 'X 5 =', num*5)
        print(num, 'X 6 =', num*6)
        print(num, 'X 7 =', num*7)
        print(num, 'X 8 =', num*8)
        print(num, 'X 9 =', num*9)
        print(num, 'X 10 =', num*10)

    
        
        
    
        

