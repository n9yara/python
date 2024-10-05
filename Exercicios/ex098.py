from time import sleep

def contador(i, f, p):
    print(f"\ncontagem de {i} até {f} de {p} em {p}")

    if p <0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f" {cont} ", end="", flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f" {cont} ", end="", flush=True)
            sleep(0.5)
            cont -= p


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input("\nInicio: "))
fim = int(input("\nFim: "))
passo = int(input("\nPasso: "))
contador(inicio,fim,passo)