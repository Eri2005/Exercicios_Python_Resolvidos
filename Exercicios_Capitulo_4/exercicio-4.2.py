
'''
Pergunte ao usuario a velocidade do carro.
Caso ultrapasse 80 km/h, exiba uma mensagem.
Dizendo que foi multado
O valor da multa é:
A cada km a mais será cobrado um valor de R$ 5 por km
'''

velocidade = int(input('Qual é a velocidade? '))
multa = 5

if velocidade > 80:
    total_da_multa = (velocidade - 80) * 5
    print(f'Valor total da multa é de R$ {total_da_multa}')
