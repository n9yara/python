print('='*25)
print('Analisador de triangulos')
print('='*25)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
soma = (s1+s2)
if soma > s3:
    print('Os segmentos acima podem formar um triangulo!')
else:
    soma < s3
    print('Os segmentos acima não podem formar um triangulo!')