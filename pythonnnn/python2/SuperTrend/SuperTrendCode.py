import pandas as pd

company_list = ['TATAMOTORSfive']

length_list = len(company_list)

number_Period =14
multpL = 3

B = 1

pre_profit_open = 0

pre_loss_open = 0


firstATR = 0
Pre_ATR_trolling = 0



for i in range(length_list):
    print(company_list[i])
    file = company_list[i] + ".csv"
    df = pd.read_csv(file)




    for x in range((number_Period+1),len(df)):
        Sum = 0
        
        if(x == (number_Period+1)):
            for y in range(x-number_Period,number_Period):
                High_Low = (df['high'][y] - df['low'][y])
                High_PreClose = abs(df['high'][y] - df['close'][y-1])
                Low_PreClose = abs (df['low'][y] - df['close'][y-1])

                list =[High_Low,High_PreClose,Low_PreClose]

                
                if(High_Low ==High_PreClose == Low_PreClose ):
                    true_range = High_Low

                else:
                    true_range = max(list)



                Sum = Sum + true_range

            firstATR = (Sum)/number_Period
            Pre_ATR_trolling = (firstATR*multpL)+df['close'][x]
        else:
            High_Low = (df['high'][x] - df['low'][x])
            High_PreClose = abs(df['high'][x] - df['close'][x-1])
            Low_PreClose = abs (df['low'][x] - df['close'][x-1])


            list =[High_Low,High_PreClose,Low_PreClose]

                
            if(High_Low ==High_PreClose == Low_PreClose ):
                true_range = High_Low

            else:
                true_range = max(list)


            ATR = (firstATR*(number_Period-1) +true_range)/number_Period

                


            if(B == 0):
                
                if(df['close'][x]<=Pre_ATR_trolling):
                    ATR_trolling = (ATR*multpL)+(df['high'][x]+df['low'][x])/2 
                    if(float(Pre_ATR_trolling) > float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling
                    else:
                        Pre_ATR_trolling = Pre_ATR_trolling

                else:
                    B = 1
                    print("date    ",df['date'][x])
                    pre_profit_open = df['openn'][x]
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*multpL)
                    Pre_ATR_trolling = ATR_trolling
                    print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
                    
            else:
               
                if(df['close'][x] >= Pre_ATR_trolling ):
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*multpL)
                    if(float(Pre_ATR_trolling) < float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling
                else:
                    B = 0
                    pre_loss_open = df['openn'][x]
                    print("date    ",df['date'][x])
                    ATR_trolling = (ATR*multpL)+(df['high'][x]+df['low'][x])/2
                    Pre_ATR_trolling = ATR_trolling
                    print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
                    



            print("date    ",df['date'][x])
            print("close   ",df['close'][x])
            print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
            print("")
            firstATR = ATR
                        
                        
            
                    
