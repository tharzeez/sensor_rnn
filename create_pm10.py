import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('interpolated_df.csv')
df = df.drop("AQI_Bucket",axis=1)
df = df.drop("AQI",axis=1)
df = df.drop("StationId",axis=1)
df = df.drop("Unnamed: 0",axis=1)
df = df.drop("Un",axis=1)
df = df.drop("PM2.5",axis=1)
df = df.drop("NO",axis=1)
df = df.drop("NO2",axis=1)
df = df.drop("NOx",axis=1)
df = df.drop("CO",axis=1)
df = df.drop("NH3",axis=1)
df = df.drop("SO2",axis=1)
df = df.drop("O3",axis=1)
df = df.drop("Benzene",axis=1)
df = df.drop("Toluene",axis=1)
df = df.drop("Xylene",axis=1)

df.to_csv('pm10_amar.csv', sep=',', index=False)
