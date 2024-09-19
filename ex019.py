import random
um = input('digite o primeiro aluno: ')
dois = input('digite o segundo aluno: ')
tres = input('digite o terceiro aluno: ')
quarto = input('digite o quarto aluno: ')
lista = [um, dois, tres, quarto]
print(f'O aluno escolhido foi {random.sample(lista, k=4)}')