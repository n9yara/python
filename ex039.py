from datetime import date
nasc = int(input('Ano de nascimento: '))
anos = (date.today().year - nasc)
diferenca = (18 - anos)
diferenca2 = (anos - 18)
print(f'quem nasceu em {nasc} tem {anos} anos em 2024.')
if anos == 18:
    print('voce tem que se alistar imediatamente!!!')
elif anos<18:
    print(f'ainda faltam {diferenca} anos para seu alistamento\nSeu alistamento sera em {2024 + diferenca}')
elif anos >18:
    print(f'voce ja deveria ter se alistado a {diferenca2} anos seu alistamento foi em {2024 - diferenca2}')

