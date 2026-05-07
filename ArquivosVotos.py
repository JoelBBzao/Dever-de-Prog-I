candidatos = []
codigoMen = 0
codigoMais = 0
nulo = 0
maisVot= 0
menosVot= float('inf')
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
cand5 = 0
with open('votos.txt','r') as arq:
    for linha in arq:
        votos = linha.strip()
        match int(votos):
            case 1:
                cand1 +=1
            case 2:
                cand2 +=1
            case 3:
                cand3 +=1
            case 4:
                cand4 +=1
            case 5:
                cand5 +=1
            case _:
                nulo +=1
candidatos.append(cand1)
candidatos.append(cand2)
candidatos.append(cand3)
candidatos.append(cand4)
candidatos.append(cand5)
for i in range(len(candidatos)):
    if candidatos[i]> maisVot:
        maisVot= candidatos[i]
        codigoMais= i+1
    else:
        maisVot= candidatos[i]
    if candidatos[i] < menosVot:
        menosVot= candidatos[i]
        codigoMen = i+1
    else:
        menosVot= menosVot
with open('apuracao.txt','w') as arq:
    arq.write(f'Mais votado: Candidato {codigoMais} com {maisVot} votos\n')
    arq.write(f'Menos votado: Candidato {codigoMen} com {menosVot} votos\n')
    arq.write(f'Houveram {nulo} votos nulos')
arq.close()