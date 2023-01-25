# Classe das curvas de tração, potência e R/C do MDO 2023

import numpy as np

class curvas:

    def tracao(self, V):
        n = 2  # Número de grau do polinômio

        if self.prop == '14x7':
            
            x_14x7 = np.array([0.00,1.16,2.28,3.44,4.56,5.72,6.88,8.00,9.16,10.28,11.44,12.61,13.72,14.89,16.05,17.17,18.33,19.45,20.61,21.77,22.89,24.05,25.17,26.33,27.49,28.61,29.77,30.89,32.05,33.21])
            y_14x7 = np.array([32.868,32.525,32.112,31.627,31.080,30.470,29.803,29.069,28.268,27.405,26.476,25.479,24.421,23.295,22.108,20.858,19.559,18.233,16.877,15.484,14.070,12.615,11.138,9.630,8.091,6.521,4.924,3.301,1.655,-0.009])
            yS_14x7 = np.array([31.017,30.693,30.303,29.845,29.329,28.754,28.124,27.432,26.676,25.862,24.985,24.044,23.045,21.983,20.862,19.683,18.457,17.206,15.926,14.612,13.277,11.905,10.511,9.088,7.636,6.154,4.647,3.115,1.562,-0.008])
            yI_14x7 = np.array([29.246,28.941,28.573,28.141,27.655,27.112,26.519,25.866,25.153,24.385,23.558,22.671,21.729,20.728,19.671,18.559,17.403,16.224,15.017,13.778,12.519,11.225,9.911,8.569,7.200,5.802,4.382,2.937,1.472,-0.008])

            z_14x7 = np.polyfit(x_14x7,y_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
            zS_14x7 = np.polyfit(x_14x7,yS_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
            zI_14x7 = np.polyfit(x_14x7,yI_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

            p_14x7 = np.poly1d(z_14x7) # Função ajustada para rho = 1.225kg/m³
            pS_14x7 = np.poly1d(zS_14x7) # Função ajustada para rho = 1.156kg/m³
            pI_14x7 = np.poly1d(zI_14x7) # Função ajustada para rho = 1.090kg/m³
            
            if self.rho == 1.225:
                return p_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
            elif self.rho == 1.156:
                return pS_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
            elif self.rho == 1.090:
                return pI_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

        if self.prop == '15x7':

            x_15x7 = np.array([0.00,1.16,2.32,3.49,4.65,5.81,6.97,8.14,9.30,10.42,11.58,12.74,13.90,15.06,16.23,17.39,18.55,19.71,20.88,22.04,23.20,24.36,25.53,26.69,27.85,29.01,30.13,31.29,32.45,33.62])
            y_15x7 = np.array([42.543,41.942,41.262,40.523,39.718,38.842,37.890,36.867,35.773,34.603,33.362,32.045,30.657,29.198,27.677,26.089,24.461,22.802,21.107,19.363,17.579,15.720,13.905,12.010,10.075,8.114,6.121,4.057,2.068,0.000])
            yS_15x7 = np.array([40.146,39.580,38.938,38.241,37.481,36.654,35.756,34.790,33.758,32.654,31.483,30.240,28.930,27.553,26.118,24.619,23.083,21.517,19.918,18.272,16.589,14.835,13.122,11.334,9.508,7.657,5.776,3.828,1.952,0.000])
            yI_15x7 = np.array([37.854,37.320,36.714,36.057,35.341,34.561,33.714,32.804,31.830,30.789,29.685,28.513,27.279,25.980,24.627,23.214,21.765,20.289,18.781,17.229,15.642,13.988,12.373,10.687,8.965,7.219,5.446,3.610,1.840,0.000])

            z_15x7 = np.polyfit(x_15x7,y_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
            zS_15x7 = np.polyfit(x_15x7,yS_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
            zI_15x7 = np.polyfit(x_15x7,yI_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

            p_15x7 = np.poly1d(z_15x7) # Função ajustada para rho = 1.225kg/m³
            pS_15x7 = np.poly1d(zS_15x7) # Função ajustada para rho = 1.156kg/m³
            pI_15x7 = np.poly1d(zI_15x7) # Função ajustada para rho = 1.090kg/m³

            if self.rho == 1.225:
                return p_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
            elif self.rho == 1.156:
                return pS_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
            elif self.rho == 1.090:
                return pI_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

        if self.prop == '15x10':
            
            x_15x10 = np.array([0.00,1.52,3.08,4.60,6.12,7.69,9.21,10.77,12.29,13.81,15.38,16.90,18.42,19.98,21.50,23.07,24.59,26.11,27.67,29.19,30.71,32.28,33.80,35.32,36.88,38.40,39.96,41.48,43.00,44.57])
            y_15x10 = np.array([46.751,46.729,46.684,46.604,46.493,46.337,46.128,45.803,45.270,44.398,43.223,41.844,40.314,38.615,36.760,34.767,32.637,30.386,28.104,25.786,23.420,21.000,18.536,16.022,13.478,10.867,8.216,5.511,2.771,0.000])
            yS_15x10 = np.array([44.117,44.096,44.055,43.979,43.874,43.727,43.530,43.223,42.720,41.897,40.789,39.487,38.043,36.440,34.690,32.809,30.798,28.674,26.521,24.334,22.101,19.817,17.492,15.120,12.719,10.255,7.753,5.201,2.615,0.000])
            yI_15x10 = np.array([41.599,41.579,41.539,41.468,41.369,41.231,41.045,40.756,40.281,39.505,38.460,37.233,35.871,34.359,32.709,30.936,29.040,27.037,25.007,22.945,20.839,18.686,16.493,14.257,11.993,9.669,7.310,4.904,2.466,0.000])

            z_15x10 = np.polyfit(x_15x10,y_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
            zS_15x10 = np.polyfit(x_15x10,yS_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
            zI_15x10 = np.polyfit(x_15x10,yI_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

            p_15x10 = np.poly1d(z_15x10) # Função ajustada para rho = 1.225kg/m³
            pS_15x10 = np.poly1d(zS_15x10) # Função ajustada para rho = 1.156kg/m³
            pI_15x10 = np.poly1d(zI_15x10) # Função ajustada para rho = 1.090kg/m³

            if self.rho == 1.225:
                return p_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
            elif self.rho == 1.156:
                return pS_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
            elif self.rho == 1.090:
                return pI_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

        if self.prop == '16x8':

            x_16x8 = np.array([0.00,1.30,2.59,3.89,5.19,6.48,7.78,9.07,10.37,11.67,13.01,14.30,15.60,16.90,18.19,19.49,20.79,22.08,23.38,24.68,25.97,27.27,28.57,29.86,31.16,32.45,33.75,35.05,36.34,37.64])
            y_16x8 = np.array([57.671,57.128,56.390,55.474,54.420,53.267,52.009,50.634,49.157,47.578,45.888,44.091,42.191,40.190,38.099,35.919,33.664,31.378,29.038,26.649,24.203,21.716,19.172,16.596,13.950,11.254,8.492,5.703,2.860,0.000])
            yS_16x8 = np.array([54.423,53.911,53.214,52.349,51.354,50.267,49.079,47.782,46.388,44.898,43.303,41.607,39.815,37.926,35.953,33.896,31.768,29.610,27.402,25.148,22.840,20.493,18.092,15.661,13.164,10.620,8.013,5.381,2.699,0.000])
            yI_16x8 = np.array([51.316,50.833,50.176,49.360,48.422,47.397,46.277,45.054,43.740,42.335,40.831,39.232,37.542,35.761,33.900,31.961,29.954,27.920,25.838,23.712,21.536,19.323,17.059,14.767,12.412,10.014,7.556,5.074,2.545,0.000])

            z_16x8 = np.polyfit(x_16x8,y_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
            zS_16x8 = np.polyfit(x_16x8,yS_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
            zI_16x8 = np.polyfit(x_16x8,yI_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

            p_16x8 = np.poly1d(z_16x8) # Função ajustada para rho = 1.225kg/m³
            pS_16x8 = np.poly1d(zS_16x8) # Função ajustada para rho = 1.156kg/m³
            pI_16x8 = np.poly1d(zI_16x8) # Função ajustada para rho = 1.090kg/m³

            if self.rho == 1.225:
                return p_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
            elif self.rho == 1.156:
                return pS_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
            elif self.rho == 1.090:
                return pI_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

    def tracao_requerida(self, V):
        if self.rho == 1.225:
            Cl = (2*self.W)/(self.rho*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            Tr = self.W/(Cl/Cd)
            return Tr
        elif self.rho == 1.156:
            Cl = (2*self.W)/(self.rho*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            TrS = self.W/(Cl/Cd)
            return TrS
        elif self.rho == 1.090:
            Cl = (2*self.W)/(self.rho*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            TrI = self.W/(Cl/Cd)
            return TrI

    def potencia_requerida(self, V):
        if self.rho == 1.225:
            Pr = curvas.tracao_requerida(self, V)*V
            return Pr
        elif self.rho == 1.156:
            PrS = curvas.tracao_requerida(self, V)*V
            return PrS
        elif self.rho == 1.090:
            PrI = curvas.tracao_requerida(self, V)*V
            return PrI

    def potencia(self, V):
        if self.prop == '14x7':
            if self.rho == 1.225:
                Pd = curvas.tracao(self, V)*V
                return Pd
            elif self.rho == 1.156:
                PdS = curvas.tracao(self, V)*V
                return PdS
            elif self.rho == 1.090:
                PdI = curvas.tracao(self, V)*V
                return PdI
        if self.prop == '15x7':
            if self.rho == 1.225:
                Pd = curvas.tracao(self, V)*V
                return Pd
            elif self.rho == 1.156:
                PdS = curvas.tracao(self, V)*V
                return PdS
            elif self.rho == 1.090:
                PdI = curvas.tracao(self, V)*V
                return PdI
        if self.prop == '15x10':
            if self.rho == 1.225:
                Pd = curvas.tracao(self, V)*V
                return Pd
            elif self.rho == 1.156:
                PdS = curvas.tracao(self, V)*V
                return PdS
            elif self.rho == 1.090:
                PdI = curvas.tracao(self, V)*V
                return PdI
        if self.prop == '16x8':
            if self.rho == 1.225:
                Pd = curvas.tracao(self, V)*V
                return Pd
            elif self.rho == 1.156:
                PdS = curvas.tracao(self, V)*V
                return PdS
            elif self.rho == 1.090:
                PdI = curvas.tracao(self, V)*V
                return PdI
        
    def razao_subida(self, V):
        if self.prop == '14x7':
            if self.rho == 1.225:
                RC_14x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RC_14x7 < 0: return 0
                else: 
                    return RC_14x7
            elif self.rho == 1.156:
                RCS_14x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCS_14x7 < 0: return 0
                else: return RCS_14x7
            elif self.rho == 1.090:
                RCI_14x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCI_14x7 < 0: return 0
                else: return RCI_14x7
        if self.prop == '15x7':
            if self.rho == 1.225:
                RC_15x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RC_15x7 < 0: return 0
                else: return RC_15x7
            elif self.rho == 1.156:
                RCS_15x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCS_15x7 < 0: return 0
                else: return RCS_15x7
            elif self.rho == 1.090:
                RCI_15x7 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCI_15x7 < 0: return 0
                else: return RCI_15x7
        if self.prop == '15x10':
            if self.rho == 1.225:
                RC_15x10 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RC_15x10 < 0: return 0
                else: return RC_15x10
            elif self.rho == 1.156:
                RCS_15x10 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCS_15x10 < 0: return 0
                else: return RCS_15x10
            elif self.rho == 1.090:
                RCI_15x10 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCI_15x10 < 0: return 0
                else: return RCI_15x10
        if self.prop == '16x8':
            if self.rho == 1.225:
                RC_16x8 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RC_16x8 < 0: return 0
                else: return RC_16x8
            elif self.rho == 1.156:
                RCS_16x8 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCS_16x8 < 0: return 0
                else: return RCS_16x8
            elif self.rho == 1.090:
                RCI_16x8 = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
                if RCI_16x8 < 0: return 0
                else: return RCI_16x8