import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("analyse.csv",encoding='utf8')
temp1,temp2 = df['Location'],df['Disease']
country=[]
for k in temp1:
    td = k.split(',')
    country.append(td[-1])
list3 = [list(a) for a in zip(country, temp2)]
hed = ['Country','desia']
daf = pd.DataFrame(list3,columns=hed)
dd = daf.groupby('Country').size()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Cities')
ax1.set_ylabel('distribution length ')
ax1.set_title("Affected cities with their disease")
dd.plot(kind='line',color='BROWN',alpha=1)