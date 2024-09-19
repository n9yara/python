n1 = int(input('digite o primero valor: '))
n2 = int(input('digite o segundo valor: '))
while True:
    opcao = str(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] fechar o programa\n>>>>Qual sua opção? '))
    if opcao == '1':
        print(f'A soma entre {n1} + {n2} deu {n1+n2}')
        print('='*27)
    elif opcao == '2':
        print(f'A multiplicação de {n1} x {n2} deu {n1*n2}')
        print('='*27)
    elif opcao == '3':
        maior = max(n1,n2)
        print(f'Entre {n1} e {n2} o maior numero foi {maior}')
        
    elif opcao == '4':
        n1 = int(input('digite o primero valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif opcao == '5':
        print('='*27)
        break
    else:
        print('digitaSERTo')

          
