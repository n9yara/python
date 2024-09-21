lista = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
         lista[1].append(valor)
print(f'Os pares digatos foram {lista.sort[0]}')
print(f'Os imapares digitados foram {lista.sort[1]}')
