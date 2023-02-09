import random
from models import Monoplano
from avl import criar_arquivo
from operator import attrgetter
from classe_desempenho import desempenho
# from random import *

n_candidatos = 150
n_selecionados = 25
n_filhos = 50


c_min_w = 0.2
c_max_w = 0.5

b_min_h = 0.1
c_min_h = 0.1
b_max_h = 2
c_max_h = 0.4
ht_max = 0.6

b_min_v = 0.1
c_min_v = 0.1
b_max_v = 0.5
c_max_v = 0.4
lambda_min_v = 0.4
lambda_max_v = 0.95

pos_cp_min = 0.2
pos_cp_max = 0.35

iw_max = 7
ih_max = -7


offset_max = 0.10
n_sect = 3
# dist_nariz = 0.295 
# soma_dims = 3.2 - dist_nariz

altura_max = 0.6
b_min_w = 1.5 #envergadura min
b_max_w = 2.3 #envergadura max
dist_solo_ev_min = 0.06

# perfis_asa = ['FX 74-Cl5-140 MOD (smoothed)', 'S1223 RTL', 'CH10 (smoothed)', 'DAE-21 AIRFOIL', 'WORTMANN FX 63-137 AIRFOIL', 'e423']
# perfis_eh = ['e168', 'e169', 'e479', 'n0012', 'naca0015']
perfis_asa = ['Asa_1', 'Asa_2', 'Asa_3', 'Asa_4']
perfis_eh = ['EH_1', 'EH_2', 'EH_3']
perfis_ev = ['EV_1', 'EV_2', 'EV_3']


# gera aleatpriamente, entre os extremos máximos e minimos os valores dos parâmetros da aeronave
def gerar_inicial(total):
    aeronaves = []
    while len(aeronaves) < total:
        #print("ok1")
        cr = random.uniform(c_min_w, c_max_w)
        cint = random.uniform(c_min_w, cr)
        ct = random.uniform(c_min_w, cint)
        br = random.uniform((b_min_w/2)*0.75, (b_max_w/2)*0.75)
        bt = random.uniform(0.1, b_max_w/2 - br)
        o1 = random.uniform(0, offset_max/10)
        o2 = random.uniform(o1,offset_max/10)
        b = br + bt
        bint = random.uniform(((b - br)*0.3) + br, ((b - br)*0.7) + br)
        
        geometria_asa = [(0, cr, 0), (br, cr, 0), (bint, cint, o1), (b, ct, o2)]

        bh = random.uniform(b_min_h/2, b_max_h/2)
        ch = random.uniform(c_min_h, c_max_h)

        geometria_eh = [(0, ch, 0), (bh, ch, 0)]

        crv = random.uniform(ch, c_max_v)
        lambda_v = random.uniform(lambda_min_v, lambda_max_v)
        ctv = lambda_v*crv
        bv = random.uniform(b_min_v, bh)

        geometria_ev = [(0, crv, 0), (bv, ctv, crv-ctv)]

        iw = round(random.uniform(0, iw_max))
        ih = round(random.uniform(ih_max, 0))

        ht = random.uniform(0, ht_max)
        lt = random.uniform(cr, 1.5 - ch)
        #lt = soma_dims - ch - b*2

        #mtow = random.uniform(mtow_min, mtow_max)

        pos_cp = round(random.uniform(pos_cp_min, pos_cp_max)*cr, 2)

        posicoes = {'asa': (0, 0), 'eh': (lt, ht),
                    'ev': (lt, ht), 'cp': (pos_cp, 0)}
        perfil_asa = random.choice(perfis_asa)
        perfil_eh = random.choice(perfis_eh)
        # preenche o vetor de aeronaves com aeronaves
        perfil_ev = random.choice(perfis_ev)
        try:
            aeronave = Monoplano(geometria_asa, perfil_asa, iw, geometria_eh, perfil_eh, ih, geometria_ev, perfil_ev, posicoes)
            #print("append")
            aeronaves.append(aeronave)
        except:
            continue
        
    return aeronaves


