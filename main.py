from models import Monoplano
from matplotlib import pyplot
import numpy as np
import optimizer
import avl
import os
import random
import pickle
import sys
import shutil

# optimizer.perfis_asa[0] = sys.argv[1]
# optimizer.perfis_eh[0] = sys.argv[2]
# print(optimizer.perfis_asa[0], optimizer.perfis_eh[0])
P_asa = sys.argv[1]
P_eh = sys.argv[2]
print(P_asa, P_eh)

code = P_asa + '-' + P_eh + '-' + str(random.randint(100, 999))
os.mkdir('./avl/configs/'+code+'/')
os.mkdir('./avl/configs/%s/geracao-%d' % (code, 0))

avl.caminho_geometrias = './avl/configs/%s/geracao-%d/' % (code, 0)

media_notas = []
inicial = optimizer.gerar_inicial(100)
media_notas.append(optimizer.mediaAvaliacao(inicial))

candidatos = sorted(inicial, key = lambda a : a.nota, reverse = True)[:optimizer.n_candidatos]
ant = 0
n = 2
nota_ant = -1000
notas = []
melhores_geracao = []

for j in range(n):
    os.mkdir('./avl/configs/%s/geracao-%d' % (code, j+1))
    avl.caminho_geometrias = './avl/configs/%s/geracao-%d/' % (code,j + 1)
    candidatos = optimizer.reproducao2(candidatos, optimizer.n_filhos, 0.01)

    melhor = max(candidatos, key= lambda a : a.nota_avaliacao)
    print(melhor.perfil_asa, melhor.perfil_eh, melhor.perfil_ev, "geração %d: %.3f" % (j+1, melhor.nota), " | Nota na competição: ", melhor.nota_avaliacao)
    print("xcp = %.3f CLmax = %.4f atrim = %.3f Sw = %.3f ME = %.2f%% CP = %.2f pouso = %.2f decolagem = %.2f cma = %.2f arw = %.3f arh = %.3f mtow = %.3f" % (melhor.posicoes['cp'][0], melhor.CLmax, melhor.atrim, melhor.Sw, melhor.ME*100, melhor.cp, melhor.x_pouso, melhor.x_decolagem, melhor.CMa *180/3.1416, melhor.ARw, melhor.ARh, melhor.mtow))
    print("Média da geração: ", optimizer.mediaAvaliacao(candidatos))
    media_notas.append(optimizer.mediaAvaliacao(candidatos))
    notas.append(melhor.nota_avaliacao)
    melhores_geracao.append(melhor)
    arq_melhor = open('./avl/configs/%s/geracao-%d-melhor.pyobj' % (code, j + 1), 'wb')
    pickle.dump(melhor, arq_melhor)
    arq_melhor.close()
    shutil.rmtree('./avl/configs/%s/geracao-%d/' % (code, j + 1))
    # if abs(melhor.nota_avaliacao - sum(notas)/10) < 0.5 and len(notas) == 10:
    #     break
    # if len(notas) == 10:
    #     notas.pop(0)

candidatos.sort(key=lambda a : a.nota_avaliacao, reverse=True)
os.mkdir('./avl/configs/%s/resultado' % code)
avl.caminho_geometrias = './avl/configs/%s/resultado/' % code
i = 1
for melhor in candidatos[:20]:
    melhor.nome = '%d'%i
    i += 1
    arq_melhor = open('./avl/configs/%s/resultado/%s.pyobj' % (code, melhor.nome), 'wb')
    pickle.dump(melhor, arq_melhor)
    arq_melhor.close()
    print("%s\n  cw = %.3f CL/CD = %.4f atrim = %.3f Sw = %.3f ME = %.2f%% Mtow = %.4f pouso = %.2f decolagem = %.2f perf = %s arw = %.3f arh = %.3f" % (melhor.nome, melhor.cw, melhor.CL_CD, melhor.atrim, melhor.Sw, melhor.ME*100, melhor.mtow, melhor.x_pouso, melhor.x_decolagem, melhor.perfil_asa, melhor.ARw, melhor.ARh))
    print("perfis asa: ", melhor.geometria_asa)
    print("perfis ev: ", melhor.geometria_ev)
    print("perfis eh: ", melhor.geometria_eh)
    print("Posicoes eh: ", melhor.posicoes["eh"])
    print("Posicoes ev: ", melhor.posicoes["ev"])
    print("Largura: ", melhor.lagura_asa)
    print("Largura: ", melhor.lagura_asa)
    print("Pos eh: ", melhor.pos_eh)
    print("Envergadura: ", melhor.envergadura)
    print("Solo ev: ", melhor.dist_solo_ev)
    avl.criar_arquivo(melhor, False)

melhores_geracao.sort(key=lambda a : a.nota, reverse=True)
os.mkdir('./avl/configs/%s/melhores_geracao' % code)
avl.caminho_geometrias = './avl/configs/%s/melhores_geracao/' % code
i = 1
for melhor in melhores_geracao:
    melhor.nome = '%d'%i
    i += 1
    arq_melhor = open('./avl/configs/%s/resultado/%s.pyobj' % (code, melhor.nome), 'wb')
    pickle.dump(melhor, arq_melhor)
    arq_melhor.close()
    print("%s\n  cw = %.3f CL/CD = %.4f atrim = %.3f Sw = %.3f ME = %.2f%% Mtow = %.4f pouso = %.2f decolagem = %.2f perf = %s arw = %.3f arh = %.3f xcg = %.4f" % (melhor.nome, melhor.cw, melhor.CL_CD, melhor.atrim, melhor.Sw, melhor.ME*100, melhor.mtow, melhor.x_pouso, melhor.x_decolagem, melhor.perfil_asa, melhor.ARw, melhor.ARh, melhor.xcg))
    print("perfis asa: ", melhor.geometria_asa)
    print("perfis ev: ", melhor.geometria_ev)
    print("perfis eh: ", melhor.geometria_eh)
    print("Posicoes ev: ", melhor.posicoes["ev"])
    print("Posicoes eh: ", melhor.posicoes["eh"])
    print("\nAltura: ", melhor.altura)
    print("Largura: ", melhor.lagura_asa)
    print("Pos eh: ", melhor.pos_eh)
    print("Envergadura: ", melhor.envergadura)
    print("Solo ev: ", melhor.dist_solo_ev)
    avl.criar_arquivo(melhor, False)

size = 5.0
x = np.arange(0, len(media_notas), 1)
y = media_notas
pyplot.figure(figsize=(2*size,size))
pyplot.xlabel('Geração', fontsize=16)
pyplot.ylabel('Média de notas', fontsize=16)
pyplot.title(label="Evolução da média de notas")
pyplot.plot(x,y)
pyplot.savefig('Evolução da avaliação.png', format = 'png')