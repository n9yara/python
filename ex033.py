n1 = int(input('digite o primero numero: '))
n2 = int(input('digite o segundo nunero: '))
n3 = int(input('digite o terceiro numero '))
lista = [n1,n2,n3]
print(f'O maior valor digitado foi {max(lista)}\nO menor valor foi {sorted(lista)[0]}')
