import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("analyse.csv",encoding='utf8')
print(df)
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.boxplot(df['Rating'])
plt.show()