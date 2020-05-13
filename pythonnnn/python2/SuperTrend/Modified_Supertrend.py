import pandas as pd

company_list = ['TATAMOTORSfive']

length_list = len(company_list)

number_Period =14
ATR_multiple = 3
B = 1


alzerba = 1



pre_profit_open = 0
pre_loss_open = 0

overall_profit = 0

Error = 0


value = 1


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
                Pre_ATR_trolling = (firstATR*ATR_multiple)+df['close'][x]
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
                    ATR_trolling = (ATR*ATR_multiple)+(df['high'][x]+df['low'][x])/2 
                    if(float(Pre_ATR_trolling) > float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling
                    else:
                        Pre_ATR_trolling = Pre_ATR_trolling

                    if(Error < 0):
                        if((((pre_loss_open - df['low'][x])*value)+Error)>0):
                            overall_profit = overall_profit + abs(Error)
                            Error = 0
                            value = 1
                        
                
                    if(alzerba == 1):
                        if(df['date'][x]>='2020-02-18'):
                            pre_loss_open = df['openn'][x]
                            print("loss start date    ",df['date'][x])
                            alzerba = alzerba+1
                        

                else:
                    B = 1
                    if(df['date'][x]>='2020-02-18'):
                        print("loss",pre_loss_open - df['close'][x])
                        print("profit start date    ",df['date'][x])

                        if((pre_loss_open - df['close'][x])*value)<0:
                            value = value * 2
                        else:
                            value = 1
                        print("value                                       ",value)

                        if((pre_loss_open - df['close'][x])<0):
                            Error = Error +((pre_loss_open - df['close'][x]))

                        overall_profit = overall_profit + (pre_loss_open - df['close'][x])


                        
                    pre_profit_open = df['close'][x]
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*ATR_multiple)
                    Pre_ATR_trolling = ATR_trolling
                    #print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
                    
            else:
               
                if(df['close'][x] >= Pre_ATR_trolling ):
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*ATR_multiple)
                    if(float(Pre_ATR_trolling) < float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling

                        
                    if(Error < 0):
                        if((((df['high'][x] - pre_profit_open)*value)+Error)>0):
                            overall_profit = overall_profit + abs(Error)
                            Error = 0
                            value = 1
                        

                    if(alzerba == 1):
                        if(df['date'][x]>='2020-02-18'):
                            pre_profit_open = df['openn'][x]
                            print("profit start date    ",df['date'][x])
                            alzerba = alzerba+1
                else:
                    B = 0
                    if(df['date'][x]>='2020-02-18'):
                        print("alzerba",alzerba)
                        print("profit", df['close'][x] - pre_profit_open )
                        
                        print("loss start date    ",df['date'][x])
                        if((df['close'][x] - pre_profit_open)*value)<0:
                            value = value * 2
                        else:
                            value = 1
                        print("value                                       ",value)

                        if((df['close'][x] - pre_profit_open)<0):
                            Error = Error +(df['close'][x] - pre_profit_open)

                        overall_profit = overall_profit + (df['close'][x] - pre_profit_open)

                        
                    pre_loss_open = df['close'][x]
                    
                        
                    ATR_trolling = (ATR*ATR_multiple)+(df['high'][x]+df['low'][x])/2
                    Pre_ATR_trolling = ATR_trolling
                    #print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
                    


            firstATR = ATR

print('overall_profit',overall_profit)
                        
                        
            
                    