def variar(aeronave, sigma):  # função para variar os paramestros de uma aeronave
    while True:
        #print("Variar")
        geometria_asa = aeronave.geometria_asa.copy()
        geometria_eh = aeronave.geometria_eh.copy()
        geometria_ev = aeronave.geometria_ev.copy()

        br, cr, o1x = geometria_asa[1]
        bint, cint, o1 = geometria_asa[2]
        b, ct, o2 = geometria_asa[3]
        bt = b - br

        ch, bh = geometria_eh[0][1], geometria_eh[1][0]
        crv, ctv, bv = ch, geometria_ev[1][1], geometria_ev[1][0]
        pos_cp = aeronave.posicoes['cp'][0]

        cint = round(trunc_gauss(cint, sigma, c_min_w, cr), 2)
        br = round(trunc_gauss(br, sigma, b_min_w/2, b_max_w/2 - 0.5), 2)
        bt = round(trunc_gauss(bt, sigma, 0.1, b_max_w/2 - bt), 2)
        cr = round(trunc_gauss(cr, sigma, ct, c_max_w), 2)
        o1 = round(trunc_gauss(o1, sigma, 0, offset_max), 2)
        ct = round(trunc_gauss(ct, sigma, c_min_w, cr), 2)
        b = round(bt + br, 2)
        b = round(trunc_gauss(b, sigma, 0.1, 1.15), 2)

        ch = round(trunc_gauss(ch, sigma, c_min_h, c_max_h), 2)
        bh = round(trunc_gauss(bh, sigma, b_min_h/2, b_max_h/2), 2)

        o2 = round(trunc_gauss(o2, sigma, o1, offset_max))
        bint = round(trunc_gauss(bint, sigma,((b - br)*0.3) + br, ((b - br)*0.7) + br), 2)

        lambda_v = ctv/crv
        lambda_v = trunc_gauss(lambda_v, sigma, lambda_min_v, lambda_max_v)
        crv = round(trunc_gauss(crv, sigma, ch, c_max_v), 2)
        ctv = round(lambda_v*crv, 2)
        bv = round(trunc_gauss(bv, sigma, b_min_h, bh), 2)

        iw = round(trunc_gauss(aeronave.iw, sigma*50, 0, iw_max))
        ih = round(trunc_gauss(aeronave.ih, sigma*50, ih_max, 0))

        ht = round(aeronave.posicoes['eh'][1], 2)
        ht = round(trunc_gauss(ht, sigma, 0, cr), 2)

        lt = round(aeronave.posicoes['eh'][0], 2)
        lt = round(trunc_gauss(lt, sigma, cr, 1.5 - ch), 2)

        pos_cp = round(trunc_gauss(pos_cp, sigma, pos_cp_min*cr, pos_cp_max*cr), 2)

        geometria_asa = [(0, cr, 0), (br, cr, 0), (bint, cint, o1), (b, ct, o2)]
        geometria_eh = [(0, ch, 0), (bh, ch, 0)]
        geometria_ev = [(0, crv, 0), (bv, ctv, crv-ctv)]

        posicoes = {'asa': (0, 0), 'eh': (lt, ht),
                    'ev': (lt, ht), 'cp': (pos_cp, 0)}
        try:
            aeronave = Monoplano(geometria_asa, aeronave.perfil_asa, iw, geometria_eh, aeronave.perfil_eh, ih, geometria_ev, aeronave.perfil_ev, posicoes)
            break
        except:
            continue
    return aeronave


