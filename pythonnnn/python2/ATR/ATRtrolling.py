import pandas as pd

df = pd.read_csv("TAT.csv")
print(len(df))
firstATR =0
for x in range(15,len(df)):
    summ = 0
    if(x == 15):
        for y in range(x-14,x):
            #true_range=max[(df['high'][y] - df['low']), abs(df['high'][y] - df['close'][y-1]), abs (df['low'][y] - df['close'][y-1])]
            HL = (df['high'][y] - df['low'][y])
            HPC = abs(df['high'][y] - df['close'][y-1])
            LPC = abs (df['low'][y] - df['close'][y-1])
            print(HL)
            list = [HL,HPC,LPC]
            if(HL==HPC==LPC):
                #print('fuck ')
                true_range = HL
            else:
                true_range = max(list)
                #print(true_range)

            summ = summ + true_range
        firstATR = summ/14
        print(df['date'][x],firstATR)
       
    else:
        #true_range=max[(df['high'][y] - df['low']), abs(df['high'][y] - df['close'][y-1]), abs (df['low'][y] - df['close'][y-1])]
        HL = (df['high'][x] - df['low'][x])
        HPC = abs(df['high'][x] - df['close'][x-1])
        LPC = abs (df['low'][x] - df['close'][x-1])
    
        if(HL==HPC==LPC):
            #print('fuck ')
            true_range = HL
        else:
            list = [HL,HPC,LPC]
            true_range = max(list)
            #print(true_range)
        
        ATR = (firstATR*(13) +true_range)/14
        print(df['date'][x],ATR)
        
        firstATR = ATR
        #print("Trollingloss", (ATR*3)+df['close'][x])
        print("Trollingprofit", abs((ATR*3)-df['close'][x]))
        
        
