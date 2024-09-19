s = 0
conta = 0
for n in range(1,501, 2):
    if n % 3 == 0:
        s += n
        conta += 1
print(f'a soma de todos os {conta} valores numeros foi {s}')