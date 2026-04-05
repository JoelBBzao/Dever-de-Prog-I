#Faça um algoritmo que leia três números reais A, B, C e mostre o resultado, em ordem
#crescente, de todas as possíveis divisões entre dois destes números.
A = int(input('Valor de A: '))
B = int(input('Valor de B: '))
C = int(input('Valor de C: '))
divisao1 = A/B
divisao2 = A/C
divisao3 = B/A
divisao4 = B/C
divisao5 = C/A
divisao6 = C/B
divisoes = [divisao6, divisao5, divisao4, divisao3, divisao2, divisao1]
divisoes.sort()
print(divisoes)
