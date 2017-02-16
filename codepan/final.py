import matplotlib.pyplot as plt
import pandas as pd
def newlinechart():
    df = pd.read_csv("analyse.csv", encoding='utf8')
    temp1, temp2 = df['Location'], df['Disease']
    country = []
    for k in temp1:
        td = k.split(',')
        country.append(td[-1])
    list3 = [list(a) for a in zip(country, temp2)]
    hed = ['Country', 'desia']
    daf = pd.DataFrame(list3, columns=hed)
    dd = daf.groupby('Country').size()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel('Cities')
    ax1.set_ylabel('distribution length ')
    ax1.set_title("Affected cities with their disease")
    dd.plot(kind='line', color='BROWN', alpha=1)
    plt.show()
def scattercheck():
    df = pd.read_csv("analyse.csv", encoding='utf8')
    ses = df
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel('LATITUDE')
    ax1.set_ylabel('LONGITUDE')
    ax1.set_title("Affected cities Along Map as Rating as size")
    val_arr = ['red', 'green', 'blue', 'yellow']
    plt.scatter(ses['Latitude'], ses['Longitude'], c=val_arr, s=ses['Rating'] * 40)
    plt.show()
def pichart():
    df = pd.read_csv("analyse.csv", encoding='utf8')
    temp1, temp2 = df['Location'], df['Disease']
    country = []
    for k in temp1:
        td = k.split(',')
        country.append(td[-1])
    list3 = [list(a) for a in zip(country, temp2)]
    hed = ['Country', 'desia']
    daf = pd.DataFrame(list3, columns=hed)
    key = input('enter the country to be searched')
    list4 = []
    for i in range(len(country)):
        if country[i] == key:
            list4.append(temp2[i])
    my_dict = {i: list4.count(i) for i in list4}
    list_key_value = [[k, v] for k, v in my_dict.items()]
    hed = ['Disease', 'countw']
    daf = pd.DataFrame(list_key_value, columns=hed)
    plt.axis('equal')
    plt.title(key)
    plt.xlabel('DISTRIBUTION OF DISEASE')
    plt.pie(daf['countw'], labels=daf['Disease'])
    plt.show()
def barchart():
    df = pd.read_csv("analyse.csv", encoding='utf8')
    temp1, temp2 = df['Location'], df['Disease']
    country = []
    for k in temp1:
        td = k.split(',')
        country.append(td[-1])
    list3 = [list(a) for a in zip(country, temp2)]
    hed = ['Country', 'desia']
    daf = pd.DataFrame(list3, columns=hed)
    daf = daf.head(200)
    dd = daf.groupby(['Country', 'desia']).size()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel('Cities,disease')
    ax1.set_ylabel('distribution lenght')
    ax1.set_title("Affected cities with their disease")
    dd.plot(kind='bar', color='red', alpha=1)
def boxchart():
    df = pd.read_csv("analyse.csv", encoding='utf8')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(df['Rating'])
    ax.set_ylabel('Rating')
    ax.set_title(" Rating Graph ")
    plt.show()

print('enter the choice of chart to be drawn')
print("enter 1 to draw pi chart")
print("enter 2 to draw scatter chart")
print("enter 3 to draw line chart")
print("enter 4 to draw barchart")
print("enter 5 to draw boxchart")

while(True):
    t = int(input())
    if t == 1:
        f = pichart()
    elif t == 2:
        f = scattercheck()
    elif t == 3:
        f = newlinechart()
    elif t == 4:
        f = barchart()
    elif t == 5:
        f = boxchart()
    else:
        exit()


