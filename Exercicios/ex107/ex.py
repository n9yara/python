import numeros

p = float(input("Digite um valor:"))
print(f"A metade de {p} é {numeros.metade(p)}")
print(f"O dobro de {p} é {numeros.dobro(p)}")
print(f"Aumentando 10% fica {numeros.aumentar(p, 10)}")
print(f"Diminuindo 5% fica {numeros.diminuir(p, 5)}")