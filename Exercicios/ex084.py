lista = []
principal = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    res = str(input('Quer continuar?[S/N] ')).upper().strip()
    if res == 'N':
        break
print(F'Ao todo voce cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')
