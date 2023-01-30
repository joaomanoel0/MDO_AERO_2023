from models import Monoplano
from matplotlib import pyplot as plt
import optimizer
import avl
import os
import random
import pickle
import sys
import shutil

optimizer.perfis_asa[0] = sys.argv[1]
optimizer.perfis_eh[0] = sys.argv[2]
print(optimizer.perfis_asa[0], optimizer.perfis_eh[0])

code = optimizer.perfis_asa[0] + '-' + optimizer.perfis_eh[0] + '-' + str(random.randint(100, 999))
os.mkdir('./avl/configs/'+code+'/')
os.mkdir('./avl/configs/%s/geracao-%d' % (code, 0))

avl.caminho_geometrias = './avl/configs/%s/geracao-%d/' % (code, 0)

inicial = optimizer.gerar_inicial(300)

candidatos = sorted(inicial, key = lambda a : a.nota, reverse = True)[:optimizer.n_candidatos]
#print("avaliação total 1: ")
#print(optimizer.avaliacaoTotal(inicial))
ant = 0
n = 80
nota_ant = -1000
notas = []
for j in range(n):
    os.mkdir('./avl/configs/%s/geracao-%d' % (code, j+1))
    avl.caminho_geometrias = './avl/configs/%s/geracao-%d/' % (code,j + 1)
    candidatos = optimizer.reproducao2(candidatos, optimizer.n_filhos, 0.01)

    # print("Avaliação total |G", j+1, "| : ")
    # print(optimizer.mediaAvaliacao(candidatos))

#    print("Teste |G", j, "| : ")
#    [pai, mae] = optimizer.selecaoRoleta(candidatos)
#    print("Pai selecionado: ", pai.nota)
#    print("Pai selecionado: ", mae.nota)

    melhor = max(candidatos, key= lambda a : a.nota)
    print(optimizer.perfis_asa[0], optimizer.perfis_eh[0], "geração %d: %.3f" % (j+1, melhor.nota), " | Nota na competição: ", melhor.nota_avaliacao)
    print("xcp = %.3f CLmax = %.4f atrim = %.3f Sw = %.3f ME = %.2f%% CP = %.2f pouso = %.2f decolagem = %.2f cma = %.2f arw = %.3f arh = %.3f mtow = %.3f" % (melhor.posicoes['cp'][0], melhor.CLmax, melhor.atrim, melhor.Sw, melhor.ME*100, melhor.carga_paga, melhor.x_pouso, melhor.x_decolagem, melhor.CMa *180/3.1416, melhor.ARw, melhor.ARh, melhor.mtow))
    print("Média da geração: ", optimizer.mediaAvaliacao(candidatos))
    notas.append(melhor.nota)
    arq_melhor = open('./avl/configs/%s/geracao-%d-melhor.pyobj' % (code, j + 1), 'wb')
    pickle.dump(melhor, arq_melhor)
    arq_melhor.close()
    shutil.rmtree('./avl/configs/%s/geracao-%d/' % (code, j + 1))
    if abs(melhor.nota - sum(notas)/10) < 0.5 and len(notas) == 10:
        break
    if len(notas) == 10:
        notas.pop(0)

candidatos.sort(key=lambda a : a.nota, reverse=True)
os.mkdir('./avl/configs/%s/resultado' % code)
avl.caminho_geometrias = './avl/configs/%s/resultado/' % code
i = 1
for melhor in candidatos[:10]:
    melhor.nome = '%d'%i
    i += 1
    arq_melhor = open('./avl/configs/%s/resultado/%s.pyobj' % (code, melhor.nome), 'wb')
    pickle.dump(melhor, arq_melhor)
    arq_melhor.close()
    print("%s\n  cw = %.3f CL/CD = %.4f atrim = %.3f Sw = %.3f ME = %.2f%% PV = %.2f pouso = %.2f decolagem = %.2f perf = %s arw = %.3f arh = %.3f" % (melhor.nome, melhor.cw, melhor.CL_CD, melhor.atrim, melhor.Sw, melhor.ME*100, melhor.peso_vazio, melhor.x_pouso, melhor.x_decolagem, melhor.perfil_asa, melhor.ARw, melhor.ARh))
    avl.criar_arquivo(melhor, False)