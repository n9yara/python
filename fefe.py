import random

opcoes = int(input('Suas opções:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nQual voce escolha? '))
lista = ['pedra', 'papel', 'tesoura']
makina = random.randint(0,2)
print(f'o computador escolheu {(lista[makina])}')

jogada_nay = lista[opcoes] # nome q representa o numero escolhido pelo user
jogada_pc = lista[makina] # nome q representa o numeo escolhido pela makina

if jogada_nay == "pedra": # jogada da nay
    if jogada_pc == "pedra": # pedra x pedra = empate
        print('empate')
    elif jogada_pc == "papel":
        print('perdeu')
    else:
        print('ganhou')
elif jogada_nay == "papel": # jogada da nay
    if jogada_pc == "pedra":
        print('venceu')
    elif jogada_pc == 1:
        print('empate')
    else:
        print('perdeu')
elif jogada_nay == 'tesoura': # jogada da nay
    if jogada_pc == 'pedra':
        print('perdeu')
    elif jogada_pc == 'papel': 
        print('venceu')
    else:
        print('empate')
else:
    print('jogada invalida')#kkkkkkkkkkk