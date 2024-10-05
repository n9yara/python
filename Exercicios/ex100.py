from random import randint

def sorteio(list):
    for cont in range(0,5):
        numero = randint(1,10)
        num.append((numero))
        print(f"{numero}")


def somarpar(list):
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {list} temos {soma}")




num = []
sorteio(num)
somarpar(num)
    