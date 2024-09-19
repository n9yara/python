maior = 0
menor = 0
for pesos in range(1,6):
    kg = float(input('Peso da {} pessoa '.format(pesos)))
    if pesos == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
           menor = kg
print(f'o maior peso lido foi {maior}')
print(f'o menor peso lido foi {menor}')



