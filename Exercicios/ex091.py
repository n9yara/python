from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),
        } 

rank = []
print('Valores sorteados: ')
for k, v in jogo.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado')
rank = sorted(jogo.items(), key =itemgetter(1), reverse=True)
print('Ranking:')
for i, v in enumerate(rank):
    sleep(0.5)
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
