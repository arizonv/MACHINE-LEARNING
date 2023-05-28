import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del archivo CSV
data = pd.read_csv("demo_round_traces_fixed(1).csv", delimiter=";")


# Exploración de la hipótesis de regresión
# Calcular estadísticas descriptivas de las variables relevantes
regression_data = data[["TimeAlive", "TravelledDistance"]]
regression_stats = regression_data.describe()
print("Estadísticas descriptivas para TimeAlive y TravelledDistance:")
print(regression_stats)


# Exploración de la hipótesis de regresión
# Graficar la relación entre TravelledDistance y TimeAlive
sns.scatterplot(data=data, x="TravelledDistance", y="TimeAlive")
plt.xlabel("Travelled Distance")
plt.ylabel("Time Alive")
plt.title("Relationship between Travelled Distance and Time Alive")
plt.show()


# Visualizar outliers en TimeAlive
sns.boxplot(data=data, x="TimeAlive")
plt.xlabel("Time Alive")
plt.title("Boxplot de Time Alive")
plt.show()

# Visualizar outliers en TravelledDistance
sns.boxplot(data=data, x="TravelledDistance")
plt.xlabel("Travelled Distance")
plt.title("Boxplot de Travelled Distance")
plt.show()


# Calcular la correlación entre TravelledDistance y TimeAlive
correlation = data["TravelledDistance"].corr(data["TimeAlive"])
print("Correlation TravelledDistance y TimeAlive : ", correlation)



# Exploración de la hipótesis de agrupación ############
# Seleccionar las columnas relevantes para la agrupación
selected_columns = ["PrimaryAssaultRifle", "PrimarySniperRifle", "PrimaryHeavy", "PrimarySMG", "PrimaryPistol", "RoundKills"]
group_data = data[selected_columns]

# Exploración de la hipótesis de agrupación
# Calcular el número de observaciones por cada categoría de PrimaryAssaultRifle
grouping_data = data["PrimaryAssaultRifle"].value_counts()
print("Número de observaciones por categoría de PrimaryAssaultRifle:")
print(grouping_data)

# Calcular el promedio de RoundKills para cada valor de PrimarySniperRifle
grouping_data = data.groupby("PrimarySniperRifle")["RoundKills"].mean()
print("Promedio de RoundKills para cada valor de PrimarySniperRifle:")
print(grouping_data)


# Detección de valores nulos
null_values = data.isnull().sum()
print("Valores nulos por columna:")
print(null_values)

# Visualizar los valores nulos
sns.heatmap(data.isnull(), cbar=False)
plt.title("Valores nulos")
plt.show()

# Visualizar la distribución de las variables relevantes
group_data.hist()
plt.tight_layout()
plt.show()

