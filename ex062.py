termo = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
cont = 1
tot = 0
more = 10
while more != 0:
    tot = tot + more
    while cont <tot:
        print(f'{termo} --> ', end = '')
        termo += razao
        cont += 1
    more = int(input('Quantos termos voce quer mostrar a mais?')) 
print('fim', end = '')