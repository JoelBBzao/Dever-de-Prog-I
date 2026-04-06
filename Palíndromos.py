import numbers
num = str(input('Digite um numero de 5 dígitos: '))
if len(num) == 5:
    inverso = num[::-1]
    print(f'O inverso de {num} é {inverso}')
    if inverso == num:
     print('Esse número é palindromo')
    else:
     print('Esse número não é palindromo')
elif num != numbers: #Como eu faço para só conter números?
    print('Insira apenas números')
else:
    print('Por favor, insira um número de 5 dígitos')

