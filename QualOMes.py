#Faça um algoritmo no qual o usuário digite um número inteiro entre 1 e 365,
#representando os dias do ano. O programa deve responder em qual mês fica o dia
#indicado pelo usuário.
dia = int(input('Digite o dia que voce deseja analisar: '))
if dia == 0 or dia >= 366:
    print('Esse dia não existe, engraçadinho!')
if dia >= 1 and dia <= 31:
    print('O dia analisado cairá em janeiro!')
elif dia >= 32 and dia <= 59:
    print('O dia analisado cairá em fevereiro!')
elif dia >= 60 and dia <= 90:
    print('O dia analisado cairá em março!')
elif dia >= 91 and dia <= 120:
    print('O dia analisado cairá em abril!')
elif dia >= 121 and dia <= 151:
    print('O dia analisado cairá em maio!')
elif dia >= 152 and dia <= 181:
    print('O dia analisado cairá em junho!')
elif dia >= 182 and dia <= 212:
    print('O dia analisado cairá em julho!')
elif dia >= 213 and dia <= 243:
    print('O dia analisado cairá em agosto!')
elif dia >= 244 and dia <= 273:
    print('O dia analisado cairá em setembro!')
elif dia >= 274 and dia <= 304:
    print('O dia analisado cairá em outubro!')
elif dia >= 305 and dia <= 334:
    print('O dia analisado cairá em novembro!')
else:
    print('O dia analisado cairá em dezembro!')
