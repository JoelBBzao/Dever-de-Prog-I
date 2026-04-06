#Faça um algoritmo que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
mes = int(input('Insira o número a ser analisado: '))
if mes <=0 or mes >=13:
    print('Não existe um mês correspondente á esse número!')
else:
    if mes == 1:
         print('O número analisado corresponde ao mês de janeiro')
    elif mes == 2:
        print('O número analisado corresponde ao mês de fevereiro')
    elif mes == 3:
        print('O número analisado corresponde ao mês de março')
    elif mes == 4:
        print('O número analisado corresponde ao mês de abril')
    elif mes == 5:
        print('O número analisado corresponde ao mês de maio')
    elif mes == 6:
        print('O número analisado corresponde ao mês de junho')
    elif mes == 7:
        print('O número analisado corresponde ao mês de julho')
    elif mes == 8:
        print('O número analisado corresponde ao mês de agosto')
    elif mes == 9:
        print('O número analisado corresponde ao mês de setembro')
    elif mes == 10:
        print('O número analisado corresponde ao mês de outubro')
    elif mes == 11:
        print('O número analisado corresponde ao mês de novembro')
    elif mes == 12:
        print('O número analisado corresponde ao mês de dezembro')