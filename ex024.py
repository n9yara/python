cidade = input('Em que cidade voce nasceu? ')
cidade = cidade.split()[0]
find = 'santo' in cidade.lower()
print(find)