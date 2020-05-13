import pandas as pd
import matplotlib.pyplot as plt
    
df = pd.read_csv("TATAMOTORS.csv")
L = len(df)
print(len(df))
Listdate = []
Listvalue = []

Po = 0
Pl = 0

firstATR =0
B = 1
ATR_trolling = 0
P_ATR_trolling = 0
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
        firstATR = (summ)/14
        #print(df['date'][x],firstATR)
        P_ATR_trolling = (firstATR*3)+df['close'][x]
       
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
        #ATR = ((true_range - firstATR)*(2/15)+firstATR)
        #print(df['date'][x+1],ATR)

        if((x+1) < L):
            
            if(B == 0):
                if(df['openn'][x+1]<=P_ATR_trolling):
                    ATR_trolling = (ATR*3)+df['close'][x] 
                    if(float(P_ATR_trolling) > float(ATR_trolling)):
                        P_ATR_trolling = ATR_trolling
                    else:
                        P_ATR_trolling = P_ATR_trolling
                else:
                    print("date     ",df['date'][x+1])
                    print("open Loss",Pl-df['close'][x+1])
                    B = 1
                    Po = df['openn'][x+1]
                    ATR_trolling = df['close'][x] -(ATR*3)
                    P_ATR_trolling = ATR_trolling
                    

            else:
                if(df['openn'][x+1]>=P_ATR_trolling):
                    ATR_trolling = df['close'][x] - (ATR*3)
                    if(float(P_ATR_trolling) < float(ATR_trolling)):
                        P_ATR_trolling = ATR_trolling
                else:
                    print("date     ",df['date'][x+1])
                    print("open profit ",df['close'][x+1] - Po )
                    B = 0
                    Pl = df['openn'][x+1]
                    ATR_trolling = (ATR*3)+df['close'][x]
                    P_ATR_trolling = ATR_trolling
                
                




        '''if(B == 1 ):
            print("date     ",df['date'][x+1])
            print("open profit ",df['close'][x+1] - Po )
            print("")
            
        else:
            print("date     ",df['date'][x+1])
            print("open Loss",Pl-df['close'][x+1])
            print("")'''
            
            #print("loss",(ATR*3)+df['close'][x])
            #print("profit",df['close'][x]-(ATR*3))
            
          
            #Listdate.append(df['date'][x+1])
            #Listvalue.append(P_ATR_trolling)
            #firstATR = ATR
                

#plt.plot(Listdate,Listvalue)
#plt.show() 
        
        if((x+1) < L):
            #print("date    ",df['date'][x+1])
            #print("close   ",df['close'][x])
            #print("B",B,"  ",P_ATR_trolling)
            #print("")
            firstATR = ATR
