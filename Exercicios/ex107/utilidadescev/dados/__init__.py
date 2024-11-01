def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('Preço invalido')
        else:
            valido=True
            return float(entrada)