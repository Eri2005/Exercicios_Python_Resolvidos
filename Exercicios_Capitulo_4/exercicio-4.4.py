
'''
Perguntar o salario e calcular o aumento
Para salarios superiores a R$ 1.250 aumento de 10 %
Para salarios inferiores aumento de 15%
'''

salario = float(input('Informe o seu salário: '))
aumento = int()

if salario >= 1250:
    aumento = salario * 0.10
    salario = salario + (salario * 0.10)
    
if salario < 1250:
    aumento = salario * 0.15
    salario = salario + (salario * 0.15)
    
print(f'O reajuste será de R$ {aumento:6.2f} \nSeu salário será de R$ {salario:6.2f}')