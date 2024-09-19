nome = str(input('digite seu nome: '))
upper = nome.upper()
lower = nome.lower()
letras = len(nome) - nome.count(' ')
first = nome.split()[0]
print(f'Seu nome em maiusculas é {upper}\nSeu nome em minusculas é {lower}\nSeu nome ao todo tem {letras} letras\nSeu primeiro nome é {first}')
      