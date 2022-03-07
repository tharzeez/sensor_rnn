
#######################################################################
# Basic cleaning of the dataset
# interpolated the missing values using the pandas library
#
######################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


######################################################################
# To convert it to get it from the parameter for the sage maker.
# 
# 
######################################################################
df = pd.read_csv('amaravatiSecretariatData.csv')


######################################################################
# The missing values are interpolated, giving a basic line between 
# the two missing time periods
######################################################################
interpolatedDF = df.interpolate()


