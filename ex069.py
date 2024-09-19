maisde18 = 0
mulhermenosde20 = 0
homens = 0
while True:
    idade = int(input('Idade: '))
    if idade >18:
        maisde18 += 1
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'F' and idade <20:
        mulhermenosde20 += 1
    if sexo == 'M':
        homens += 1
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18: {maisde18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulhermenosde20} mulheres com menos de 20')

