from lib import interface
from lib import arquivo


arq = 'db.txt'
if not arquivo.arquivo(arq):
    arquivo.criaraquivo(arq)
while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        arquivo.lerarquivo(arq)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('ERRO: Digite uma opção valida!')