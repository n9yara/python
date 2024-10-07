def leiainteiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric:
            valor = int(n)
            ok = True
        else:
            print("ERROR, digite um numero inteiro")
        if ok:
            break
    return valor


n = leiainteiro("digite um numero: ")
print(f"voce acabou de digitar o numero {n}")