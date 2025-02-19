
'''
Aprovar emprestimo para compra de um casa
Perguntar o valor da casa
Salario
Quantidade de anos a pagar
O valor das prestações não deve passar de 30% do salario
Calcule o valor das prestações divido pelo número de meses a pagar
'''

valor_da_casa = float(input('Qual é valor da casa: '))
salario = float(input('Qual é salário: '))
anos = int(input('Quantidade de anos para pagar: '))

meses = anos * 12
prestacoes = valor_da_casa / meses

if prestacoes > salario * 0.3:
    print('Infelizmente você não pode obter o emprestimo')

else:
    print(f'Valor da prestação: R${prestacoes:7.2f} Empréstimo OK')