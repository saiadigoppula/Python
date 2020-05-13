import pandas as pd

df = pd.read_csv("TATAMOTORS.csv")
print(len(df))

for x in range(11,len(df)):
    summ = 0
    if(x == 11):
        for y in range(x-10,x):
            summ = summ +df['close'][x]
        firstEMA = (10-summ)/10
       
    else:
        close = float(df['close'][x])
        EMA = ((close-firstEMA)*(2/(10+1))+firstEMA)
        print(df['date'][x],EMA)
        firstEMA = EMA
               
           
       
