s1 = int(input('primeiro segmento: '))
s2 = int(input('segundo segmento: '))
s3 = int(input('terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triangulo!')
    if s1 ==  s2 == s3:
        print('*EQUILATERO*')
    elif s1 != s2 != s3 != s1:
        print('*ESCALENO*') 
    else:
        print('*ISOCELES*')
else:
    print('Os segmentos acima não podem formar um triangulo!')


