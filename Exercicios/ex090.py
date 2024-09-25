lista = []
dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Media de {dic["nome"]}: '))
lista.append(dic.copy())
print(f'Nome é igual a {dic["nome"]}')
print(f'A media é igual a {dic["media"]}')
if dic['media'] < 6:
    print('Situação é igual a reprovado')
else:
    print('Situação igual aprovado.')

