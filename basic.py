
#############################################
# Basic cleaning of the dataset
# interpolated the missing values using the pandas library
#
#############################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('amaravatiSecretariatData.csv')

# amaravatiSecretariatData = df[df['StationId'] == 'AP001']
# head_df = df.head(500)
# head_df = df
# new_df = df.dropna()

# new_df.to_csv('null_removed', sep='\t')

# df.pivot()
# ax = df.plot(kind='line',x='Datetime',y='PM2.5',color='green')

# df.plot(kind='line',x='Datetime',y=['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'])

print('Check here', df.count(), '\n')
# df.plot(kind='line',x='Datetime',y=['PM10'])

interpolatedDF = df.interpolate()

# interpolatedDF.to_csv('interpolated_df_all_stations.csv', sep=',')
df.interpolate().plot(kind='line',x='Datetime',y=['PM10'])
# head_df.interpolate().plot(kind='line',x='Datetime',y=['PM10'])

# amaravatiSecretariatData.to_csv('amaravatiSecretariatData.csv', sep=',')

plt.show()
print('Hello world', df)

