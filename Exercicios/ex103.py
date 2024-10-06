def ficha(nome="desconhecido", gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato")
    


nome = str(input("Nome do jogador: "))
gols = str(input("Quantidade de gols: "))
ficha(nome, gols)