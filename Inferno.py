#Faça um programa que peça ao usuário para digitar 30 números reais e informe na tela
#qual par de números digitados consecutivamente (um depois do outro) teve a maior
#soma.
X = [0] * 30
p = 0
maiorSoma = -10000
for i in range(30):
    X[i] = float(input(f'Digite o {i+1}° número: '))
    soma = X[i] + X[i+p]
    if i <= 28:
        p = 1
    else:
        p = 0
if soma > maiorSoma:
    maiorSoma = soma
else:
    maiorSoma = maiorSoma
print(f'A maior soma de dois números consecutivos é {maiorSoma}')

