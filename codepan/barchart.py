import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("analyse.csv",encoding='utf8')
var = df.groupby('Disease').Disease.count()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('DISEASES')
ax1.set_ylabel('Distribution length')
ax1.set_title("DISEASE VS DISTRIBUTION GRAPH")
var.plot(kind='bar',color='green',alpha=1)