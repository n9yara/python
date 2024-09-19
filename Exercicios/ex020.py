import random
n1 = input('digite o primeiro aluno: ')
n2 = input('digite o segundo aluno: ')
n3 = input('digite o terceiro aluno:')
n4 = input('digite o quarto aluno: ')
lista = [n1, n2, n3, n4]
print(f'a ordem escolhida foi {random.sample(lista, k=4)}')