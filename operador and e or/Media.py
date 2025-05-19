n1 = int(input("solicite uma nota "))
n2 = int(input("solicite outra nota "))
if n1 > 0 and n1 < 100 and n2 > 0 and n2 < 100:
    nota = n1 + n2
    media = nota / 2
if media >= 70:
    print("exibir aprovado")
if media <= 70:
    print("exibir reprovado")
elif media >= 50 and media <= 70:
    print("exibir recuperação")
