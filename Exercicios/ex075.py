numeros = tuple(int(input('Digite os numeros: '))for c in range(1, 5))
print(f'Voce digitou os valores: {numeros}')
print(f'O numero nove foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 esta na posição {numeros.index(3)}')
else:
    print('O valor 3 não foi digitado')
print(f'Foram digitados os valores pares', end = '')  
for n in numeros:
    if n % 2 == 0:
        print(n, end = '')
        