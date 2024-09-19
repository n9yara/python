import random 
vitoria = 0
while True:
    jogador = int(input('digite um valor '))
    computador = random.randint(0,11)
    tot = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print(f'voce jogou {jogador} e o computador jogou {computador} no total de {tot}')
    if escolha == 'P':
        if tot % 2 ==0:
            print('voce venceu')
            vitoria += 1
        else:
            print('voce perdeu')
            break
    elif escolha == 'I':
        if tot % 2 == 1:
            print('voce venceu')
            vitoria += 1
        else:
            print('voce perdeu')
            break
print(f'GAME OVER, voce venceu {vitoria} vezes')