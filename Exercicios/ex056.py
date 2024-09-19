sum = 0
c = 0
velho = 0
menosde20 = 0
for ppl in range(1,5):
    print('---- {} PESSOA ----'.format(ppl))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    sum += idade
    c = sum / 4
    if sexo in 'Ff' and idade <20:
     menosde20 += 1


print(f'a media de idade do grupos é {c} anos.')
print(f'Ao todo são {menosde20} mulheres com menos de 20 anos.')
