dic = {}
dic['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dic['idade'] = 2024 - nasc
dic['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['cpts'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salario'] = int(input('Salario: '))
    dic['aposentadoria'] = dic['idade'] + ((dic["contratação"] + 35) - 2024)

print(f'Nome: {dic["nome"]}')
print(f'Idade: {dic["idade"]}')
print(f'Ctps: {dic["cpts"]}')
if dic['cpts'] != 0:
    print(f'Contratação: {dic["contratação"]}')
    print(f'Salario: {dic["salario"]}')
    print(f'Aposentadoria: {dic["aposentadoria"]}')