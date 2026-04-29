listaA = []
listaB = []
j=1
for i in range(20):
    num = int(input('Bota: '))
    listaA.append(num)

for x in range(j,21):
    men = min(listaA)
    listaA.remove(min(listaA))
    listaB.insert(0,men)
    j+=1
invB = listaB[::-1]
print(invB)

