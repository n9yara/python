n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
med = (n1 + n2) / 2
print(f'tirando {n1} e {n2} a media do aluno é {med}')
if med >= 7:
    print('*APROVADO*')
elif med <5:
    print('*REPROVADO*')
elif med >= 5 and med < 7:
    print('*RECUPERAÇÃO*')