import pandas as pd

def transformar_medias_ph(dados_ph):
    # Carregar o arquivo CSV e transformar em resultados de média
    try:
        dados_ph = pd.read_csv(dados_ph)
        descricao = dados_ph.describe()
        media = descricao.loc['mean', 'ph']
        media_temperatura = descricao.loc['mean','temperatura']
        
        # Salvar as médias e dados de retorno em um novo CSV
        media_df = pd.DataFrame({'mean_ph': [media], 'mean_temperatura': [media_temperatura]})
        media_df.to_csv('medias_e_dados_de_retorno.csv', header=True, index=False)
        print("Dados de medias gerado com sucesso")
    except pd.errors.EmptyDataError as e:
        print("Erro: O arquivo dados_ph está vazio ou não contém dados válidos.")
        print(f"Detalhes do erro: {e}")
    except Exception as e:
        print("Ocorreu um erro inesperado.")
        print(f"Detalhes do erro: {e}")

selecao = input("Selecione 1  para converter dados de concentracao media de seus dados relatados ja em formato csv")
if selecao == "1":
    dados_ph = input("Insira o caminho do arquivo JSON: ")
    transformar_medias_ph(dados_ph)