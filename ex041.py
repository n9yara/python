from datetime import date
nasc = int(input('digite o ano de nascimento: '))
anos = (date.today().year - nasc)
print(f'O atleta tem {anos} anos.')
if anos <= 9:
    print('Classificação: MIRIM')
elif anos <=14:
    print('Classificação: INFANTIL')
elif anos <=19:
    print('Classificação: JUNIOR')
elif anos <=25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

