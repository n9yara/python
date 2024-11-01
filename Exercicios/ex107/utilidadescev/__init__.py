def metade(preco=0, formato=False):
  res = preco / 2
  return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
  res = preco * 2
  return res if not formato else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
  res = preco + (preco*taxa/100)
  return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
  res = preco - (preco*taxa/100)
  return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
  return f"{moeda}{preco}".replace('.', ',')


def resumo(preco, mais, menos):
  print('-'*30)
  print('RESUMO DO VALOR'.center(30))
  print('-'*30)
  print(f'Preço analisado: \t{moeda(preco)}')
  print(f'Dobro do preço: \t{dobro(preco, formato=True)}')
  print(f'Metade do preço: \t{metade(preco, True)}')
  print(f'{mais}% de aumento: \t{aumentar(preco, formato=True)}')
  print(f'{menos}% de redução: \t\t{diminuir(preco,formato=True)}')
  print('-'*30)
  