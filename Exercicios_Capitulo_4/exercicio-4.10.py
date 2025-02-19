
'''
Calcular o preço a pagar pelo fornecimento de energia
Pergunte a quantidade kWh consumida e o tipo de instalação
R -> Residência
I -> Indústria
C -> Comércio
Preço por faixa:

Residencia -> até 500 kWh       - R$ 0,40
              acima de 500kWh   - R$ 0,65

Comercial  -> até 1000 kWh      - R$ 0,55
           -> acima de 1000 kWh - R$ 0,60
           
Industrial -> até 5000 kWh      - R$ 0,55
           -> acima de 5000 kWh - R$ 0,60
'''

consumo = int(input("Quanto foi o consumo de kWh do mês? "))
instalacao = input('Qual é tipo de instalação: \nR -> Residencial \nC -> Comercial \nI -> Industrial \nInforme qual: ')

if instalacao == 'R':
    if consumo <= 500:
        valor = 0.40
    else:
        valor = 0.65
        
elif instalacao == 'C':
    if consumo <= 1000:
        valor = 0.55
    else:
        valor = 0.60
        
elif instalacao == 'I':
    if consumo <= 5000:
        valor = 0.55
    else:
        valor = 0.60
else:
    valor = 0
    print('Erro! Tipo de instalação desconhecido!')

total_pagar = consumo * valor

print(f'Valor a pagar ficou em: R$ {total_pagar:6.2f}')