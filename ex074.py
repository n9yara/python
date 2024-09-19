from random import sample

sort = tuple(sample(range(10), 5))
print(sort)
print(f'O menor valor foi {min(sort)}')
print(f'E o menor valor foi {max(sort)}')
