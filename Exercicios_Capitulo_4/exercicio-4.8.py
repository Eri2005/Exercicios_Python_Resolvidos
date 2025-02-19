
'''
Lê dois números e pergunte qual operação deseja realizar
(+) Adição
(-) Subtração
(*) Multiplicação
(/) Divisão
E exiba o resultado
'''

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
operecao = input('Qual operação deseja realizar? \nSoma -> [+] \nSubtração -> [-] \nMultiplicação -> [*] \nDivisão -> [/] \nQual é a opção? ')

if operecao == '+':
    print(f'O resultado da Soma é {int(numero1 + numero2)}')

elif operecao == '-':
    print(f'O resultado da Subtração é {int(numero1 - numero2)}')
    
elif operecao == '*':
    print(f'O resultado da Multiplicação é {int(numero1 * numero2)}')
    
elif operecao == '/':
    print(f'O resultado da Divisão é {int(numero1 / numero2)}')

else:
    print('Opção inválida, digite novamente!')
    
#print(f'O resultado da {operecao} é {resultado}')