import pandas as pd
import matplotlib.pyplot as plt
import numpy
    
df = pd.read_csv("TATAMOTORS.csv")
L = len(df)
#print(len(df))
Listdate = []
Listvalue = []

over_all = 0


for j in numpy.arange(0.1, 10, 0.1):       
    for i in range(4,50):
        Po = 0
        Pl = 0
        profit = 0
        loss = 0
        firstATR =0
        B = 1
        ATR_trolling = 0
        P_ATR_trolling = 0
        for x in range(i+1,len(df)):
            summ = 0
            if(x == i+1):
                for y in range(x-i,x):
                    #true_range=max[(df['high'][y] - df['low']), abs(df['high'][y] - df['close'][y-1]), abs (df['low'][y] - df['close'][y-1])]
                    HL = (df['high'][y] - df['low'][y])
                    HPC = abs(df['high'][y] - df['close'][y-1])
                    LPC = abs (df['low'][y] - df['close'][y-1])
                    #print(HL)
                    list = [HL,HPC,LPC]
                    if(HL==HPC==LPC):
                        #print('fuck ')
                        true_range = HL
                    else:
                        true_range = max(list)
                        #print(true_range)

                    summ = summ + true_range
                firstATR = (summ)/i
                #print(df['date'][x],firstATR)
                P_ATR_trolling = (firstATR*j)+df['close'][x]
               
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
                
                ATR = (firstATR*(i-1) +true_range)/i
                #ATR = ((true_range - firstATR)*(2/15)+firstATR)
                #print(df['date'][x+1],ATR)

                if((x+1) < L):
                    
                    if(B == 0):
                        if(df['openn'][x+1]<=P_ATR_trolling):
                            #ATR_trolling = (ATR*j)+df['close'][x]
                            ATR_trolling = (ATR*j)+(df['high'][x]+df['low'][x])/2 
                            if(float(P_ATR_trolling) > float(ATR_trolling)):
                                P_ATR_trolling = ATR_trolling
                            else:
                                P_ATR_trolling = P_ATR_trolling
                        else:
                            #print("date     ",df['date'][x+1])
                            #print("open Loss",Pl-df['close'][x+1])
                            loss = loss + Pl-df['close'][x+1]
                            #print("loss",loss)
                            B = 1
                            Po = df['openn'][x+1]
                            #ATR_trolling = df['close'][x] -(ATR*3)
                            ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*j)
                            P_ATR_trolling = ATR_trolling
                            

                    else:
                        if(df['openn'][x+1]>=P_ATR_trolling):
                            #ATR_trolling = df['close'][x] - (ATR*3)
                            ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*j)
                            if(float(P_ATR_trolling) < float(ATR_trolling)):
                                P_ATR_trolling = ATR_trolling
                        else:
                            #print("date     ",df['date'][x+1])
                            #print("open profit ",df['close'][x+1] - Po )
                            profit = profit + df['close'][x+1] - Po
                            #print("profit",profit)
                            B = 0
                            Pl = df['openn'][x+1]
                            #ATR_trolling = (ATR*j)+df['close'][x]
                            ATR_trolling = (ATR*j)+(df['high'][x]+df['low'][x])/2
                            P_ATR_trolling = ATR_trolling
                        
                    firstATR = ATR
                    
        #print(i)           
        #print("profit",profit)
        #print("Loss",loss)
        if(over_all<(profit+loss)):            
            print("i",i,"j",j)
            print(profit+loss)
            over_all = profit+loss
print("FINISHED")
            
