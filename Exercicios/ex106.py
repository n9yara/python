def ayuda(com):
    help(com)


def titulo(msg, cor=0   ):
    tam = len(msg)
    print("-"* tam)
    print(msg)
    print("-"* tam)



comando = " "
while True:
    titulo("SISTEMA DE AJUDA")
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ayuda(comando)
    titulo("FIM")