n = int(input('Digite um numero '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[0;32m", end='')
        tot += 1
    else:
        print("\033[0;31m", end='')
    print(f'{c}',end ='')
print(f'\n\033[mO {n} foi divisivel {tot} vezes')
if tot == 2:
    print('É um numero primo!')
else:
    print('Não é um numero primo :3')
