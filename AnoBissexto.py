from random import randint
from time import sleep
ano = int(input('Qual ano você quer analizar? '))
print(ano)
if ano <=1000:
    bissexto = ano%400
    if bissexto == 0:
        print('Esse ano é bissexto, já que é múltiplo de 400')
    else:
        print('Esse ano não é bissexto pois não é múltiplo de 400')
elif ano >=1000:
    bissexto = ano%4
    if bissexto == 0:
        print('Esse ano é bissexto, já que é múltiplo de 4')
    else:
        print('Esse ano não é bissexto, já que não é múltiplo de 4')