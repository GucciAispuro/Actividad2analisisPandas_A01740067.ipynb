import pandas as pd

air_df = pd.read_csv('LaqnData.csv')
#Pregunta 1
#Observa la estructura y contenido del dataframe con los atributos y métodos estudiados
print(air_df.shape)
print(air_df.columns)
print(air_df.head())
print(air_df.tail())
print(air_df.dtypes)
print(air_df.isna().sum())
#Calcula el porcentaje de valores faltantes por columna.
missing_percentage = air_df.isna().sum() / len(air_df) * 100
print(missing_percentage)

#Pregunta 2
#Total mediciones
total_mediciones = air_df.shape[0]
print(f"Total de mediciones realizadas: {total_mediciones}")

#Cuantas especies se analizaron
print(air_df.nunique())

#Columnas sin valor
for col in air_df.columns:
    if air_df[col].nunique() == 1:
        air_df.drop(columns=[col], inplace=True)

#Eliminar units
print(air_df['Units'].unique())
air_df.drop(columns=['Units'], inplace=True)

#Pregunta 3
#Valores por categoria
species_count = air_df['Species'].value_counts()
print(species_count)

#Pregunta 4
avg_by_species = air_df.groupby('Species')['Value'].mean()
print(avg_by_species)

#Pregunta 5 
pvt_df = air_df.pivot(index='ReadingDateTime', columns='Species', values='Value')
print(pvt_df.head())

#Pregunta 6 
print(pvt_df.describe())
#Mayor valor de NO2
max_no2 = pvt_df['NO2'].idxmax(), pvt_df['NO2'].max()
print("Mayor valor de NO2 registrado:", max_no2)
#Menor valor de PM10 
min_pm10 = pvt_df['PM10'].idxmin(), pvt_df['PM10'].min()
print("Menor valor de PM10 registrado:", min_pm10)
#Mediana NO
median_no = pvt_df['NO'].median()
print("Mediana del NO:", median_no)
#Primer cuartil de PM2.5
q1_pm25 = pvt_df['PM2.5'].quantile(0.25)
print("Primer cuartil de PM2.5:", q1_pm25)

#Pregunta 7
import matplotlib.pyplot as plt
pvt_df.hist(bins=50, figsize=(10,10))
plt.show()
#Contaminante con mayor variabilidad 
print(pvt_df.std())

#Pregunta 8 
#Separa la columna ReadingDateTime en Date y Time
datetime_df = air_df.ReadingDateTime.str.split(' ', expand=True)
datetime_df.columns = ['Date', 'Time']

#Separa la columna Date en Day, Month y Year
date_df = datetime_df.Date.str.split('/', expand=True)
date_df.columns = ['Day', 'Month', 'Year']

#Une las columnas de fecha y hora al DataFrame original y elimina la columna ReadingDateTime
air_df = air_df.join(date_df).join(datetime_df.Time).drop(columns=['ReadingDateTime', 'Year'])

#Configura el índice con Month, Day, Time y Species
air_df = air_df.set_index(['Month', 'Day', 'Time', 'Species'])
print(air_df.head())

#Pregunta 9 
print(air_df.unstack())
#Si son diferentes, debido a como se representa la tabla, todo depende del formato que le quieras dar, pero en mi opinión el unstack() no es necesario, ya que la tabla de la pregunta 8 es más digerible.

#Pregunta 10
#Ambos pares son funciones que nos ayudan a cambiar el formato de un data frame, organizando los datos en formato ancho o largo, aunque melt se utiliza para transformar data frames simples sin índices jerárquicos, y por eso mismo, en este caso optaría por utilizar el par de .stack() y .unstack() para un data frame más comprensible.