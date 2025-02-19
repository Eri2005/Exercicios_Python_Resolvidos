
"""
Calcular a redução de tempo de vida de um fumante
Perguntar quantos cigarros fuma por dia
Perguntar qwunatos anos ja fumou
Considere que a cada cigarro ele perde 10 minutos de vida
Calcule quantos dias de vida perderá 
Exiba o total em dias
"""

cigarro_por_dia = int(input("Quantos cigarros fuma por dia? "))
anos_que_fumou = int(input("Por quantos anos já fumou? "))

'''
horas_perdidos_de_vida = int(cigarro_por_dia * 10) / 60 # Calculando os minutos total
horas = int(horas_perdidos_de_vida / 60)
minutos = round(horas_perdidos_de_vida % 1 * 60) # Trazendo somente os minutos
# A função ROUND permite arredondar um número para um determinado número de casas decimais
'''

total_de_cigarros_por_mes = cigarro_por_dia * 30
total_de_cigarro_por_ano = total_de_cigarros_por_mes * 12
horas_perdidos_de_vida = int(cigarro_por_dia * 10) / 60 # Calculando as horas e mostrando os minutos total
total_de_horas_perdido_de_vida = (anos_que_fumou * total_de_cigarro_por_ano) * horas_perdidos_de_vida

print("\n")

print(f'{int(horas_perdidos_de_vida)} horas')
print(f'Total de cigarro no mês: {total_de_cigarros_por_mes} cigarros')
print(f'Total de cigarro ao ano: {total_de_cigarro_por_ano} cigarros')
print(f'Total de horas perdido ao ano: {int(total_de_horas_perdido_de_vida)} horas') # Pegando somente a parte inteira do resultado


'''
print(f'Horas {horas}H')
print(f'Horas perdido de vida {horas_perdidos_de_vida:.2f}H')
print(f'Horas perdido de vida {int(horas_perdidos_de_vida)}H') # Pegando somente a parte inteira do resultado
print(f'Minutos {minutos}M')
print(f'Total de anos {total_de_anos} meses')
'''


print("\n")