
# Calcular aumento de salario conforme a porcentagem fornecida pelo usuario
# Mostrar o valor da porcentagem e valor total com o reajuste

salario = float(input("Qual é o seu salário? R$ "))
porcentagem_de_aumento = float(input("Quantos porcentos será o aumento? "))

porcento = salario * porcentagem_de_aumento / 100
novo_salario = salario + (salario * porcentagem_de_aumento / 100)

print("\n")

print(f'Seu salario é R$ {salario:.2f}')
print(f'{porcentagem_de_aumento}% de aumento será de: R$ {porcento}')
print(f'Novo salário é: R$ {novo_salario:.2f}')

print("\n")