print('-'*30)
texto = 'LISTAGEM DE PREÇO'
print(f'{texto.center(30)}')
print('-'*30)
lista = ('Selula', 1000,
         'Caderno', 10,
         'Bota', 5000,
         'Blusa', 50,
         'Controle', 160,
         'Mousepad', 250,
         'Teclado', 1600,)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end = '')
    else:
        print(f'R$ {lista[pos]:>4}')
print('-'*30)