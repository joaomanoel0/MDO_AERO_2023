import subprocess

perfis_asa = ['FX 74-Cl5-140 MOD (smoothed)', 'S1223 RTL', 'CH10 (smoothed)', 'DAE-21 AIRFOIL', 'WORTMANN FX 63-137 AIRFOIL', 'e423']
perfis_eh = ['e168', 'e169', 'e479', 'n0012', 'naca0015']

for eh in perfis_eh:
    processos = []
    for asa in perfis_asa:
        processos.append(subprocess.Popen(['python', 'main.py', asa, eh]))
    for p in processos:
        p.wait()
    print(eh, 'pronto')
        