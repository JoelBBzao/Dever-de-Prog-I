N = int(input('Insira o numero a ser analisado: '))
soma = 0
for x in range(1,N):
    if N%x == 0:
        soma += x
        print(x,end=' ')
if N == soma:
    print()
    print(f'Esse número é perfeito, já que a soma de seus divisores é igual a {N}')
else:
    print()
    print('Esse número não é perfeito')