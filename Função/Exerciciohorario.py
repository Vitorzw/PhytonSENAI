from datetime import datetime

def cumprimentar(nome: str) -> str:
    """
    Retorna uma saudação baseada na hora atual.

    Args:
        nome (str): O nome da pessoa a ser saudada.

    Returns:
        str: A saudação.
    """

    hora_atual = datetime.now().hour

    if 0 <= hora_atual <= 5:
        return f"Boa madrugada, {nome}!"
    elif 5 < hora_atual <= 12:
        return f"Bom dia, {nome}!"
    elif 12 < hora_atual <= 19:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"

# Exemplo de uso:
print(cumprimentar("Vitor"))