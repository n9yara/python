grupo = {}
grupo2 = []
soma = media = 0
while True:
    grupo['nome'] = str(input('Nome: '))
    grupo['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()
    grupo['idade'] = int(input('Idade: '))
    soma += grupo['idade']
    grupo2.append(grupo.copy())
    res = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if res == 'N':
        break
print(f'A) Ao todo temos {len(grupo2)} pessoas cadastradas.')
media = soma / len(grupo2)
print(f'B) A media de idade é {media} anos.')
print(f'C) As mulheres cadastradas foram: ', end = '')
for p in grupo2:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end = '')
print()
print(f'D) Lista de pessoas que estão acima da media: ', end = '')
for p in grupo2:
    if p['idade'] >= media:
        print(f'foi {p["nome"]} com {p["idade"]}', end = '')
