import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados de absorbância
data = {'Comprimento de Onda (nm)': [400, 450, 500, 550, 600], 'Absorbância': [0.2, 0.5, 0.8, 1.2, 0.9]}
df = pd.DataFrame(data)

# Gráfico de linha
sns.lineplot(x='Comprimento de Onda (nm)', y='Absorbância', data=df, marker='o')
plt.title('Curva de Absorbância x Comprimento de Onda')
plt.show()