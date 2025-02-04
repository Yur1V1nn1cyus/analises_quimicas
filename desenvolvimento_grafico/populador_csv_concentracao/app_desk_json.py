import json
import csv
from datetime import datetime

def preencher_dados_concentracao(inserir_loc_arq):
    try:
        with open(inserir_loc_arq, 'r', encoding='utf-8') as json_file:
            dados = json.load(json_file)

        if not isinstance(dados, dict) or "sample" not in dados:
            print("Erro: O arquivo JSON não contém a chave 'sample' ou não é um dicionário.")
            return

        sample = dados["sample"]

        if not isinstance(sample, list) or len(sample) == 0:
            print("Erro: 'calibration_curve' não é uma lista ou está vazia.")
            return

        if not all(isinstance(item, dict) for item in sample):
            print("Erro: A lista 'calibration_curve' contém itens que não são dicionários.")
            return


        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo_csv = f'concentracoes_{timestamp}.csv'

        with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as csv_file:
            cabecalho = sample[0].keys()
            escrever_csv = csv.DictWriter(csv_file, fieldnames=cabecalho)
            
            escrever_csv.writeheader()

            for item in sample:
                linha_tratada = {chave: (valor if valor is not None and valor != "" else "N/A") for chave, valor in item.items()}
                escrever_csv.writerow(linha_tratada)

        print(f"Arquivo CSV gerado com sucesso: {nome_arquivo_csv}")

    except FileNotFoundError:
        print("Erro: O arquivo 'concentracoes.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo 'concentracoes.json' não é um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def concentracoes_espectofotometricas(inserir_loc_arq2):
    try:
        with open(inserir_loc_arq2, 'r', encoding='utf-8') as json_file:
            dados = json.load(json_file)  

            if not isinstance(dados, dict) or "calibration_curve" not in dados:
                print("Erro: O arquivo JSON não contém a chave 'calibration_curve' ou não é um dicionário.")
                return
            
            calibration_curve = dados["calibration_curve"]

            if not isinstance(calibration_curve, list) or len(calibration_curve) == 0:
                print("Erro: 'calibration_curve' não é uma lista ou está vazia.")
                return

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'concentracoes_espectofotometricas_{timestamp}.csv'

            with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
                cabecalho = calibration_curve[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=cabecalho)
                writer.writeheader()
                writer.writerows(calibration_curve)
                print(f"Arquivo CSV gerado com sucesso: {filename}")

    except FileNotFoundError:
        print("Erro: O arquivo JSON não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está em formato inválido.")
    except Exception as e:
        print("Erro inesperado:", e)

selecao = input("Selecione 1 para converter dados de concentracao para formato csv, selecione 2 para converter  dados de concentracao espectofotometricas para csv")
if selecao == "1":
    inserir_loc_arq = input("Insira o caminho do arquivo JSON: ")
    preencher_dados_concentracao(inserir_loc_arq)

elif selecao == "2":
    inserir_loc_arq2 = input("Insira o caminho de seu arquivo")
    concentracoes_espectofotometricas(inserir_loc_arq2)