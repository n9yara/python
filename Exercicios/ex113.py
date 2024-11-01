def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('**digite um valor inteiro valido**')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'***DIgite um valor float valido***')
            continue
        else:
            return n



num = leiafloat('digite um numero: ')
print(f'o valor digitado foi {num}')