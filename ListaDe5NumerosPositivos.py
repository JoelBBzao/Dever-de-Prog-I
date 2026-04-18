lista = []
for x in range(5):
    num = int(input('Digite um número: '))
    if num <= -1:
        print('insira números positivos')
    elif num == 0:
        break
    else:
        lista.append(num)
if len(lista) == 5:
    for i in range(5):
        print(f'{lista[i]}')
    lista.clear()
else:
    print(lista)
