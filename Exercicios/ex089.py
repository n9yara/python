galera = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    galera.append([nome, [nota1, nota2,], media])
    res = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if res == 'N':
        break
print(f'{'N.':<4}{'NOME':<6}{'MEDIA':>8}')
for i, a in enumerate(galera):
    print(f'{i:<4}{a[0]:<6}{a[2]:>8}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? (333 da break): '))
    if opcao == 333:
        break
    if opcao <= len(galera) -1:
        print(f'Notas de {galera[opcao][0]} sáo {galera[opcao][1]}')