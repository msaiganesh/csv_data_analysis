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
key = input('enter the country to be searched')
list4 = []
for i in range(len(country)):
    if country[i]==key:
        list4.append(temp2[i])
my_dict = {i:list4.count(i) for i in list4}
list_key_value = [ [k,v] for k, v in my_dict.items() ]
hed = ['Disease','countw']
daf = pd.DataFrame(list_key_value,columns=hed)
plt.axis('equal')
plt.title(key)
plt.xlabel('DISTRIBUTION OF DISEASE')
plt.pie(daf['countw'],labels=daf['Disease'])
plt.show()




