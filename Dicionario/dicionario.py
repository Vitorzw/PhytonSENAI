time = {
    "nome": "Real Madrid",
    "champions": 15,
    "la liga": 36,
    "copa del rey":12,
    "mundial": 9
    
}

time1 = {
    "nome": "Barcelona",
    "champions": 5,
    "la liga": 28,
    "copa del rey":32,
    "mundial": 3
    
}

time2 = {
    "nome": "Atletico de Madrid",
    "champions": 0,
    "la liga": 11,
    "copa del rey":10,
    "mundial": 1
       
}

# exibir uma lista de dicionarios
lista_times = [time, time1, time2]

 # Escolhendo os campos
for times in lista_times:
    print(f"{times['nome']} - {times['champions']}")
    
    
    # exibindo todos
for times in lista_times:
    for chave, valor in times.items():
        print(f"{chave} - {valor}")
    print()
    
    
    
    
    
