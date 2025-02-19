
'''
Lê três números e que imprima o maior e o menor
'''

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

maior = 0
menor = 0

if numero1 > numero2:
    maior = numero1
    menor = numero2

if numero1 > numero3:
    maior = numero1
    menor = numero3

if numero1 < numero2:
    maior = numero2
    menor = numero1

if numero1 < numero3:
    maior = numero3
    menor = numero1

if numero2 > numero3:
    maior = numero2
    menor = numero3

if numero2 < numero3:
    maior = numero3
    menor = numero2
    
print(f'Maior é {maior} \nMenor é {menor}')