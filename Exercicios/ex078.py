lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor na posicão{cont}: ')))
print(f'Voce digitou os valores {lista}')   
print(f'O menor foi {min(lista)} na posição {lista.index(min(lista))}...')
print(f'O maior foi {max(lista)} na posição {lista.index(max(lista))}...')
    