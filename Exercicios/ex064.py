cont = 0
n = 1
s = 0
while n != 999:
    n = int(input('Digite um numero inteiro'))
    if n != 999:
        cont += 1
        s += n
print(f'Voce digitou {cont} numeros e a soma deles foi {s}.')