# -*- coding: utf-8 -*-
"""Evidencia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sdeVsPGMTkm_ekUbxPgi2WWppobqObJ8
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('d.csv')
df.head()

"""Tipos de variables

Año: int64

Periodo: object

Agricultura.ganaderia: int64

Industria.electricidad: int64

Industria.manufacturera: int64

Construccion: int64



"""

df.info()

df.describe()

min_a = df['Agricultura.ganaderia'].min()
print('Mínimo de Agricultura.ganaderia es', min_a)

min_e = df['Industria.electricidad'].min()
print('Mínimo de Industria.electricidad es', min_e)


min_m = df['Industria.manufacturera'].min()
print('Mínimo de Industria.manufacturera es', min_m)

min_c = df['Construccion'].min()
print('Mínimo de Construccion es', min_c)

print()

max_a = df['Agricultura.ganaderia'].max()
print('Máximo de Agricultura.ganaderia es', max_a)

max_e = df['Industria.electricidad'].max()
print('Máximo de Industria.electricidad es', max_e)


max_m = df['Industria.manufacturera'].max()
print('Máximo de Industria.manufacturera es', max_m)

max_c = df['Construccion'].max()
print('Máximo de Construccion es', max_c)

import numpy as np

# promedio de Agricultura.ganaderia
media_a = df['Agricultura.ganaderia'].mean()
print('La media de Agricultura.ganaderia es', media_a)

# mediana de Agricultura.ganaderia
mediana_a = df['Agricultura.ganaderia'].median()
print('La mediana de Agricultura.ganaderia es', mediana_a)

# desviación estandar de Agricultura.ganaderia
std_a = df['Agricultura.ganaderia'].std()
print('La desviación estándar de Agricultura.ganaderia es', std_a)

# varianza de Agricultura.ganaderia
var_a = (df['Agricultura.ganaderia'].var())
print('La varianza de Agricultura.ganaderia es', var_a)

print()

# promedio de Industria.electricidad
media_e = (df['Industria.electricidad'].mean())
print('La media de Industria.electricidad es', media_e)

# mediana de Industria.electricidad
mediana_e = (df['Industria.electricidad'].median())
print('La mediana de Industria.electricidad es', mediana_e)

# desviación estandar de Industria.electricidad
std_e = (df['Industria.electricidad'].std())
print('La desviación estándar de Industria.electricidad es', std_e)

# varianza de Industria.electricidad
var_e = (df['Industria.electricidad'].var())
print('La varianza de Industria.electricidad es', var_e)

print()

# promedio de Industria.manufacturera
media_m = (df['Industria.manufacturera'].mean())
print('La media de Industria.manufacturera es', media_m)

# mediana de Industria.manufacturera
mediana_m = (df['Industria.manufacturera'].median())
print('La mediana de Industria.manufacturera es', mediana_m)

# desviación estandar de Industria.electricidad
std_m = (df['Industria.manufacturera'].std())
print('La desviación estándar de Industria.manufacturera es', std_m)

# varianza de Industria.electricidad
var_m = (df['Industria.manufacturera'].var())
print('La varianza de Industria.manufacturera es', var_m)

print()

# promedio de Construccion
media_c = (df['Construccion'].mean())
print('La media de Construccion es', media_c)

# mediana de Construccion
mediana_c = (df['Construccion'].median())
print('La mediana de Construccion es', mediana_c)

# desviación estandar de Industria.electricidad
std_c = (df['Construccion'].std())
print('La desviación estándar de Construccion es', std_c)

# varianza de Construccion
var_e = (df['Construccion'].var())
print('La varianza de Construccion es', var_e)

"""De la media, mediana, desviación estándar y varianza podemos concluir lo siguiente:

La media de las 4 variables es muy alta y esto indica que dichos sectores están funcionando de manera eficiente y producen resultados consistentemente altos.

La mediana de las cuatro variables es similar a la media, esto quiere decir que los datos de dichas variables están distribuidos de manera simétrica.

La desviación estándar en las cuatro variables es muy alta esto indica que existe una mayor variabilidad en los datos de las variables.

Al igual que en la desviación estándar la varianza es alta, esto indica que los valores de las variables están más dispersos y tienen una mayor inestabilidad o fluctuación.


