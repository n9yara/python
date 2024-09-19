lista = []
soma = 0
barato = ' '
maisde1000 = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    lista.append(preco)
    if preco == min(lista):
        barato = nome
    if preco >1000:
        maisde1000 += 1
        soma += preco
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
print(f'O total da compra foi {soma}R$')
print(f'Temos {maisde1000} produtos custando mais de 1000.00R$')
print(f'O produto mais barato foi {barato} que custa {min(lista)} ')