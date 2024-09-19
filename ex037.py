num = int(input('digite um numero inteiro: '))
opcao = int(input('Escolha uma das bases para conversão:\n[1] converter para BINARIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL\nSua opção: '))
if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])