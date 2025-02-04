import pandas as pd
import matplotlib.pyplot as plt
#primeiro definimos variaveis para os valores a serem necessarios
#a= absorbancia
#b= coef_abs_molar
#c=caminho optico da cubeta (mostrar padrao como 1cm)
#d= concentracao

#usuario / maquina ira inserir os dados aqui

##
def calculo_conc (carregar_df, descarregar_df):
    valoresDF = pd.read_csv(carregar_df)
    a = float(valoresDF.loc[0, 'Absorbância'])
    b = float(valoresDF.loc[0, 'Coeficiente de Absorção Molar'])
    c = float(valoresDF.loc[0, 'Caminho Óptico'])
    if c is None :
        c = 1
    else:
        try:
            d = a / (b*c)
            d_sci = f"{d:.2e}"
            resultadoDF = pd.DataFrame([{"Concentração" : d_sci}])
            resultadoDF.to_csv(descarregar_df, index=False)
            print(f"Arquivo salvo com sucesso: {descarregar_df}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero nao e aceitavel")
        except Exception as e:
            print(f"Erro: {e}")
        except ValueError as e:
            print(f"Erro: {e}")
        except FileNotFoundError as e:
            print(f"Erro: {e}")
        
carregar_df = input("Insira o caminho do arquivo JSON: ")
descarregar_df = input("Insira o caminho do arquivo que queira salvar o arquivo csv: ")
calculo_conc(carregar_df, descarregar_df)

ver_plot = input("Deseja visualizar o arquivo csv gerado? (s/n): ")
if ver_plot == "s":
    try:
        df = pd.read_csv(carregar_df)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(df['Absorbância'], df['Coeficiente de Absorção Molar'], color ='r', marker='o')
        ax.set_xlabel('Absorbância')
        ax.set_ylabel('Coeficiente de Absorção Molar')
        ax.set_zlabel('Concentração')
        ax.set_title('Gráfico de Concentração em Dispercao 3D')
        save_plot = input("Deseja salvar o gráfico? (s/n): ")
        if save_plot == "s":
            fig.savefig('Gráfico de Concentração em Dispercao 3D.png')
        plt.show()
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")