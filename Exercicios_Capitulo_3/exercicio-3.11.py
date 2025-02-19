
"""
Solicitar o preço ao usuario e o percentual de desconto
Exibir o valor do desconto e o preço a pagar
"""

valor_da_mercadoria = float(input("Qual o valor da mercadoria? R$: "))
valor_do_desconto = float(input("Qual a porcentagem de desconto: "))

total_da_porcentagem = valor_da_mercadoria * valor_do_desconto /100
total_de_desconto = valor_da_mercadoria - (valor_da_mercadoria * valor_do_desconto /100)

print("\n" + "-" * 15 + "Resultado " + "-" * 15 + "\n")
print(f'Valor da mercadoria: R$ {valor_da_mercadoria:.2f}')
print(f'Valor do desconto: {total_da_porcentagem}')
print(f'Total a pagar com o desconto: R$ {total_de_desconto:.2f}')

print("\n")