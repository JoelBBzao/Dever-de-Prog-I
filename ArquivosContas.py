numero = []
operadores = []
op = 0
with open('conta.txt ','w')as arq:
    while op != '=':
        num = input('Insira um número: ')
        arq.write(num)
        op = input('Insira um operador: ')
        arq.write('\n')
        arq.write(op)
        arq.write('\n')
arq.close()