import re
num = str(input('Digite um numero de 5 dígitos: '))
if re.fullmatch(r'[0-9]+', num):
    if len(num) == 5:
        inverso = num[::-1]
        print(f'O inverso de {num} é {inverso}')
        if inverso == num:
            print('Esse número é palindromo')
        else:
         print('Esse número não é palindromo')
    else:
        print('Por favor, insira um número de 5 dígitos')
else:
    print('Por favor, insira apenas números')
