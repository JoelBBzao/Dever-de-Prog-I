A = int(input('Insira um numero inteiro: '))
Fat = A
F = 1
print(f'O resultado de {A}! é = ', end='')
while Fat > 0:
    print(f'{Fat}', end='')
    print(' x ' if Fat > 1 else ' = ' , end='')
    F *= Fat
    Fat -= 1
print(F)
