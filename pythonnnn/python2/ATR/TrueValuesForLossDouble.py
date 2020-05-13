import pandas as pd
import matplotlib.pyplot as plt
import numpy
import time
   
df = pd.read_csv("TATAMOTORS.csv")
L = len(df)
print(len(df))
Listdate = []
Listvalue = []




value = 1


trueproft = 0


for j in numpy.arange(0.1, 10, 0.1):       
    for i in range(3,50):
        profit = 0
        loss = 0
        error = 0
        perror =0
        xprofit = 0
        value = 1
        Po = 0
        Pl = 0
        firstATR =0
        B = 1
        ATR_trolling = 0
        P_ATR_trolling = 0
        
        HH = -9999
        LL = -9999

        
        for x in range((i+1),len(df)):
            summ = 0
            if(x == i+1):
                for y in range(x-i,x):
                  
                    HL = (df['high'][y] - df['low'][y])
                    HPC = abs(df['high'][y] - df['close'][y-1])
                    LPC = abs (df['low'][y] - df['close'][y-1])
                    #print(HL)
                    list = [HL,HPC,LPC]
                    if(HL==HPC==LPC):
                        
                        true_range = HL
                    else:
                        true_range = max(list)
                       

                    summ = summ + true_range
                firstATR = (summ)/i
               
                P_ATR_trolling = (firstATR*j)+df['close'][x]
               
            else:
              
                HL = (df['high'][x] - df['low'][x])
                HPC = abs(df['high'][x] - df['close'][x-1])
                LPC = abs (df['low'][x] - df['close'][x-1])
           
                if(HL==HPC==LPC):
                   
                    true_range = HL
                else:
                    list = [HL,HPC,LPC]
                    true_range = max(list)
                   
               
                ATR = (firstATR*(i-1) +true_range)/i
               

                if((x+1) < L):
                   
                    if(B == 0):
                        if(df['openn'][x+1]<=P_ATR_trolling):
                            ATR_trolling = (ATR*j)+df['close'][x]
                            if(float(P_ATR_trolling) > float(ATR_trolling)):
                                P_ATR_trolling = ATR_trolling
                            else:
                                P_ATR_trolling = P_ATR_trolling
                                
                                                        
                            if(error<0):
                                if((error + (Pl-(df['low'][x+1]))* value)>0):
                                    perror = perror + (Pl-(df['low'][x+1]))* value
                                    #print("low value  date ",df['date'][x+1])
                                    #print("low value",(Pl-(df['low'][x+1])))
                                    #print("perrorperrorperrorperrorperrorperrorperror",perror)
                                    value = 1
                                    error = 0

                            
                        else:
                            #print("date     ",df['date'][x+1])
                            #print("open Loss",Pl-df['close'][x+1])

                           

                           
                            loss = loss + (Pl-df['close'][x+1])*value
                            #print("loss",loss)

                            if((Pl-df['close'][x+1])*value <0):
                                error = error + (Pl-df['close'][x+1])*value
                                #print("final profit      ",(Pl-df['close'][x+1])*value)
                                #print("error                                       ",error)
                                value = value * 2
                            else:
                                value = 1
                            #print("value                                                                     ",value)
                           
                            B = 1
                            Po = df['openn'][x+1]
                            ATR_trolling = df['close'][x] -(ATR*j)
                            P_ATR_trolling = ATR_trolling
                           

                    else:
                        if(df['openn'][x+1]>=P_ATR_trolling):
                            ATR_trolling = df['close'][x] - (ATR*j)
                            if(float(P_ATR_trolling) < float(ATR_trolling)):
                                P_ATR_trolling = ATR_trolling


                            if(error<0):
                                if((error + ((df['high'][x+1])-Po)* value)>0):
                                    perror = perror + ((df['high'][x+1])-Po)* value
                                    #print("high value  date ",df['date'][x+1])
                                    #print("high value",(df['high'][x+1])-Po)
                                    #print("perrorperrorperrorperrorperrorperrorperror",perror)
                                    value = 1
                                    error = 0
                                
                        else:

                            #print("date     ",df['date'][x+1])
                            #print("open profit ",df['close'][x+1] - Po )
                            profit = profit + df['close'][x+1] - Po
                            #print("profit",profit)
                            

                            if((df['close'][x+1] - Po)*value <0):
                                error = error + (df['close'][x+1] - Po)*value
                                #print("final loss      ",(df['close'][x+1] - Po)*value)
                                #print("error                                       ",error)
                                value = value * 2
                            else:
                                value = 1
                                

                            #print("value                                                              ",value)
                       
                            B = 0
                            Pl = df['openn'][x+1]
                            ATR_trolling = (ATR*j)+df['close'][x]
                            P_ATR_trolling = ATR_trolling
                       
                       






                    if(value >=500):
                        print("value                                                              ",value)

                    firstATR = ATR
                    

        xprofit = (profit+loss+perror)

        if(trueproft < xprofit):
            trueproft = xprofit
            print("i  ",i,"j  ",j,"trueproft ",trueproft)
            xprofit = 0
        #print("end value",profit+loss+perror)
print("FINISHED")
