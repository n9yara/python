from datetime import date


totmenor = 0
totmaior = 0
for pessoas in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pessoas)))
    anos = (date.today().year - nasc)
    if anos >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'ao todo tivemos {totmaior} maiores de idade e')
print(f'E tambem tivemos {totmenor} pessoas menores de idade')
