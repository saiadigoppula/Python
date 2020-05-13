import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


df = pd.read_csv("TAT.csv")
#df['close'].plot()
#plt.show()
#print(df.head())
print(len(df))


for x in range(15,len(df)):
    lossesSum = 0
    profitsSum = 0
    for y in range(x-14,x):
        #print(type(df['close'][y-1]))
        pre = float(df['close'][y-1])
        now = float(df['close'][y])
        #print(df['date'][y-1],"pre",pre)
        #print(df['date'][y],"now",now)
        #print(type(pre))
        if(pre > now):
              losses = pre - now
              print("loss",losses)
              lossesSum = float(lossesSum + losses)
              print("lossesSum",lossesSum)
        else:
            profits = now - pre
            print("profit",profits)
            profitsSum = float(profitsSum + profits)
            print("profitsSum",profitsSum)
    lossesSum = (lossesSum /14)
    print("lossesAVG",lossesSum)
    profitsSum = (profitsSum/14)
    print("profitsAVG",profitsSum)

    rs = profitsSum / lossesSum
    print("rs",rs)

    rsi = 100 - (100/(1+rs))
    print(df['date'][y],"rsi                     ",rsi)
