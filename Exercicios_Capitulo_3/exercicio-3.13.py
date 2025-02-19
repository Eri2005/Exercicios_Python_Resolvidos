
"""
# Converter uma temperatura de ºC (Celsius) em ºF (fahrenheit)
# Formula f = 9 X C / 5 + 32

Formulas de conversões
Kelvin -> Celsius: C = k - 273
Kelvin -> Fahrenheit: (k - 273) x 1.8 + 32
Celsius -> Kelvin: k = c + 273
Celsius -> Fahrenheit: f = c x 1.8 + 32
Fahrenheit -> Celsius: c = (f -32) / 1.8
Fahrenheit -> Kelvin: k = (f - 32) x 5 / 9 + 273
"""


celsius = int(input("Informe o graus em Celsius para converter para Fahrenheit: "))

graus_fahrenheit = float(celsius * 1.8 + 32)

print(f'Valor de {celsius}°C em Fahrenheit é de {graus_fahrenheit}°F')