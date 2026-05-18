numero = []
operadores = []
op = 0
i = 0
equa = 0
soma = 0
with open('conta.txt ','w')as arq:
    while op != '=':
        num = input('Insira um número: ')
        arq.write(num)
        op = input('Insira um operador: ')
        arq.write('\n')
        arq.write(op)
        arq.write('\n')
arq.close()

with open('conta.txt ','r')as arq:
    for linha in arq:
        numero.append(linha.strip())
while i+2<len(numero):
    for i in range(1,len(numero),2):

        if numero[i] == '*':
            equa = float(numero[i-1]) * float(numero[i+1])
            soma += equa
        if numero[i] == '/':
            equa = float(numero[i - 1]) / float(numero[i + 1])
            soma += equa
        if numero[i] == '+':
            equa = float(numero[i - 1]) + float(numero[i + 1])
            soma += equa
        if numero[i] == '-':
            equa = float(numero[i - 1]) - float(numero[i + 1])
            soma += equa
print(f'{soma-3:.1f}')