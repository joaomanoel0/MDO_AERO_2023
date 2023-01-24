from models import Monoplano
import pickle
import matplotlib.pyplot as plt
from avl import resultados_avl
import csv

caminho = r"C:/Users/rubem/Documents/git/mdo/avl/configs/e423-e168-900/resultado/"
csvwriter = csv.writer(open('e423-e168-900.csv', 'w'))
csvwriter.writerow(['rank', 'cr', 'ct', 'br', 'bt', 'ch', 'bh', 'crv', 'ctv', 'bv','zt', 'xt', 'xcp', 'xcg', 'ARw', 'ARh', 'PV', 'CP', 'ME', 'dec', 'pouso', 'atrim', 'perfil_asa', 'perfil_ev'])
for i in range(10):
    aeronave = pickle.load(open(caminho + str(i + 1) + '.pyobj', 'rb'))
    cr = aeronave.geometria_asa[0][1]
    ct = aeronave.geometria_asa[-1][1]
    br = aeronave.geometria_asa[1][0]
    bt = aeronave.geometria_asa[-1][0] - br
    ch = aeronave.geometria_eh[0][1]
    bh = aeronave.geometria_eh[1][0]
    crv = aeronave.geometria_ev[0][1]
    ctv = aeronave.geometria_ev[1][1]
    bv = aeronave.geometria_ev[1][0]
    zt = aeronave.posicoes['eh'][1]
    xt = aeronave.posicoes['eh'][0]
    xcp = aeronave.posicoes['cp'][0]
    xcg = aeronave.xcg
    ARw = aeronave.ARw
    ARh = aeronave.ARh
    PV = aeronave.peso_vazio
    CP = aeronave.carga_paga
    ME = aeronave.ME
    dec = aeronave.x_decolagem
    pouso = aeronave.x_pouso
    atrim = aeronave.atrim
    perfil_asa = aeronave.perfil_asa
    perfil_eh = aeronave.perfil_eh
    csvwriter.writerow([i, cr, ct, br, bt, ch, bh, crv, ctv, bv, zt, xt, xcp, xcg, ARw, ARh, PV, CP, ME, dec, pouso, atrim, perfil_asa, perfil_eh])

