salario = float(input('qual o salario do funcionario? '))
dez = salario + (salario* 10 / 100)
quinze = salario + (salario * 15 / 100)
if salario >1250:
    print(f'quem ganhava {salario}R$ vai ganhar {dez}R$')
else:
    salario <=1250
    print(f'quem ganhava {salario}R$ vai ganhar {quinze}R$')
