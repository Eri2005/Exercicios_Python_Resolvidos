
'''
Modifique o programa anterior 5.6
Sendo que pedir para o usuário informe o inicio e o fim da tabuada
Em vez de 1 a 10
'''

tabuada = int(input('Tabuada de: '))
inicio = int(input('De: '))
fim = int(input('Até: '))

x = inicio

while x <= fim:
    print(f'{tabuada} X {x} = ', tabuada * x)
    x = x + 1