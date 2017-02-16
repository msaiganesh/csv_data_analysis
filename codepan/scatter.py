import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import random, randint
df=pd.read_csv("analyse.csv",encoding='utf8')
ses = df
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('LATITUDE')
ax1.set_ylabel('LONGITUDE')
ax1.set_title("Affected cities Along Map as Rating as size")
val_arr = ['red','green','blue','yellow']
plt.scatter(ses['Latitude'],ses['Longitude'],c=val_arr,s=ses['Rating']*40)
plt.show()