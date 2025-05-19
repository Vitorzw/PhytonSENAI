ano = int(input(" Digite um ano de nascimento"))
idade = 2025 - ano

if ano_atual <= 2025 and ano_atual >= 1908 and ano_nascimento >= 1908 and ano_nascimento <= 2025:

if ano <= 2025:
    if idade <= 10:
        print("criança")

    elif idade >= 11 and idade <= 17:
        print("adolescente")
        
    elif idade >= 18 and idade <= 59:
        print("adulto")
        
    elif idade < 60:
        print("idoso")
else:
    print("selecione um ano menor")
        
