import inputs
 
 
pais_inscritos = []

pais_presentes = []

pais_ausentes = []
 
while True:

    print("")

    print("Menu de opções")

    print("1 - Cadastrar nome dos pais")

    print("2 - Exibir o total de pais")

    print("3 - Exibir a lista de nomes em ordem alfabética")

    print("4 - Realizar a confirmação de presença dos pais")

    print("5 - Exibir um relatório das chamadas")

    print("6 - Sair")

    op = inputs.input_int("Digite sua escolha: ")

    if op == 1:

        nome = inputs.input_str("Digite o nome que deseja cadastrar: ")

        if nome in pais_inscritos:

            print("Nome já cadastrado.")

        else:

            pais_inscritos.append(nome)

            print("Nome cadastrado com sucesso.")

    elif op == 2:

        print("O total de inscritos foi de", len(pais_inscritos), "pessoas.")

    elif op == 3:

        pais_inscritos.sort()

        for nome in pais_inscritos:

            print(nome)

    elif op == 4:

        pais_presentes = []

        pais_ausentes = []

        for nome in pais_inscritos:

            pergunta = inputs.input_int(nome + " está presente? (s/n): ")

            if pergunta == "s":

                pais_presentes.append(nome)

            elif pergunta == "n":

                pais_ausentes.append(nome)

    elif op == 5:

        print("Relatório de presença:")

        for nome in pais_presentes:

            print("Presente:", nome)

        for nome in pais_ausentes:

            print("Ausente:", nome)

    elif op == 6:

        print("Fechando o programa.")

        break
 
import inputs
 
 
 
lista = []
 
while True:

    print("")

    print("menu de opções")

    print("1 - cadastrar um nome")

    print("2 - exibir o total de inscritos")

    print("3 - exibir a lista de nomes em ordem alfabética")

    print("4 - permitir a consulta de um nome")

    print("5 - sair")

    opcao = inputs.input_int(("Digite sua escolha"))
 
    print("")
 
    if opcao == 1:
 
        nome = inputs.input_str("digite o nome que deseja cadastrar:")
 
        if nome in lista:
 
            print("nome cadastrado")
 
        else:
 
            lista.append(nome)
 
            print("nome cadastrado ")
 
    elif opcao == 2:
 
        print("o total de inscritos foram", len(lista))
 
    elif opcao == 3:
 
        for nome in lista:
 
            print(nome)
 
    elif opcao == 4:
 
        nome = inputs.inputs_int("digite seu nome que deseja consultar")
 
        if nome in lista:
 
            vari = inputs.inputs_str("nome encontrado com sucesso , você deseja remover da lista? s/n ")
 
            if vari == "s":
 
                lista.remove(nome)
 
                print("nome retirado com sucesso")
 
            elif nome1 == "n":
 
                print("o nome ainda permanece na lista")
 
        else:
 
            nome1 = inputs.inputs_str("nome não encontrado, deseja adiciona-lo? s/n")
 
            if nome1 == "s":
 
                lista.append(nome)
 
                print("o nome foi adicionado à lista")
 
            elif  nome1 == "n":
 
                print("ok")
 
            else:
 
                print("opção inesistente")
 
    elif opcao == 5:
 
        print("você saiu")
 
        break
 
    else:
 
        print("opção inesistente")

 
 