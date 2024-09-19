import random
opcoes = int(input('Suas opções:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nQual voce escolha? '))
lista = ['pedra', 'papel', 'tesoura']
makina = random.randint(0,2)
print(f'o computador escolheu {(lista[makina])}')
if opcoes == 0:
    if makina == 0:
        print('empate')
    elif makina == 1:
        print('perdeu')
    else:
        print('ganhou')
elif opcoes == 1:
    if makina == 0:
        print('venceu')
    elif makina == 1:
        print('empate')
    elif makina == 2:
        print('perdeu')
elif opcoes == 2:
    if makina == 0:
        print('perdeu')
    elif makina == 1: 
        print('venceu')
    elif makina == 2:
        print('empate')
else:
    print('jogada invalida')
        
           

