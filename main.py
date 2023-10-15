import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='dark')

# Dataset
df = pd.read_csv('all_data.csv')

st.title('Konsentrasi Distribusi PM2.5 diudara')

plt.figure(figsize=(12, 5))
sns.histplot(data=df, x='PM2.5', bins=50, kde=True)
# plt.title('Distribution of the recorded PM2.5 concentration in the air', fontsize=16)

st.pyplot(plt)

monthly_data = df[['month', 'PM2.5', 'station']]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
ordered_monthdf = pd.DataFrame(months, columns=['month'])
map_dict = {}
for i, j in enumerate(months):
    map_dict.setdefault(i+1, j)

monthly_data['month'] = monthly_data['month'].map(map_dict)
monthly_average = monthly_data.groupby('month').median()
monthly_average = pd.merge(
    ordered_monthdf, monthly_average, left_on='month', right_index=True)
monthly_average = np.round(monthly_average, 1)
monthly_average = monthly_average.set_index('month')

st.title('Jumlah PM2.5 yang terkandung di udara')

plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_data, x='month', y='PM2.5', hue='station', ci=None)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Konsentrasi PM2.5 (ug/m^3)', fontsize=14)
# plt.title('Jumlah PM2.5 yang terkandung di udara', fontsize=16)
plt.grid(axis='x')
plt.tight_layout()

st.pyplot(plt)

st.write("Dilihat dari grafik visualisasi yang didapat kualitas udara disetiap station perbulannya dilihat dari indikator PM2.5 mengalami peningkatan yang sangat signifikan mulai dari bulan agustus sampai dengan desember. jika dilihat per station, station yang cenderung mengalami peningkatan disetiap bulannya adalah Station Wanshouxigong.")

st.title('Arah pergerakan udara yang tercemar')

wind_dir = df[['wd', 'PM2.5']]

wind_dir = wind_dir.groupby('wd').median()


with plt.style.context('ggplot'):
    plt.figure(figsize=(12, 5))
    wind_dir.plot(legend=False, kind='bar', linewidth=0.9)
    plt.xlabel('Arah udara', fontsize=14)
    plt.ylabel('Konsentrasi PM2.5 (ug/m^3)', fontsize=14)
    # plt.title('Arah pergerakan udara yang tercemar', fontsize=16)
    plt.grid(axis='x')
    plt.tight_layout()

st.pyplot(plt)
st.write("Apabila dilihat dari arah bergeraknya udara, terdapat 2 arah yang paling tinggi pergerakannya yaitu ESE dan SE namun juga terdapat arah yang tidak diketahui arahnya dengan nilai yang cukup tinggi.")

st.title('Korelasi Matrix Antar Variable')
plt.figure(figsize=(13, 9))
correlation_data = df[['PM2.5', 'PM10', 'SO2', 'NO2',
                       'CO', 'O3', 'TEMP', 'PRES',
                       'DEWP', 'RAIN', 'WSPM']]
sns.heatmap(correlation_data.corr(), cmap=plt.cm.Reds, annot=True)
# plt.title('Korelasi Matrix antar variable', fontsize=16)
plt.show()
st.pyplot(plt)

st.write("Terdapat 3 variable yang memiliki keterkaitan untuk mempengaruhi Kualitas PM2.5, yaitu PM10, NO2 dan CO, karena memiliki korelasi posiitif untuk mempengaruhi peningkatan PM2.5.")
