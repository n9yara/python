conta = []
aberto = 0
fechado = 0
conta.append(str(input('Digite uma expressão: ')))
for expressao in conta:
    if expressao == '(':
        aberto += 1
    elif expressao == ')':
        fechado += 1

if aberto == fechado:
    print('Sua expressão esta valida!')
else:
    print('expressão invalida.')