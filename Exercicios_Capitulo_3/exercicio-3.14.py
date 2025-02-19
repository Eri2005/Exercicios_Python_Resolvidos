
"""
Perguntar a quantidade de KM percorrida por um carro alugado
E a quantidade de dias ficou
Calcule o preço a pagar
Sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado 
"""

quilometro_percorrido = float(input("Distancia percorrido pelo veiculo: "))
quantidade_de_dias_alugado = int(input("Quantidade de dias ficou alugado: "))

valor_total_a_pagar = float((quilometro_percorrido * 0.15) + (quantidade_de_dias_alugado * 60))

print(f'Valor total a pagar é de {valor_total_a_pagar:.2f}')