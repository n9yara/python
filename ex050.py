s = 0
c = 0
for c in range(0,6):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
     s += numero
     c += 1
print(f'voce informou {c} pares e a soma de todos eles foi {s}')


    