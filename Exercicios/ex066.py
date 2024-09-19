cont = 0
soma = 0
while True:
    num = int(input('digite um numero(>999< me para) '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'voce digitou {cont} valores e a soma deles foi {soma}')