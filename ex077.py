palavras = ('nayara', 'fernanda', 'carro', 'computador',
            'televisao', 'monitor', 'teclado', 'mouse')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end = '')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end = '')