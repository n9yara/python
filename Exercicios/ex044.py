price = float(input('Preço das compras: '))
opcao = int(input('FORMAS DE PAGAMENTO\n[1] á vista no dinheiro/cheque\n[2] á vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nQual é sua opcão? '))
dez = price - (price*10/100)
cinco = price - (price*5/100)
if opcao == 1:
    total = dez
elif opcao == 2:
    total = cinco
elif opcao == 3:
    total = price
    parcela = price / 2
    print(f'Sua compra sera parcela em 2x de {parcela}')
elif opcao == 4:
    total = price + (price * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    totaldeparcelas = total / parcelas
    print(f'Sua compra vai ser parcelada em {parcelas} parcelas com juros de {totaldeparcelas:.2f}')
print(f'sua compra de R${price:.2f} vai custar {total:.2f} no final com juros')

                
