import random


palpite = random.randint(0,10)
tentativas = 0
while True:
 tentativas += 1
 advinhar = int(input('Sou seu computador...\nEstou pensando em um numero entre 0 e 10.\nSerá que voce consegue advinhar qual foi?\nQual seu palpite? '))
 if palpite == advinhar:
    print(f'Acertou depois de {tentativas} tentativas!\n')
    break
 else:
   print(f'Resposta errada, tente novamente!\n')