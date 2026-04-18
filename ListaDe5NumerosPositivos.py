listaA = []
listaB = []
listaC = []

for x in range(5):
    num = int(input('Digite um número para A: '))
    listaA.append(num)
print(listaA)

for x in range(5):
    num = int(input('Digite um número para B: '))
    listaB.append(num)
print(listaB)
listaC.extend(listaA)
listaC.extend(listaB)
for x in (listaC):
    while p < len(listaC) and num > listaC[p]:
        p += 1
    listaC.insert(p, listaC[x])
print(listaC)

