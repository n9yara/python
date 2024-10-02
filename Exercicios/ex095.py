jogador = {}
partidas = []
galera = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    galera.append(jogador.copy())
    res = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if res == 'N':
        break
for k, v in enumerate(galera):
    print(f'{k:>4}',  end = '')
    for d in v.values():
        print(d)
while True:
    busca = int(input("Mostrar dados de qual jogador?(333 para parar): "))
    if busca == 333:
        break
    if busca >= len(galera):
        print(f"nao existe jogador com o codigo {busca}")
    else:
        print(f"-- levantamento do jogador {galera[busca]["nome"]}")
        for i, g in enumerate(galera[busca]["nome"]):
            print(f"  No jogo {i+1} fez {g} gols")
