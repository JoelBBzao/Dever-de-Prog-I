maiorNum = 0
for n in range(10):
    num = int(input(f'Digite o {n+1}° número: '))
    if num > maiorNum:
        segundoNum = maiorNum
        maiorNum = num
    else:
        maiorNum = maiorNum
print(f'O segundo maior número é {segundoNum}')