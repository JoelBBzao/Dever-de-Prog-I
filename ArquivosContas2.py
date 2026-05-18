numero = []
operadores = []
i = 0
equa = 0
soma = 0
with open('conta.txt ','r')as arq:
    for linha in arq:
        numero.append(linha.strip())
print(numero)
while i+2<len(numero):
    for i in range(1,len(numero),2):
        print(f'soma:{soma} i-1: {i-1}  i:{i}, i+1:{i+1}')
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