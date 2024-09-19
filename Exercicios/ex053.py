frase = str((input('digite uma frase: '))).strip().upper()
txt = frase.split()
juntas = ''.join(txt)
inverso = juntas[::-1]
print(f'O inverso de {frase} é {inverso}')
if juntas == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('a frase digitada não é um palindromo!')
