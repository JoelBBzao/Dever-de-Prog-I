str = input('Digite uma sequência de letras: ').upper()
cont = 1
for i in range(1,len(str)):
    if str[i] == str[i-1]:
        cont +=1
    else:
        print(F'{cont}{str[i-1]}',end='')
        cont=1

print(F'{cont}{str[i-1]}')