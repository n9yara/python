viagem = float(input('digite a distancia da sua viagem: '))
print(f'voce esta preste a comecar uma viagem de {viagem}Km')
if viagem <= 200:
    print(f'E o preço da sua passagem sera {viagem*0.50}')
else:
    print(f'E o preço da sua passagem sera {viagem*0.45}')

    