def gerarFilho(pai, mae, sigma, indiceMutacao):
    variar = 0
    while True:
        #print("GerarF")
        #print(variar)
        geometria_asaPai = pai.geometria_asa.copy()
        geometria_ehPai = pai.geometria_eh.copy()
        geometria_evPai = pai.geometria_ev.copy()
        geometria_asaMae = mae.geometria_asa.copy()
        geometria_ehMae = mae.geometria_eh.copy()
        geometria_evMae = mae.geometria_ev.copy()
        posicoes_Mae = mae.posicoes.copy()

        #dados da aeronave pai
        # brPai, crPai, o1xPai = geometria_asaPai[1]
        # bintPai, cintPai, o1Pai = geometria_asaPai[2]
        # bPai, ctPai, o2Pai = geometria_asaPai[3]

        # btPai = bPai - brPai
        # chPai, bhPai = geometria_ehPai[0][1], geometria_ehPai[1][0]
        # crvPai, ctvPai, bvPai = chPai, geometria_evPai[1][1], geometria_evPai[1][0]
        # pos_cpPai = pai.posicoes['cp'][0]

        # #dados da aeronave mae
        # brMae, crMae, o1xMae = geometria_asaMae[1]
        # bintMae, cintMae, o1Mae = geometria_asaMae[2]
        # bMae, ctMae, o2Mae = geometria_asaMae[3]

        # bint, cint = bintMae, cintMae
        # btMae = bMae - brMae
        # chMae, bhMae = geometria_ehMae[0][1], geometria_ehMae[1][0]
        # crvMae, ctvMae, bvMae = chMae, geometria_evMae[1][1], geometria_evMae[1][0]
        # pos_cpMae = mae.posicoes['cp'][0]

        # br, bt, cr, o1, ct, o2 = brMae, btMae, crMae, o1Mae, ctMae, o2Mae
        # b = round(bt + br, 2)
        # b = round(trunc_gauss(b, sigma, 0.1, 1.15), 2)

        # ch, bh = chPai, bhPai

        # lambda_v = ctvPai/crvPai

        # crv, ctv, bv = crvMae, ctvMae, bvMae

        # iw, ih = pai.iw, mae.ih

        # ht = round(pai.posicoes['eh'][1], 2)

        # lt = round(mae.posicoes['eh'][0], 2)

        # pos_cp = pos_cpMae

        # geometria_asa = [(0, cr, 0), (br, cr, 0), (bint, cint, o1), (b, ct, o2)]
        # geometria_eh = [(0, ch, 0), (bh, ch, 0)]
        # geometria_ev = [(0, crv, 0), (bv, ctv, crv-ctv)]

        # posicoes = {'asa': (0, 0), 'eh': (lt, ht),
        #             'ev': (lt, ht), 'cp': (pos_cp, 0)}
        try: 
            aeronave = Monoplano(geometria_asaPai, pai.perfil_asa, mae.iw, geometria_ehMae, mae.perfil_eh, pai.ih, geometria_evPai, pai.perfil_ev, posicoes_Mae)
            if indiceMutacao > random.random():
                aeronave = variar(aeronave, sigma)
            #print("ok")
            return aeronave
        except:
            variar += 1
            if variar >= 4:
                return pai
            else:
                continue
            # return pai


def reproducao(gerados, sigma):  # função de reprodução recebe aeronaves
    pais = sorted(gerados, key=lambda a: a.nota_avaliacao, reverse=True)[:n_selecionados]
    filhos = []
    for pai in pais:
        for i in range(int(len(gerados)/len(pais)) - 1):
            filhos.append(variar(pai, sigma))
        filhos.append(pai)
    return filhos

def trunc_gauss(mu, sigma, bottom, top):
    a = random.gauss(mu, sigma)
    if a >= top:
        return top
    if a <= bottom:
        return bottom
    return a

def mediaAvaliacao(aeronaves):
    media = 0
    for aeronave in aeronaves:
        media += aeronave.nota_avaliacao
    return (media/(len(aeronaves)))

def sortear(pais, indice_a_ignorar = -1):
    sigma = len(pais)/20
    continua = True
    while continua:
        indice_sorteado = int(random.gauss(0, sigma))
        if indice_sorteado < 0: indice_sorteado = 0
        elif indice_sorteado > len(pais)-1: indice_sorteado = len(pais)-1
        if indice_sorteado != indice_a_ignorar:
            continua = False
    return indice_sorteado

def selecaoRoleta(pais):
    ordenados = sorted(pais,  key=attrgetter('nota_avaliacao'), reverse=True)
    indice_pai = sortear(ordenados)
    indice_mae = sortear(ordenados, indice_pai)
    pai = pais[indice_pai]
    mae = pais[indice_mae]

    return pai, mae

def reproducao2(populacao, n_filhos, sigma, mutacao = 0.4):
    candidatos = sorted(populacao, key = lambda a : a.nota_avaliacao, reverse = True)[:int(n_filhos/2)]
    filhos = []
    for individuo in candidatos:
        pai, mae = selecaoRoleta(candidatos)
        #print("ok2.1")
        filho1, filho2 = gerarFilho(pai, mae, sigma, mutacao), variar(individuo, sigma)
        if verifica_cond(filho1): filhos.append(filho1)
        if verifica_cond(filho2): filhos.append(filho2)
        # filhos.append(gerarFilho(pai, mae, sigma, mutacao))
        # filhos.append(variar(individuo, sigma))
    return filhos

def verifica_cond(aeronave):
    retorno = True
    if aeronave.altura > altura_max:
        retorno = False
    if aeronave.envergadura > b_max_w:
        retorno = False
    if aeronave.dist_solo_ev < dist_solo_ev_min:
        retorno = False
    return retorno