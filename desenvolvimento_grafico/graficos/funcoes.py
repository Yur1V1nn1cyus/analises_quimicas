import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Função para verificar se o arquivo CSV existe
def verificar_csv(caminho):
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return False
    return True

# Função para gerar gráfico de concentração de amostra
def funcao_spot_concentracao(dados_load_c):
    if not verificar_csv(dados_load_c):
        return "Erro: Arquivo não encontrado."
    
    dados_Conc = pd.read_csv(dados_load_c)
    
    sns.set_theme(style="ticks")
    sns.catplot(data=dados_Conc, x="Amostra", y="Concentração (mg/L)", kind="point", palette="muted", height=4, aspect=2)
    plt.title('Gráfico de Concentração')    
    try:
        plt.savefig('dados_retornados_de_amostras_de_concentracao.png')
        print("Gráfico salvo com sucesso!")
    except Exception as e:
        print("Erro ao salvar o gráfico:", e)

    plt.show()
    return "Dados Carregados com sucesso"

# Função para gerar gráfico de calibração espectrofotométrica
def funcao_spot_e_calibration(dados_load_e):
    if not verificar_csv(dados_load_e):
        return "Erro: Arquivo não encontrado."
    
    calibragem = pd.read_csv(dados_load_e)
    
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(6.5, 6.5))
    sns.despine(f, left=True, bottom=True)

    # Certifique-se de que os nomes das colunas estão corretos
    calibragem.rename(columns={"Amostra": "sample", "Concentração (mg/L)": "concentration_mg_L"}, inplace=True)

    sns.scatterplot(x="sample", y="concentration_mg_L", hue="absorbance",
                    palette="ch:r=-.2,d=.3_r", linewidth=0, data=calibragem, ax=ax)
    
    plt.title('Gráfico de Espectrofotometria')
    plt.xlabel('Absorbância')
    plt.ylabel('Concentração (mg/L)')
    
    try:
        plt.savefig('dados_retornados_de_calibracao_espectofotometrica.png')
        print("Gráfico salvo com sucesso!")
    except ValueError :
        print("Verique os dados de seu grafico")
    except Exception as e:
        print("Erro ao salvar o gráfico:", e)

    plt.show()
    return "Dados Carregados com sucesso"

# Função para gerar gráfico de absorção espectrofotométrica
def funcao_spot_e_absorbation(dados_load_esp):
    if not verificar_csv(dados_load_esp):
        return "Erro: Arquivo não encontrado."
    
    calibragem = pd.read_csv(dados_load_esp)
    
    sns.set_theme(style="darkgrid")

    # Certifique-se de que as colunas existem antes de usá-las
    if "sample" not in calibragem.columns or "concentration_mg_L" not in calibragem.columns or "wavelength_nm" not in calibragem.columns:
        print("Erro: O arquivo CSV não contém as colunas necessárias.")
        return "Erro nos dados"

    sns.lineplot(x="sample", y="concentration_mg_L", hue="wavelength_nm", data=calibragem)
    
    plt.title('Gráfico de Espectrofotometria')
    plt.xlabel('Absorbância')
    plt.ylabel('Concentração (mg/L)')
    
    try:
        plt.savefig('dados_retornados_de_espectro_espectofotometrica.png')
        print("Gráfico salvo com sucesso!")
    except Exception as e:
        print("Erro ao salvar o gráfico:", e)

    plt.show()
    return "Dados Carregados com sucesso"

selecao = int(input("SELECIONE 1 PARA CONCETRACAO, 2 PARA ESPECTOFOTOMETRIA CALIBRACAO, 3 ESPECTOFOTOMETRIA ABSORBANCIA"))
if selecao == 1:
    dados_load_c = input("Descreva seu caminho de arquivo : ")
    funcao_spot_concentracao(dados_load_c)
elif selecao ==2:
    dados_load_e = input("Descreva seu caminho de arquivo : ")
    funcao_spot_e_calibration(dados_load_e)
elif selecao == 3 :
    dados_load_esp = input("Descreva seu caminho de arquivo : ")
    funcao_spot_e_absorbation(dados_load_esp)