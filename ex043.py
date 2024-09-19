peso = int(input('qual o seu peso? (kg) '))
altura = float(input('qual a sua altura '))
imc = peso / (altura * altura)
print(f'o imc dessa pessoa é de {imc:.1f}')
if imc <18.5:
    print('voce esta *ABAIXO* do peso normal, cuidado!')
elif imc <=25:
    print('voce esta no *PESO IDEAL*, parabens!')
elif imc <=30:
    print('voce esta em *SOBREPESO*, cuidado')
elif imc <=40:
    print('voce esta em *OBESIDADE*, cuidado!')
else:
    print('voce esta em *OBESIDADE MORBIDA*, muito cuidado!!!')