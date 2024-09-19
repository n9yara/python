import random
from time import sleep
palpite = int(input('Tente a advinhar o numero: '))
secret = random.randint(0,5)
print('loading...')
sleep(3)
if palpite == secret:
    print('parabens voce acertou')
else:
    print(f'Voce errou!, eu pensei no nunero {secret} e não no {palpite}!')