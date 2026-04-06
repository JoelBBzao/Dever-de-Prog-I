mes = int(input('Insira o número a ser analisado: '))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
num = 0 + mes
if mes <=0 or mes >=13:
    print('Não existe um mês correspondente á esse número!')
else:
    num = mes
    print(f'O número analisado corresponde ao mês de {meses[num-1]}')
