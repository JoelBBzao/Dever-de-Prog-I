A = 5000000
B = 7000000
ano = 0
while A<=B:
    natA = A * 1.003
    natB = B * 1.002
    A = natA
    B = natB
    ano += 1
print(f'Demorou {ano} anos para o país A superar a população do país B')