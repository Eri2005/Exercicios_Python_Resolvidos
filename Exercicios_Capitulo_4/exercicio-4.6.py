
'''
Pergunte ao usuario a distancia que deseja percorrer
Calcule o preço da passagem
Cobrando R$ 0,50 por km para viagem ate de 200 km
E R$ 0,45 para viagens mais longas
'''

distancia = int(input('Qual é a distancia deseja percorrer? '))
passagem = 0

if distancia <= 200:
    passagem = float(distancia * 0.50)
else:
    passagem = float(distancia * 0.45)
    
print(f'A viagem de {distancia} KM. \nO valor da passagem ficou em R${passagem:6.2f}')