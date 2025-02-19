
'''
Reescreva o código anterior 5.4
Que imprima os 10 primeiros múltiplicos de 3
'''
multiplos = int(input('Digite quantos multiplos deseja calcular: '))
x = 0

while x <= multiplos:
    if x % 3 == 0:
        print(x)
    x = x + 1