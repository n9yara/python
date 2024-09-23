from random import randint as rando
from time import sleep as timer


lista = []
listadois = []
total = 1
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
while total <= jogos:
    cont = 0
    while True:
        num = rando(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort() 
    listadois.append(lista[:])   
    lista.clear()
    total += 1 
timer(0.5)
print(f'SORTEANDO...')
for i, l in enumerate(listadois):
    timer(1)
    print(f'Jogo {i+1}: {l}')