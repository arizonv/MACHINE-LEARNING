import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('demo_round_traces_fixed.csv', delimiter=';')
df.dtypes
#int64 para enteros, float64 para números decimales, y object para cadenas de texto. También es posible que haya otros tipos de datos como bool para booleanos, datetime para fechas y horas, etc., dependiendo del contenido del archivo CSV y cómo se haya interpretado al leerlo en pandas.

df['Map'] = pd.to_numeric(df['Map'], errors='coerce')
df['RoundWinner'] = df['RoundWinner'].astype(int)
df['MatchWinner'] = df['MatchWinner'].astype(int)
df['Survived'] = df['Survived'].astype(int)
df['AbnormalMatch'] = df['AbnormalMatch'].astype(int)
# Convertir la columna 'Team' a una variable categórica 
df['Team'] = pd.Categorical(df['Team'])
df['Team'] = df['Team'].cat.codes

print("\nPrimeras filas del dataframe:")
df.head()

print("Información del dataframe:")
df.info()

print("\nValores nulos en el dataframe:")
df.isnull().sum()

print("\nValores nulos en el dataframe por cada fila :")
df.isna()

print("\nEstadísticas descriptivas del dataframe:")
print(df.describe())



# #histograma utilizando Seaborn
# sns.histplot(df['MatchKills'], bins=15)
# plt.xlabel('MatchKills')
# plt.ylabel('Frecuencia')
# plt.title('Histograma de MatchKills')
# plt.show()

# #diagrama de dispersión utilizando Matplotlib
# plt.scatter(df['TimeAlive'], df['RoundKills'])
# plt.xlabel('TimeAlive')
# plt.ylabel('RoundKills')
# plt.title('Diagrama de dispersión: TimeAlive vs RoundKills')
# plt.show()