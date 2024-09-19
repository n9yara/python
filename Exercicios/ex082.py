lista = []
pares = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'os pares {pares}')
print(f'os impar {impar}')
