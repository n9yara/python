casa = float(input('Valor da casa: '))
salario = float(input('Salario do comprador: '))
anos = int(input('quantos anos de financiamento: '))
parcela = casa / (anos*12)
taxa = salario * 30 / 100
print(f'Para pagar uma casa no valor de {casa:.2f} em {anos} anos a prestação sera de {parcela:.2f}')
if parcela <= taxa:
    print('APROVADO!')
else:
    print('NEGADO!')