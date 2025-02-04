import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import desenvolvimento_grafico.graficos.funcoes as funcoes

#raiz_path = os.path.dirname(os.path.abspath(__file__))
#caminho_do_json = os.path.join(raiz_path, 'populador_csv','dadosdescarregar.json' )

selecao = int(input("SELECIONE 1 PARA CONCETRACAO, 2 PARA ESPECTOFOTOMETRIA CALIBRACAO, 3 ESPECTOFOTOMETRIA ABSORBANCIA"))
if selecao == 1:
    funcoes.funcao_spot_concentracao()
elif selecao ==2:
    funcoes.funcao_spot_e_calibration()
elif selecao ==3:
    funcoes.funcao_spot_absorbancia()