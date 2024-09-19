
lista = []
s = 0
cont = 0
while True:
    num = (int(input('Digite o numero ')))
    lista.append(num)
    s += num
    cont += 1
    res = str(input('Quer continuar?[S/N] ')).upper()
    maior = max(lista)
    menor = min(lista)
   
    if res == 'N':
        break
print(f'Voce digitou {cont} numeros e a media deles foi {s/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')