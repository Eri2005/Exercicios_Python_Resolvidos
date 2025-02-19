
"""
Perguntar a distancia 
Perguntar a velocidade media esperada
Calcular o tempo de viagem
"""

distancia_percorrer = int(input("Qual a distancia vai percorrer? "))
velocidade = int(input("Qual a velocidade pretende andar? "))

tempo_total_da_viagaem = distancia_percorrer / velocidade

print(f'O tempo gasto para a viagemserá de {tempo_total_da_viagaem:0.1f}H')