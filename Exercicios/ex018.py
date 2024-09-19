import math
angulo = float(input('digite o angulo que vc deseja: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O angulo de {angulo} tem o SENO de {seno:.2F}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2F}')
print(f'O angulo de {angulo} tem o TANGENT de {cosseno:.2F}')

