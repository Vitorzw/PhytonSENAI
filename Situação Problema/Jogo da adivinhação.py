import random
pc = random.randint(0,100)

print("  JOGO DO ADIVINHA ")
print("vamos jogar?")
while True:
  numero = int(input('digite um numero'))
  if numero == pc:
    print('seu numero é',pc)
    print("[1]-sim")
    print("[0   ]-nao")
    escolha = int(input("voce quer continuar?: "))
    if escolha == 0:
        break
    pc = random.randint(0,100)
  elif numero > pc:
      print('o numero menor que',numero)
  elif numero < pc:
      print('o numero maior que',numero)