"""

plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation= 45)
plt.show()

corr= df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr,annot= True, cmap= "RdPu")
plt.show()

varianza1=df["Agricultura.ganaderia"].var()
print(varianza1)

varianza2=df["Industria.electricidad"].var()
print(varianza2)

varianza3=df["Industria.manufacturera"].var()
print(varianza3)

varianza4=df["Construccion"].var()
print(varianza4)

sns.pairplot(data=df, hue= 'Agricultura.ganaderia')

"""Podemos ver que en las gráficas de "Año x Industria Manufacturera" y "Año x Construcción" que las variables tienen una relación linear positiva y su correlación es fuerte en ciertos momentos. Mientras que las demás gráficas no parecen tener una correlación entre sí."""

sns.pairplot(data=df, hue= 'Industria.electricidad')

sns.pairplot(data=df, hue= 'Industria.manufacturera')

sns.pairplot(data=df, hue= 'Construccion')

sns.pairplot(data=df, hue="Periodo")

sns.pairplot(data=df, hue="Año")

sns.histplot(data=df, x="Periodo")

columns= ["Agricultura.ganaderia", "Industria.electricidad", "Industria.manufacturera", "Construccion"]
x = df.loc[:, columns]
scaler = StandardScaler()

x_norm = scaler.fit_transform(x)
df_norm = pd.DataFrame(x_norm, columns=columns)
print(df_norm.head())

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

kmax= 20
grupos = range(3,kmax)
wcss = []
score = []

for k in grupos:
  model = KMeans(n_clusters = k)
  clusters = model.fit_predict(df_norm)
  wcss.append(model.inertia_)
  score.append(silhouette_score(df_norm,clusters))

plt.clf()
fig, axs = plt.subplots(1,2,figsize=(10,5))

axs[0].plot(grupos,wcss)
axs[0].grid(True)
axs[1].plot(grupos,score)
plt.grid(True)

model = KMeans(n_clusters=8)
clusters = model.fit_predict(df_norm)

df['Grupo'] = clusters.astype('str')

print(df.head())

sns.pairplot(data=df, hue="Grupo")

df.groupby("Grupo").mean()
mean_values_round = df.groupby("Grupo").mean().round(3)
mean_values_round.head()

sns.histplot(data=df, x="Grupo")

X = df["Industria.manufacturera"].values.reshape(-1, 1)
Y = df["Agricultura.ganaderia"].values

from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Industria manufacturera')
plt.ylabel('Agricultura ganaderia')
plt.legend()
plt.show()

X = df["Industria.manufacturera"].values.reshape(-1, 1)
Y = df["Industria.electricidad"].values

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Industria manufacturera')
plt.ylabel('Industria electricidad')
plt.legend()
plt.show()

df = df.sort_values(by="Año")
ultimo_registro_por_año = df.groupby("Año").last().reset_index()

X = ultimo_registro_por_año["Año"].values.reshape(-1, 1)
Y = ultimo_registro_por_año["Agricultura.ganaderia"].values

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Año')
plt.ylabel('Agricultura.ganaderia')
plt.legend()
plt.show()

X = ultimo_registro_por_año["Año"].values.reshape(-1, 1)
Y = ultimo_registro_por_año["Industria.electricidad"].values

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Año')
plt.ylabel('Industria electricidad')
plt.legend()
plt.show()

X = ultimo_registro_por_año["Año"].values.reshape(-1, 1)
Y = ultimo_registro_por_año["Industria.manufacturera"].values

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Año')
plt.ylabel('Industria manufacturera')
plt.legend()
plt.show()

#Predicción de población dedicada a la industria manufacturera después de 20 años de la primer medición.
X_pred = [[20]]
Y_pred = modelo.predict(X_pred)
print("Predicción de Y para X =", X_pred, "es", Y_pred)

X = ultimo_registro_por_año["Año"].values.reshape(-1, 1)
Y = ultimo_registro_por_año["Construccion"].values

modelo = LinearRegression()
modelo.fit(X, Y)

r_cuadrado = modelo.score(X, Y)
print("Coeficiente de determinación (R^2):", r_cuadrado)

plt.scatter(X, Y, label='Datos')

plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión')

plt.xlabel('Año')
plt.ylabel('Construcción')
plt.legend()
plt.show()

#Predicción de población dedicada a la construccion después de 20 años de la primer medición.
X_pred = [[20]]
Y_pred = modelo.predict(X_pred)
print("Predicción de Y para X =", X_pred, "es", Y_pred)