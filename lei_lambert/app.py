import pandas as pd
#primeiro definimos variaveis para os valores a serem necessarios
#a= absorbancia
#b= coef_abs_molar
#c=caminho optico da cubeta (mostrar padrao como 1cm)
#d= concentracao

#usuario / maquina ira inserir os dados aqui

##
def calculo_conc (carregar_df='C:/Users/marci/Documents/Program/python_chemistry/lei_lambert/dados_populados.csv', descarregar_df='C:/Users/marci/Documents/Program/python_chemistry/lei_lambert/retorno.csv' ):
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

calculo_conc()