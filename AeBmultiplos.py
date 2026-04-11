A = int(input('Insira um numero para A que seja igual ou menos a B: '))
B = int(input('Insira um numero para B: '))
qtd = 0
soma = 0
if A > B:
    print('O A precisa ser menor que o B')
else:
    for x in range (A,B):
        if x%3 == 0 or x%5 == 0 or x%7 == 0:
            print(x, end=' ')
            qtd += 1
            soma += x
print()
print(soma)
print(f'Quantidade total de multiplos: {qtd}')