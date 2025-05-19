#Crie uma lista com 5 objetos
Objetos = ["Borracha", "Apontador", "Lapis", "Garrafa", "Garfo"]
print('lista foi criada')

#Adicione mais um objeto no final da lista
Objetos.append("losa")

#Acesse o objeto que esta na segunda opção e exiba-o
V = Objetos[1]
print(V)

#Remova um objeto da lista e exiba-o
V = Objetos.pop(1)
print(V)

#Exiba o tamanho da lista

print(len(Objetos))

#Mostre todos os itens com o for
for Objeto in Objetos:
    print(Objeto)

#Verifique se 'cadeira' esta na lista. Se sim remova-a, senão adicione
if "cadeira" in Objetos:
    Objetos.remove("cadeira")
    
else:
    Objetos.append("cadeira")


#Ordene a lista em ordem alfabetica, exiba o antes e o depois
print(Objetos)
Objetos.sort()
print(Objetos)

#Exiba o primeiro e o ultimo objeto e exiba eles
len(Objetos)
PRIMEIRO = Objetos[0]
ULTIMO = Objetos [- 1]
print("PRIMEIRO", PRIMEIRO, "ULTIMO", ULTIMO)

#limpe toda a lista
Objetos.clear()

