
def converter_temperatura(celsius: float) -> tuple:
    """
    Converte uma temperatura em graus Celsius para Fahrenheit e Kelvin.

    Args:
        celsius (float): A temperatura em graus Celsius.

    Returns:
        tuple: Uma tupla contendo a temperatura em Fahrenheit e Kelvin.
    """

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    return fahrenheit, kelvin

# Exemplo de uso:
celsius = 30
fahrenheit, kelvin = converter_temperatura(celsius)

print(f"{celsius}°C é igual a:")
print(f"{fahrenheit:.2f}°F")
print(f"{kelvin:.2f}K")