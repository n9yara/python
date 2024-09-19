lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res == 'N':
            break
lista.sort(reverse=True)
print(f'voce digitou {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
        print('Essa lista possui o numero 5')
else:
        print('O valor 5 não foi digitado!')