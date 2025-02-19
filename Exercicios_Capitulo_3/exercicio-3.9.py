
#Conversão de Dia, Hora e Minutos para Segundos e somando todos os segundos

dias = int(input("Informe quantidade de dias: "))
horas = int(input("Informe quantidade de horas: "))
minutos = int(input("Informe quantidade de minutos: "))
segundos = int(input("Informe quantidade de segundos: "))

segundos = 3600
conversao_minutos_em_segundos = segundos * 60
conversao_horas_em_segundos = conversao_minutos_em_segundos * 60
conversao_dia_em_segundos = conversao_horas_em_segundos * 60

total_minutos_em_segundos = conversao_minutos_em_segundos * minutos
total_horas_em_segundos = conversao_horas_em_segundos * horas
total_dias_em_segundos = conversao_dia_em_segundos * dias
total_de_segundos = segundos + total_minutos_em_segundos + total_horas_em_segundos + total_dias_em_segundos

print('\n')

print(f'Um segundo é {segundos}')
print(f'Total de {minutos} minutos convertidos em segundos é {total_minutos_em_segundos}')
print(f'Total de {horas} horas convertidos em segundos é {total_horas_em_segundos}')
print(f'Total de {dias} dias convertidos em segundos é {total_dias_em_segundos}')
print(f'Total de segundos é {total_de_segundos}')