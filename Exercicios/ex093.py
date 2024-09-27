jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(F'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-'*30)
print(f'Nome: {jogador["nome"]}')
print(f'Gols: {jogador["gols"]}')
print(f'Total: {jogador["total"]}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'  -> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
