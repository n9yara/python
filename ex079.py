lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print('Numero repetido, tente dnv')
    else:
        lista.append(num)
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break  
lista.sort()
print(f'Voce digitou os valores {lista}')