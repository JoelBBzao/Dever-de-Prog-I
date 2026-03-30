import math
lata = 18 #litros 215 reais
litro = 3#m quadrado
pintor = 8#m quadrado/h 60rs/h
rolos = 12 #(meia hora)

largura = float(input('Largura da parede: '))
comprimento = float(input('Comprimento da parede: '))
altura = float(input('Altura da parede: '))

aP1 = largura * altura
aP2 = comprimento * altura
aTeto = comprimento * largura
aT = aP1*2 + aP2+2 + aTeto
print(f'A área total a ser pintada é {aT} m²')
latas = math.ceil(aT/(18*3))
print(f'A quantidade de latas que serão utilizadas é {latas} ')
vL = latas*215
print(f'O preço gasto em latas será de R${vL:.2f}')
pintorH = math.ceil(aT/8)
print(f'o pintor levará {pintorH} horas')
vP = pintorH*60
print(f'O valor gasto com o pintor será de R${vP}')
valorRolo = pintorH*12*2
print(f'Serão gastos R${valorRolo:.2f} em rolos')
ValorTotal = vL+vP+valorRolo
print(f'O valor total gasto com essa reforma é de R${ValorTotal:.2f}')

