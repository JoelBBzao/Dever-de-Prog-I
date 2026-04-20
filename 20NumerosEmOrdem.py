lista = []

for k in range(20):
    num = int(input(f'Insira o {k+1}° número: '))
    p=0
    while p < len(lista) and num > lista[p]:
        p+=1
    lista.insert(p, num)
print(lista)

